"""
Dependencies; Since every class relies on these dependencies, they are imported here, and this module is imported
"""


from math import sin, cos, radians as rad, atan2, dist
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import matplotlib.image as mpimg
import json
import pygame

matplotlib.use('Agg')

# Screen
HEIGHT = 500
WIDTH = 1000
WIN = pygame.display.set_mode([WIDTH, HEIGHT])

# Color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FPS = 60
T = 1 / FPS

# Physics Constants
k = 8.98755 * (10 ** 9)
g = 9.81
e = 1.60 * (10 ** -19)

# Detail
DETAIL = 4

# Pixel to Meter Ratio
PIX_RATIO = 2.645833 * 10 ** -10