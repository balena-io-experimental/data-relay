import os
import sys
import yaml
from yamlVariableResolver import Resolver
from util import get_plugin_source

def _read_value(var_name):
    """Read and scrub environment variable value

    :return: variable value or None if not found
    """
    raw_value = os.getenv(var_name)
    if not raw_value:
        return None
    return raw_value.replace("\\n", "\n")

def invoke_plugin(plugin):
    pluginDirectory = "./plugins/"
    componentDirectory = "/app/components/"
    if plugin.TYPE == "secrets":
        componentDirectory += "secrets/"
    
    #run the invoke method, if the plugin has one
    try:
        plugin.invoke()
    except AttributeError:
        # don't need to do anything here
        None

    # load dictionary of variable names/values expected by template
    variables = {var: _read_value(var) for var in plugin.VARS}

    # if all the variables are empty, we're not configuring the plugin, so we can quit
    if not any(variables.values()):
        print("No {name} configuration details set".format(name=plugin.NAME))
        return False

    # if only some of the variables are empty, then there's a configuration issue
    if not all(variables.values()):
        print("Attempting to configure an {name} connection, but not all environment variables have been set:".format(name=plugin.NAME))
        for var, value in variables.items():
            if value:
                print("- {0} is set".format(var))
            else:
                print("- {0} is unset".format(var))

        return False

    # Use the custom YAML loader to resolve the inline variables 
    output = Resolver.resolve(pluginDirectory + plugin.FILE, variables)
    print("{name} will be configured with:".format(name=plugin.NAME))
    print(str(output))

    # write the resolved YAML to the component directory
    with open(componentDirectory + plugin.FILE, "w") as f:
        yaml.dump(output, f)

    return True

def Configure(invoke_plugin_types):
    for type in invoke_plugin_types:
        print("Finding {value} plugins to run".format(value=type))

    plugin_source = get_plugin_source()

    plugin_configured = False
    # Call each plugin
    for plugin_name in plugin_source.list_plugins():
       
        plugin = plugin_source.load_plugin(plugin_name)

        if plugin.TYPE not in invoke_plugin_types:
            continue

        print("Loading plugin " + plugin_name)
        plugin_configured |= invoke_plugin(plugin)
        # put this into state, to be used later

    if not plugin_configured:
        for type in invoke_plugin_types:
            print("No {value} plugins loaded".format(value=type))
        return 1

    return 0

invoke_plugin_types = ["input","output"]
if len(sys.argv) > 1:
    # This should use argparse
    print("balenablocks/cloud")
    print("----------------------")
    print('Intelligently connecting devices to clouds')
    invoke_plugin_types = [sys.argv[1]]

exitcode = Configure(invoke_plugin_types)

if len(sys.argv) <= 1:
    print("Finished configuring cloud block")
sys.exit(exitcode)
