from utils import D3Point
from random import randrange


class Triangle:
    __slots__ = ("p1", "p2", "p3", "color", "lines")
    def __init__(self, p1, p2, p3, lines=False, color=(0, 0, 0)):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = color
        self.lines = lines

    def render(self, camera, surface):
        p1, p2, p3 = map(camera.render_point, (self.p1, self.p2, self.p3))
        surface.draw_triangle(p1, p2, p3, self.lines, self.color)

    def overall_distance(self, camera):
        return sum(
            map(camera.distance, (self.p1, self.p2, self.p3))
        ) // 3


class Shape:
    def __init__(self, *triangles):
        self.triangles = triangles

    def overall_distance(self, camera):
        return sum(
            map(lambda triangle: triangle.overall_distance(camera), self.triangles)
        ) // len(self.triangles)

    def render(self, camera, surface):
        for triangle in reversed(sorted(self.triangles, key=lambda triangle: triangle.overall_distance(camera))):
            triangle.render(camera, surface)

    def __iter__(self):
        return iter(self.triangles)

    def __len__(self):
        return len(self.triangles)


class Cube:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        x, y, z = position
        p1 = position
        p2 = D3Point(x + size, y, z)
        p3 = D3Point(x + size, y - size, z)
        p4 = D3Point(x, y - size, z)

        p5 = D3Point(x, y, z + size)
        p6 = D3Point(x + size, y, z + size)
        p7 = D3Point(x + size, y - size, z + size)
        p8 = D3Point(x + size, y - size, z + size)

        color = (randrange(255), randrange(255), randrange(255))
        tr1 = Triangle(p1, p2, p3, color=color)
        tr2 = Triangle(p1, p4, p3, color=color)
        face1 = Shape(tr1, tr2)

        color = (randrange(255), randrange(255), randrange(255))
        tr3 = Triangle(p1, p5, p6, color=color)
        tr4 = Triangle(p1, p2, p6, color=color)
        face2 = Shape(tr3, tr4)

        # not finished
        tr5 = Triangle(p4, p3, p5)
        tr6 = Triangle(p1, p2, p6)
        face3 = Shape(tr5, tr6)

        self.faces = Shape(face1, face2)

    def overall_distance(self, camera):
        return sum(
            map(lambda shape: shape.overall_distance(camera), self.faces)
        ) // len(self.faces)

    def render(self, camera, surface):
        self.faces.render(camera, surface)
