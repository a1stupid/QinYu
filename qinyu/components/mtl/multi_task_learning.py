from qinyu.common.torch_component import TorchComponent
# from hanlp.common.torch_component import TorchComponent


class MultiTaskLearning(TorchComponent):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.model = None
        self.task = None
        self.vocabs = None


    def on_config_ready(self, **kwargs):
        pass