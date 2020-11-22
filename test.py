import pygame
from math import cos, sin

axis_x, axis_y, axis_z = 0, 1, 2

BLACK, WHITE = 0x000, 0xffffff


def mul_matrix(a, b):
    c = [[0 for _ in range(len(b[0]))]for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            total = 0
            for ii in range(len(a[0])):
                total += a[i][ii] * b[ii][j]
            c[i][j] = total

    return c


def rot_matrix(a, b, t):
    sa, ca = sin(a), cos(a)
    sb, cb = sin(b), cos(b)
    st, ct = sin(t), cos(t)
    return (
        (cb*ct, -cb*st, sb),
        (ca*st + sa*sb*ct, ca*ct - st*sa*sb, -cb*sa),
        (st*sa - ca*sb*ct, ca*st*sb + sa*ct, ca*cb)
    )


class Object:
    def __init__(self, vertices, edges, length):
        print(vertices)
        self.vertices = vertices
        self.edges = edges
        self.rotation = [3, 3, 0]
        self.len = length

    def rotate(self, axe, o):
        self.rotation[axe] += o

    def lines(self):
        location = mul_matrix(self.vertices, rot_matrix(*self.rotation))
        return ((location[v1], location[v2]) for v1, v2 in self.edges)


def line(size, vec, shape):
    return [round(shape.len * coordinate + frame / 2) for coordinate, frame in zip(vec, size)]


def draw_shape(screen, shape, size):
    for start, end in shape.lines():
        pygame.draw.line(screen, BLACK, line(size, start, shape), line(size, end, shape))


def main(screen):
    clock = pygame.time.Clock()
    size = screen.get_width(), screen.get_height()
    vertices = [(-1, -1, -1), (-1, -1, 1),
                (-1, 1, -1), (-1, 1, 1),
                (1, -1, -1), (1, -1, 1),
                (1, 1, -1), (1, 1, 1),
                (0, 0, 2.25)]
    lines = [(0, 1), (0, 2), (2, 3), (1, 3),
             (4, 5), (4, 6), (6, 7), (5, 7),
             (0, 4), (1, 5), (2, 6), (3, 7),
             (7, 8), (1, 8), (5, 8), (3, 8)]

    house = Object(vertices, lines, 70)

    rad = 0.05

    params = {pygame.K_UP: (axis_x, -rad),
              pygame.K_DOWN: (axis_x, rad),
              pygame.K_LEFT: (axis_y, -rad),
              pygame.K_RIGHT: (axis_y, rad),
              pygame.K_a: (axis_z, -rad),
              pygame.K_d: (axis_z, rad)}

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        keys = pygame.key.get_pressed()
        for key in params:
            if keys[key]:
                house.rotate(*params[key])
        screen.fill(WHITE)
        draw_shape(screen, house, size)
        pygame.display.flip()
        clock.tick(40)


if __name__ == '__main__':
    pygame.init()
    main(pygame.display.set_mode((450, 450)))
    pygame.quit()
