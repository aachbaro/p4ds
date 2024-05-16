class calculator:
    """A class a calculator"""

    def __init__(self, vector):
        """Init the calculator class"""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add method"""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiplication method"""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Substraction method"""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Division method"""
        if not object:
            raise ZeroDivisionError("Cant divide by zero")
        self.vector = [x / object for x in self.vector]
        print(self.vector)