from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    def __init__(self, first_name: str, is_alive=True):
        """init the baratheon"""
        self.first_name = first_name
        self.family_name = 'Baratheon'
        self.is_alive = is_alive
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """The baratheon dies"""
        self.is_alive = False

    def __str__(self):
        """Return a description of the object"""
        return f"{self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        """Return a description of the object"""
        return f"{self.family_name, self.eyes, self.hairs}"

class Lannister(Character):
    """Representing the Lannister family."""
    def __init__(self, first_name: str, is_alive=True):
        """init the Lannister"""
        self.first_name = first_name
        self.family_name = 'Lannister'
        self.is_alive = is_alive
        self.eyes = "blue"
        self.hairs = "light"

    @staticmethod
    def create_lannister(first_name, is_alive=True):
        """Returns a new Lannister"""
        return Lannister(first_name, is_alive)


    def die(self):
        """The lannister dies"""
        self.is_alive = False

    def __str__(self):
        """Return a description of the object"""
        return f"{self.family_name, self.eyes, self.hairs}"

    def __repr__(self):
        """Return a description of the object"""
        return f"{self.family_name, self.eyes, self.hairs}"
