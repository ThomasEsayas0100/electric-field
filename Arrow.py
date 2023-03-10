from PointCharge import *


class Arrow:
    instances = []

    def __init__(self, xy, dir=0, mag=0):
        self.__class__.instances.append(self)
        self.mag = mag
        self.dir = dir
        self.xy = xy

    def update(self):
        e_total = np.array([0, 0])
        for charge in PointCharge.instances:
            radius = np.hypot(charge.xy[1] - self.xy[1], charge.xy[0] - self.xy[0])
            self.mag = k * charge.charge / radius
            ang = atan2(charge.xy[1] - self.xy[1], charge.xy[0] - self.xy[0])
            e_current = np.array([self.mag * cos(ang), self.mag * sin(ang)])
            e_total = np.add.reduce([e_total, e_current])
            self.dir = atan2(e_total[1], e_total[0])

    def draw(self, width=1):
        self.update()
        length = int(100 / DETAIL) * .7
        start_pos = (self.xy[0] - length / 2 * cos(self.dir), self.xy[1] - length / 2 * sin(self.dir))
        end_pos = (self.xy[0] + length / 2 * cos(self.dir), self.xy[1] + length / 2 * sin(self.dir))


        a = np.array(np.array(end_pos) - np.array(start_pos))
        b = np.array(start_pos)
        b += np.array([5*cos(self.dir + rad(180-15)), 5*sin(self.dir + rad(180-15))])

        c = np.array(start_pos)
        c += np.array([5 * cos(self.dir - rad(180 - 15)), 5 * sin(self.dir - rad(180 - 15))])

        return ([start_pos[0], start_pos[1]], [end_pos[0], end_pos[1]], [(a + b)[0], (a + b)[1]], [(a + c)[0], (a + c)[1]])


