import os
import yaml
from yamlVariableResolver import Resolver

def invoke():
    # these are constant
    pluginDirectory = "./plugins/"
    componentDirectory = "/app/components/"

    # these are plugin/component specific
    componentName = "GCP Pubsub"
    filename = "GcpPubsubOutput.yaml"
    topic = os.environ.get('GCP_PUBSUB_TOPIC')
    pubsubType = os.environ.get('GCP_PUBSUB_TYPE')
    projectId = os.environ.get('GCP_PUBSUB_PROJECT_ID')
    privateKeyId = os.environ.get('CP_PUBSUB_PRIVATE_KEY_ID')
    clientEmail = os.environ.get('GCP_PUBSUB_CLIENT_EMAIL')
    clientId = os.environ.get('GCP_PUBSUB_CLIENT_ID')
    authUri = os.environ.get('GCP_PUBSUB_AUTH_URI')
    tokenUri = os.environ.get('GCP_PUBSUB_TOKEN_URI')
    authProviderCertUrl = os.environ.get('GCP_PUBSUB_AUTH_PROVIDER_X509_CERT_URL')
    clientCertUrl = os.environ.get('GCP_PUBSUB_CLIENT_X509_CERT_URL')
    privateKey = os.environ.get('GCP_PUBSUB_PRIVATE_KEY')

    variableList = [topic, pubsubType, projectId, privateKeyId, clientEmail, clientId, authUri, tokenUri, authProviderCertUrl, clientCertUrl, privateKey]

    # if all the variables are empty, we're not configuring an GCP Pubsub, so we can quit
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
