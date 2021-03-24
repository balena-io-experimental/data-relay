import os
import sys
from functools import partial
from pluginbase import PluginBase
from plugins import AzureSecretsKeyvault

def Configure():
    AzureSecretsKeyvault.invoke()
    

print("balenablocks/cloud")
print("----------------------")
print('Intelligently connecting devices to clouds')
Configure()
print("Finished configuring cloud block")