### Adapted from: ###
# https://gist.github.com/mkaranasou/ba83e25c835a8f7629e34dd7ede01931

import os
import re
import yaml

class Resolver():

    ################
    # Load a yaml configuration file and resolve any environment variables
    # The environment variables must have !ENV before them and be in this format
    # to be parsed: ${VAR_NAME}.
    ################
    def resolve(path=None, data=None, tag='!ENV'):

        # pattern for global vars: look for ${variable}
        pattern = re.compile('.*?\${(\w+)}.*?')
        loader = yaml.SafeLoader

        # the tag will be used to mark where to start searching for the pattern
        # e.g. somekey: !ENV somestring${MYENVVAR}blah blah blah
        loader.add_implicit_resolver(tag, pattern, None)

        ################
        # Extracts the environment variable from the node's value
        # :param yaml.Loader loader: the yaml loader
        # :param node: the current node in the yaml
        # :return: the parsed string that contains the value of the environment
        # variable
        ################
        def constructor_env_variables(loader, node):
            value = loader.construct_scalar(node)
            match = pattern.findall(value)  # to find all env variables in line
            if match:
                full_value = value
                for g in match:
                    full_value = full_value.replace(f'${{{g}}}', data[g])
                #print("full_value is {}".format(full_value))
                return full_value
            return value

        loader.add_constructor(tag, constructor_env_variables)
        # Change directory to this file's location
        os.chdir(os.path.dirname(__file__))

        if path:
            with open(path) as conf_data:
                return yaml.load(conf_data, Loader=loader)
        else:
            raise ValueError('Path must be passed in. Exiting.')
