import abc
from entity.tasks.task import Task


class EngineInterface(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def run(self, task: Task):
        return NotImplemented
