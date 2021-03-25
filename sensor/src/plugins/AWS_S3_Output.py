import os
import yaml
from yamlVariableResolver import Resolver

PLUGIN_TYPE = "output"

def invoke():
    # these are constant
    pluginDirectory = "./plugins/"
    componentDirectory = "/app/components/"

    # these are plugin/component specific
    componentName = "AWS S3"
    filename = "AWS_S3_Output.yaml"
    bucket = os.environ.get('AWS_S3_BUCKET')
    region = os.environ.get('AWS_S3_REGION')
    accesskey = os.environ.get('AWS_ACCESS_KEY')
    secretkey = os.environ.get('AWS_SECRET_KEY')
    variableList = [bucket, region, accesskey, secretkey]

    # if all the variables are empty, we're not configuring an SQS, so we can quit
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
