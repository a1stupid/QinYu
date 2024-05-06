import os
from abc import ABC

from qinyu_common.configurable import Configurable
from qinyu_common.structure import SerializableDict
from qinyu.common.component import Component


class TorchComponent(Component, ABC):
    def __init__(self):
        super().__init__()
        self.config = SerializableDict()
        self.model = None
        self.vocabs = None

    def load_config(self, save_dir: str, file_name='config.json', **kwargs):
        self.config.load_json(os.path.join(save_dir, file_name))
        self.config.update(kwargs)
        for k, v in self.config:
            if isinstance(v, dict) and 'classpath' in v:
                self.config[k] = Configurable.from_config(v)
        self.on_config_ready(**self.config, save_dir = save_dir)
        print()


    def load(self, save_dir: str, devices=None, verbose=True, **kwargs):
        self.load_config(save_dir)
        self.load_vocabs(save_dir)

