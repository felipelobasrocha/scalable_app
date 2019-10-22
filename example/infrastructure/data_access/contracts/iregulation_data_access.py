from abc import ABCMeta, abstractmethod

class IRegulationDataAccess:

    @abstractmethod
    def get_minimum_age(self): pass
