import os
import sys
import yaml
from yamlVariableResolver import Resolver
from util import get_plugin_source

def invoke_plugin(plugin):
    pluginDirectory = "./plugins/"
    componentDirectory = "/app/components/"
    if plugin.TYPE == "secrets":
        componentDirectory += "secrets/"

    variables = {var: os.getenv(var) for var in plugin.VARS}

    # if all the variables are empty, we're not configuring the plugin, so we can quit
    if not any(variables.values()):
        print("No {name} connection details set".format(name=plugin.NAME))
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
    output = Resolver.resolve(pluginDirectory + plugin.FILE)
    print("{name} will be configured with:".format(name=plugin.NAME))
    print(str(output))

    # write the resolved YAML to the component directory
    with open(componentDirectory + plugin.FILE, "w") as f:
        yaml.dump(output, f)

    return True

def Configure():
    invoke_plugin_type = "output"
    if len(sys.argv) > 1:
        # This should use argparse
        invoke_plugin_type = sys.argv[1]

    print("Finding cloud block plugins to run")
    plugin_source = get_plugin_source()

    plugin_configured = False
    # Call each plugin
    for plugin_name in plugin_source.list_plugins():
        print("Loading plugin " + plugin_name)
        plugin = plugin_source.load_plugin(plugin_name)

        if plugin.TYPE != invoke_plugin_type:
            continue

        plugin_configured |= invoke_plugin(plugin)

    if not plugin_configured:
        print("No {0} plugins were configured".format(invoke_plugin_type))
        return 1

    return 0

print("balenablocks/cloud")
print("----------------------")
print('Intelligently connecting devices to clouds')
exitcode = Configure()
print("Finished configuring cloud block")
sys.exit(exitcode)
