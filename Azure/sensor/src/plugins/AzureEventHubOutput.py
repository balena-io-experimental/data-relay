import os
import yaml
from yamlVariableResolver import Resolver

def invoke():
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
    
    output = Resolver.resolve('./plugins/AzureEventHubOutput.yaml')
    print(str(output))
    # os.chdir(os.path.dirname(__file__))
    # print(os.getcwd())
    f = open('/app/components/AzureEventHubOutput.yaml', 'w')
    f.write(yaml.dump(output))
    f.close()


