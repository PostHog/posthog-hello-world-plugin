from abc import ABC, abstractmethod

class Plugin(ABC):

    @abstractmethod
    def process_event(self, event):
        pass

    @abstractmethod
    def process_person(self, event):
        pass

    @abstractmethod
    def process_identify(self, event):
        pass
