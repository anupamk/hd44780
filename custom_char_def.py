# a rudimentary class defining a custom character. 
class CustomCharacter:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)

