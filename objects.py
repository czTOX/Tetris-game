

class Shape:
    def __init__(self): 
        pass


class Oshape(Shape):
    def __init__(self, squeare):
        self.squeare = squeare
        self.structure = { 0, 0, 0, 0,
                           0, 1, 1, 0,
                           0, 1, 1, 0,
                           0, 0, 0, 0 }


class Ishape(Shape):
    def __init__(self, squeare):
        self.squeare = squeare
        self.structure = { 0, 0, 0, 0,
                           1, 1, 1, 1,
                           0, 0, 0, 0,
                           0, 0, 0, 0 }                           


class Sshape(Shape):
    def __init__(self, squeare):
        self.squeare = squeare
        self.structure = { 0, 0, 0, 0,
                           0, 0, 1, 1,
                           0, 1, 1, 0,
                           0, 0, 0, 0 }


class Zshape(Shape):
    def __init__(self, squeare):
        self.squeare = squeare
        self.structure = { 0, 0, 0, 0,
                           0, 1, 1, 0,
                           0, 0, 1, 1,
                           0, 0, 0, 0 }                           


class Lshape(Shape):
    def __init__(self, squeare):
        self.squeare = squeare
        self.structure = { 0, 0, 0, 0,
                           0, 1, 1, 1,
                           0, 1, 0, 0,
                           0, 0, 0, 0 }


class Jshape(Shape):
    def __init__(self, squeare):
        self.squeare = squeare
        self.structure = { 0, 0, 0, 0,
                           0, 1, 1, 1,
                           0, 0, 0, 1,
                           0, 0, 0, 0 }       


class Tshape(Shape):
    def __init__(self, squeare):
        self.squeare = squeare
        self.structure = { 0, 0, 0, 0,
                           0, 1, 1, 1,
                           0, 0, 1, 0,
                           0, 0, 0, 0 }