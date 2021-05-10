### Adapted from: ###
# https://gist.github.com/mkaranasou/ba83e25c835a8f7629e34dd7ede01931

import os
import re
import yaml

class Resolver():

    def resolve(path=None, data=None, tag='!ENV'):
        """
        Load a templated YAML configuration file, and substitute values from the
        provided 'data' dictionary into named tags marked in the file. A named tag
        is in the form: "<tag> ${<name>}". In this text:

            Lorem ipsum !ENV ${GCP_PUBSUB_TOPIC} sit amet

        the tag is "!ENV" and the name is "GCP_PUBSUB_TOPIC". If the value in 'data'
        for the key 'GCP_PUBSUB_TOPIC' is 'dolet', the result is:

            Lorem ipsum dolet sit amet

        :tag: Identifier for a <tag>
        :data: dictionary, where a key is the <name> for a tag, and a value is the
        value to be substituted for the named tag
        :return: loaded YAML list/dictionary with substituted text
        """

        # pattern for tag name
        pattern = re.compile('.*?\${(\w+)}.*?')
        loader = yaml.SafeLoader

        loader.add_implicit_resolver(tag, pattern, None)

        def value_constructor(loader, node):
            """
            Extracts the environment variable from the node's value
            
            :param yaml.Loader loader: the yaml loader
            :param node: the current node in the yaml
            :return: the parsed string that contains the value
            """
            value = loader.construct_scalar(node)
            match = pattern.findall(value)  # to find all env variables in line
            if match:
                full_value = value
                for g in match:
                    full_value = full_value.replace(f'${{{g}}}', data[g])
                #print("full_value is {}".format(full_value))
                return full_value
            return value

        loader.add_constructor(tag, value_constructor)
        # Change directory to this file's location
        os.chdir(os.path.dirname(__file__))

        if path:
            with open(path) as conf_data:
                return yaml.load(conf_data, Loader=loader)
        else:
            raise ValueError('Path must be passed in. Exiting.')
