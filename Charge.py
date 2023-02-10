from PointCharge import *

class Charge:
    def __init__(self, xy):
        self.vel = np.array([0, 0])
        self.xy = xy
        self.f_total = np.array([0, 0])
        self.charge = e


        # Constants
        self.M = 1.67 * 10 ** -13

    def move(self):
        e_total = np.array([0, 0])

        for charge in PointCharge.instances:
            # Setting up formula for Electric Field calc
            radius = np.hypot(charge.xy[1] - self.xy[1], charge.xy[0] - self.xy[0])*PIX_RATIO
            e_mag = k * charge.charge / radius*PIX_RATIO
            ang = atan2(charge.xy[1] - self.xy[1], charge.xy[0] - self.xy[0])
            # Calculating the Electric Field vector of current charge within for loop
            e_current = np.array([e_mag * cos(ang), e_mag * sin(ang)])
            # Adding
            e_total = np.add.reduce([e_total, e_current])
            self.f_total = e_total

        ang = atan2(self.f_total[1], self.f_total[0])
        mag_force = np.linalg.norm(self.f_total)
        acc = np.array([mag_force / self.M * cos(ang), mag_force / self.M * sin(ang)])
        self.vel = np.add.reduce([self.vel, acc * T])
        self.xy = (self.xy + (self.vel * T) + (1 / 2 * acc * T ** 2))

        if self.xy[0] <= 0:
            self.xy[0] = 0
        if self.xy[0] >= 1000:
            self.xy[0] = 1000

        if self.xy[1] <= 0:
            self.xy[1] = 0
        if self.xy[1] >= 500:
            self.xy[1] = 500

        pygame.draw.circle(WIN, BLACK, self.xy, 5)

        end_pos = (self.xy[0] + 30 * cos(ang), self.xy[1] + 30 * sin(ang))

        pygame.draw.line(WIN, RED, self.xy, end_pos)