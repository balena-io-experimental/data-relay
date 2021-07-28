import os
from functools import partial
from pluginbase import PluginBase

def get_plugin_source():
    """Creates and returns a 'plugin_source' object as defined by PluginBase,
       which provides access plugins.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    get_path = partial(os.path.join, here)
    plugin_base = PluginBase(package='plugins')
    plugin_source = plugin_base.make_plugin_source(searchpath=[get_path('plugins')])

    return plugin_source
