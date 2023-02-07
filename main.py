from Charge import *
from Arrow import *
pygame.init()

"""
Constant Declaration
"""

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


def draw_window():
    WIN.fill(WHITE)
    for i in range(int(WIDTH / (100 / DETAIL))):
        for j in range(int(HEIGHT / (50 / DETAIL))):
            a = Arrow((i * 104 / DETAIL, j * 104 / DETAIL))
            a.draw()

    for pointCharge in PointCharge.instances:
        pointCharge.draw()

    z.move()


w = PointCharge((500, 250), -e)
x = PointCharge((300, 250), e)
y = PointCharge((700, 250), -e)
z = Charge((100, 100))


def main():
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18, bold=True)

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
        fps = str(int(clock.get_fps()))
        fps_t = font.render(fps, True, pygame.Color("RED"))
        WIN.blit(fps_t, (0, 0))
        pygame.display.update()
    pygame.quit()


if __name__ == '__main__':
    main()
