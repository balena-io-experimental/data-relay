import os
import sys
from functools import partial
from pluginbase import PluginBase

def Configure():
    print("Finding cloud block plugins to run")
    # Use PluginBase to find the plugins
    here = os.path.abspath(os.path.dirname(__file__))
    get_path = partial(os.path.join, here)
    plugin_base = PluginBase(package='plugins')
    plugin_source = plugin_base.make_plugin_source(searchpath=[get_path('plugins')])

    # Call each plugin 
    for plugin_name in plugin_source.list_plugins():
        print("Loading plugin " + plugin_name)
        plugin = plugin_source.load_plugin(plugin_name)
        plugin.invoke()

print("balenablocks/cloud")
print("----------------------")
print('Intelligently connecting devices to clouds')
Configure()
print("Finished configuring cloud block")