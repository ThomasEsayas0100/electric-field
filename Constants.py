"""
Dependencies; Since every class relies on these dependencies, they are imported here, and this module is imported
"""

from math import sin, cos, atan2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pygame

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