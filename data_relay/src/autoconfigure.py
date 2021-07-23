"""
Handles configuration of data relay block to run dapr. Writes dapr component configurations
by applying required values read from environment variables or secret store contents
to dapr configuration template files.
See plugins/README.md for important background.

If DAPR_DEBUG environment variable is defined, enables debug logging when reading
dapr secret store.

Exits with 0 if at least one plugin found, otherwise exits with 1.

Copyright 2021 balena inc.
"""
import os
import sys
import traceback
import yaml
import getSecrets as secret_reader
from yamlVariableResolver import Resolver
from util import get_plugin_source

# constants to identify plugin types
PLUGIN_TYPE_SECRETS = "secrets"
PLUGIN_TYPE_LOCAL = "local"
PLUGIN_TYPE_REMOTE = "remote"

# Directory to contain dapr component configuration files
component_directory = "/app/components/"

# All variables read from environment variables or from secret stores.
# A value is None if already queried but not found.
all_vars = {}

# True if secretReader module is available and ready to use
has_secret_reader = False

# Map of secret store name to URL segment required by dapr to lookup secrets
secret_store_urls = {}
secret_store_urls["Azure Secrets"] = "azure-keyvault"
secret_store_urls["GCP Secrets"] = "gcp-secret-manager"
secret_store_urls["AWS Secrets"] = "aws-secrets-manager"

def _read_value(var_name):
    """Read and scrub value read from environment variable or secret store.
    Environment variable value has precedence over secret store.

    :return: variable value or None if not found
    """
    value = os.getenv(var_name)
    if value == None:
        if has_secret_reader:
            # secret name in form like 'gcp-topic' rather than 'GCP_TOPIC'
            name = var_name.replace("_", "-").lower()
            value = secret_reader.read_value(name)

    if value != None:
        value = value.replace("\\n", "\n")
    return value


def write_config(plugin):
    """Writes a dapr component configuration from a provided template plugin.

    :return: True if successful; otherwise False
    """
    pluginDirectory = "./plugins/"

    # run optional invoke() method if present
    try:
        plugin.invoke()
    except AttributeError:
        # invoke() not found
        pass

    # load dictionary of variable names/values expected by template
    var_count = len(plugin.VARS)
    found_count = 0
    for var in plugin.VARS:
        if not var in all_vars:
            all_vars[var] = _read_value(var)

        if all_vars[var] != None:
            found_count += 1

    # if all the variables are empty, we're not configuring the plugin, so we can quit
    if found_count == 0:
        print("No {name} configuration details set".format(name=plugin.NAME))
        return False

    # if only some of the variables are empty, then there's a configuration issue
    if found_count < var_count:
        print("Attempting to configure {name} connection, but not all environment variables have been set:".format(name=plugin.NAME))
        for var in plugin.VARS:
            if all_vars[var]:
                print("- {0} is set".format(var))
            else:
                print("- {0} is unset".format(var))
        return False

    # Use the custom YAML loader to resolve the inline variables 
    output = Resolver.resolve(pluginDirectory + plugin.FILE, all_vars)
    print("{name} will be configured with:".format(name=plugin.NAME))
    print(str(output))

    # write the resolved YAML to the component directory
    with open(component_directory + plugin.FILE, "w") as f:
        yaml.dump(output, f)

    return True

def configure(plugin_type):
    """Write dapr component configuration files for the provided type.

    :return: List of names of configured plugins; empty if none
    """
    types = ""
    print("Finding {} plugins to run".format(plugin_type))

    plugin_source = get_plugin_source()

    configured_plugins = []
    # Call each plugin
    for plugin_name in plugin_source.list_plugins():
       
        plugin = plugin_source.load_plugin(plugin_name)
        if plugin.TYPE != plugin_type:
            continue

        if write_config(plugin):
            configured_plugins.append(plugin.NAME)

    if not configured_plugins:
        print("No {} plugins loaded".format(plugin_type))

    return configured_plugins


print("Data Relay block ==> build component configurations")
exitCode = 0

# First try to configure and open a secret store because it may hold values for
# other components. Expect only a *single* secret store is configured.
secret_plugins = configure(PLUGIN_TYPE_SECRETS)
if secret_plugins:
    if len(secret_plugins) > 1:
        print("Using first secret store plugin: {}".format(plugin_name))

    plugin_name = secret_plugins[0]
    if plugin_name in secret_store_urls:
        has_secret_reader = secret_reader.open(secret_store_urls[plugin_name],
                                component_directory, bool(os.getenv("DAPR_DEBUG")))
    else:
        print("Can't open secret reader for store: {}".format(plugin_name))
        exitCode = 1

# Now configure local and remote plugins from environment variables or secret store values.
if exitCode == 0:
    try:
        count = len(configure(PLUGIN_TYPE_LOCAL))
        count += len(configure(PLUGIN_TYPE_REMOTE))
        if count == 0:
            exitCode = 1
    except Exception as e:
        exitCode = 1
        print("Error configuring plugins: {}".format(e))
        traceback.print_exc(file=sys.stdout)
    finally:
        if has_secret_reader:
            secret_reader.close()

sys.exit(exitCode)
