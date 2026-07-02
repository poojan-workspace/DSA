'''
super() method in python
'''


class BaseChai:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size
    

class GingerChai(BaseChai):
    def __init__(self, type_, size, spice_level):
        self.type = type_
        self.size = size
        self.spice_level = spice_level


class GingerChai(BaseChai):

    def __init__(self, type_, size, spice_level):
        # this is exactly the same as >> BaseChai.__init__(self, type_, size)
        super().__init__(type_, size)
        self.spice_level = spice_level