import os
import sys
from functools import partial
from pluginbase import PluginBase

def Configure():
    invoke_plugin_type = "output"
    if len(sys.argv) > 1:
        # This should use argparse
        invoke_plugin_type = sys.argv[1]

    print("Finding cloud block plugins to run")
    # Use PluginBase to find the plugins
    here = os.path.abspath(os.path.dirname(__file__))
    get_path = partial(os.path.join, here)
    plugin_base = PluginBase(package='plugins')
    plugin_source = plugin_base.make_plugin_source(searchpath=[get_path('plugins')])

    plugin_configured = False
    # Call each plugin
    for plugin_name in plugin_source.list_plugins():
        print("Loading plugin " + plugin_name)
        plugin = plugin_source.load_plugin(plugin_name)

        if plugin.PLUGIN_TYPE != invoke_plugin_type:
            continue

        plugin_configured |= plugin.invoke()

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
