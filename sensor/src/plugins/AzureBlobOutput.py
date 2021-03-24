import os
import yaml
from yamlVariableResolver import Resolver

def invoke():
    # these are constant
    pluginDirectory = "./plugins/"
    componentDirectory = "/app/components/"

    # these are plugin/component specific
    componentName = "Azure BLOB storage"
    filename = "AzureBlobOutput.yaml"
    storageAccount = os.environ.get('AZURE_BLOB_STORAGE_ACCOUNT')
    storageAccountKey = os.environ.get('AZURE_BLOB_STORAGE_ACCOUNT_KEY')
    storageContainerName = os.environ.get('AZURE_BLOB_CONTAINER_NAME')
    variableList = [storageAccount, storageAccountKey, storageContainerName]

    # if all the variables are empty, we're not configuring an EventHub, so we can quit
    if not any(variableList):
        print("No {name} connection details set".format(name=componentName))
        return

    # if only some of the variables are empty, then there's a configuration issue
    if not all(variableList):
        print("Attempting to configure an {name} connection, but not all environment variables have been set.".format(name=componentName))
        return
    
    # Use the custom YAML loader to resolve the inline variables 
    output = Resolver.resolve(pluginDirectory + filename)
    print("{name} will be configured with:".format(name=componentName))
    print(str(output))

    # write the resolved YAML to the component directory
    f = open(componentDirectory + filename, 'w')
    f.write(yaml.dump(output))
    f.close()