import pygame
from camera import Camera
from collections import deque


class Screen:
    SCALE = 50
    def __init__(self, screen, camera, origin, *shapes):
        self.screen = screen
        self.camera = camera
        self.origin = origin
        self.shapes = shapes

    def draw_triangle(self, p1, p2, p3, lines=False, color=(0, 0, 0)):
        dx, dy = self.origin
        p1, p2, p3 = map((lambda n: (dx + n[0] * self.SCALE, dy + n[1] * self.SCALE)), (p1, p2, p3))

        if not lines:
            pygame.draw.polygon(self.screen, color, (p1, p2, p3))
        else:
            points = deque((p1, p2, p3))
            last = points[0]
            points.rotate(-1)
            for point in points:
                pygame.draw.line(self.screen, (0, 0, 0), last, point, 1)
                last = point

    def draw(self):
        for shape in reversed(sorted(self.shapes, key=lambda shape: shape.overall_distance(self.camera))):
            shape.render(self.camera, self)