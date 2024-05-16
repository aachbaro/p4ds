from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract class to create Character"""
    def __init__(self, first_name: str, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        
    @abstractmethod
    def die(self):
        pass
    

class Stark(Character):
    """Inherit from the Character class, create a Stark Character"""
    def die(self):
        """The stark character dies"""
        self.is_alive = False