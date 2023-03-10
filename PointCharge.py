from Constants import *

class PointCharge:
    instances = []

    def __init__(self, xy, charge):
        self.__class__.instances.append(self)
        self.xy = xy
        self.charge = charge

    def update(self, xy):
        self.xy = xy

    def draw(self):
        return [self.xy[0], self.xy[1]]