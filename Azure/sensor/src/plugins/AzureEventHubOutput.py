import os
import yaml
from yamlVariableResolver import Resolver

def invoke():
    filename = "AzureEventHubOutput.yaml"
    pluginDirectory = "./plugins/"
    componentDirectory = "/app/components/"

    connectionString = os.environ.get('AZURE_EH_CONNECTIONSTRING')
    consumerGroup = os.environ.get('AZURE_EH_CONSUMER_GROUP')
    storageAccount = os.environ.get('AZURE_EH_STORAGE_ACCOUNT')
    storageAccountKey = os.environ.get('AZURE_EH_STORAGE_ACCOUNT_KEY')
    storageContainerName = os.environ.get('AZURE_EH_CONTAINER_NAME')
    variableList = [connectionString, consumerGroup, storageAccount, storageAccountKey, storageContainerName]

    # if all the variables are empty, we're not configuring an EventHub, so we can quit
    if not any(variableList):
        print("No Azure EventHub connection details set.")
        return

    # if only some of the variables are empty, then there's a configuration issue
    if not all(variableList):
        print("Attempting to configure an Azure EventHub connection, but not all environment variables have been set.")
        return
    
    # Use the custom YAML loader to resolve the inline variables 
    output = Resolver.resolve(pluginDirectory + filename)
    print("Azure EventHub will be configured with:")
    print(str(output))

    # write the resolved YAML to the component directory
    f = open(componentDirectory + filename, 'w')
    f.write(yaml.dump(output))
    f.close()


