from abc import abstractmethod


class Rule:
    def __init__(self):
        super().__init__()

    @abstractmethod
    def __call__(self, *args, **kwargs):
        ...
