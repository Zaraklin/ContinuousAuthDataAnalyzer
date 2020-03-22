class KeyPressed(object):
    def __init__(self, data):
        self.__dict__                = data
        self.intervalBetweenKeyPress = self.__dict__["intervalBetweenKeyPress"]
        self.keyPressed              = self.__dict__["keyPressed"]

    def __repr__(self):
        return str(self)

    def __str__(self):
        return str(self.intervalBetweenKeyPress) + "," + "'" + str(self.keyPressed) + "'"

    def __int__(self):
        return int(self.intervalBetweenKeyPress)

    def __lt__(self, other):
        return int(self.intervalBetweenKeyPress) < int(other.intervalBetweenKeyPress)

    def __le__(self, other):
        return int(self.intervalBetweenKeyPress) <= int(other.intervalBetweenKeyPress)

    def __gt__(self, other):
        return int(self.intervalBetweenKeyPress) > int(other.intervalBetweenKeyPress)

    def __ge__(self, other):
        return int(self.intervalBetweenKeyPress) > int(other.intervalBetweenKeyPress)

    def __eq__(self, other):
        return int(self.intervalBetweenKeyPress) == int(other.intervalBetweenKeyPress)

    def __ne__(self, other):
        return int(self.intervalBetweenKeyPress) != int(other.intervalBetweenKeyPress)

    def __radd__(self, other):
        return self.intervalBetweenKeyPress + int(other)

    def __iadd__(self, other):
        return self.intervalBetweenKeyPress + int(other)

    def __sum__(self, other):
        return self.intervalBetweenKeyPress + int(other)

    def __rsub__(self, other):
        return self.intervalBetweenKeyPress - int(other)

    def __isub__(self, other):
        return self.intervalBetweenKeyPress - int(other)
    
    def __sub__(self, other):
        return self.intervalBetweenKeyPress - int(other)

    def __rtruediv__(self, other):
        return self.intervalBetweenKeyPress / int(other)

    def __truediv__(self, other):
        return self.intervalBetweenKeyPress / int(other)

    def __rfloordiv__(self, other):
        return self.intervalBetweenKeyPress / int(other)

    def __floordiv__(self, other):
        return self.intervalBetweenKeyPress / int(other)