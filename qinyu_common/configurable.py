import dict

from qinyu_common.reflection import str_to_type


class Configurable:
    def from_config(config: dict, **kwargs):
        cls = config.get('classpath', None)
        cls = str_to_type(cls)
        deserialized_config = dict(cls)
        for k, v in config.item():
            if isinstance(v, dict) and 'classpath' in v:
                deserialized_config[k] = Configurable.from_config(v)
        deserialized_config.pop('classpath')
        return cls(**deserialized_config)