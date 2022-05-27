
from wing_class import Wing

class Spar(Wing):
    def __init__(self, geometry, b):
        super().__init__(b)
        self.__geometry = geometry

    def __repr__(self):
        pass

if __name__ == '__main__':
    pass