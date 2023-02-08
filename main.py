from Charge import *
from Arrow import *
from EquipotentialLines import *
pygame.init()


def draw_window():
    WIN.fill(WHITE)
    for i in range(int(WIDTH / (100 / DETAIL))):
        for j in range(int(HEIGHT / (50 / DETAIL))):
            a = Arrow((i * 104 / DETAIL, j * 104 / DETAIL))
            a.draw()

    for pointCharge in PointCharge.instances:
        pointCharge.draw()
    equipotential_lines()
    z.move()


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
