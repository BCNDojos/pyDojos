from abc import ABCMeta, abstractmethod


class PunchService(metaclass=ABCMeta):

    @abstractmethod
    def punch(self):
        pass
