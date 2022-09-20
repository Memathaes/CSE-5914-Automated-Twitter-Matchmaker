from abc import ABC, abstractmethod

class DataGetter(ABC):
    @abstractmethod
    def get_Data(usrname):
        pass