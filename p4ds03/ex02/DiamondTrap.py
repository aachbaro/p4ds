from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
    def set_eyes(self, color):
        """Set a new eyes color for the king"""
        self.eyes = color
    
    def set_hairs(self, color):
        """Set a new hair color for the king"""
        self.hairs = color
    
    def get_eyes(self):
        """Returns the eyes color of the king"""
        return self.eyes

    def get_hairs(self):
        """Returns the hair color of the king"""
        return self.hairs

    