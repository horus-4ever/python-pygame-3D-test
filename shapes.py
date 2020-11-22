from utils import D3Point
from random import randrange


class Triangle:
    __slots__ = ("p1", "p2", "p3", "color", "lines", "center")
    def __init__(self, p1, p2, p3, lines=False, color=(0, 0, 0)):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.color = color
        self.lines = lines
        self.center = D3Point(
            *map(
                lambda n: sum(n) / 3,
                zip(self.p1, self.p2, self.p3)
            )
        )

    def render(self, camera, surface):
        p1, p2, p3 = map(camera.render_point, (self.p1, self.p2, self.p3))
        """for ((x1, y1), (x2, y2))
        if any(map(lambda n: n[0]> 50 or n[0] < -50 or n[1] > 50 or n[1] < -50, (p1, p2, p3))):
            return"""
        surface.draw_triangle(p1, p2, p3, self.lines, self.color)

    def can_render(self, camera):
        """
        for p in (self.p1, self.p2, self.p3):
            if not camera.can_render(p):
                return False
        return True
        """
        if camera.can_render_from_distance(self.center):
            for p in (self.p1, self.p2, self.p3):
                if not camera.can_render(p):
                    return False
            return True
        return False

    def overall_distance(self, camera):
        return sum(
            map(camera.distance, (self.p1, self.p2, self.p3))
        ) // 3


class Shape:
    def __init__(self, *triangles):
        self.triangles = triangles
        self.center = D3Point(
            *map(
                lambda n: sum(n) / len(triangles),
                zip(*map(lambda shape: shape.center, triangles))
            )
        )

    def overall_distance(self, camera):
        return sum(
            map(lambda triangle: triangle.overall_distance(camera), self.triangles)
        ) // len(self.triangles)
        return camera.distance(self.center)

    def render(self, camera, surface):
        for triangle in sorted(self.triangles, key=lambda triangle: triangle.overall_distance(camera), reverse=True):
            triangle.render(camera, surface)

    def can_render(self, camera):
        """
        for shape in self.triangles:
            if not shape.can_render(camera):
                return False
        return True
        """
        if camera.can_render_from_distance(self.center):
            for shape in self.triangles:
                if not shape.can_render(camera):
                    return False
            return True
        return False

    def __iter__(self):
        return iter(self.triangles)

    def __len__(self):
        return len(self.triangles)


class Cube(Shape):
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
        p8 = D3Point(x, y - size, z + size)

        color = (50, randrange(255), 0)
        tr1 = Triangle(p1, p2, p3, color=color)
        tr2 = Triangle(p1, p4, p3, color=color)
        face1 = Shape(tr1, tr2)

        color = (50, randrange(255), 0)
        tr3 = Triangle(p1, p5, p6, color=color)
        tr4 = Triangle(p1, p2, p6, color=color)
        face2 = Shape(tr3, tr4)

        # not finished
        color = (50, randrange(255), 0)
        tr5 = Triangle(p4, p3, p7, color=color)
        tr6 = Triangle(p4, p8, p7, color=color)
        face3 = Shape(tr5, tr6)

        color = (50, randrange(255), 0)
        tr7 = Triangle(p2, p3, p7, color=color)
        tr8 = Triangle(p2, p6, p7, color=color)
        face4 = Shape(tr7, tr8)

        color = (50, randrange(255), 0)
        tr9 = Triangle(p1, p5, p8, color=color)
        tr10 = Triangle(p1, p4, p8, color=color)
        face5 = Shape(tr9, tr10)

        color = (50, randrange(255), 0)
        tr11 = Triangle(p5, p6, p7, color=color)
        tr12 = Triangle(p5, p8, p7, color=color)
        face6 = Shape(tr11, tr12)

        super().__init__(face1, face2, face3, face4, face5, face6)

    """def overall_distance(self, camera):
        return sum(
            map(lambda shape: shape.overall_distance(camera), self.faces)
        ) // len(self.faces)

    def render(self, camera, surface):
        self.faces.render(camera, surface)
    """

class Chunk(Shape):
    def __init__(self, origin: D3Point, size=5, cube_size=10):
        x, y, z = origin
        shapes = []
        for i in range(size):
            for j in range(size):
                for k in range(size):
                    point = D3Point(x + i * cube_size, y + j * cube_size, z + k * cube_size)
                    shapes.append(Cube(point, cube_size))
        super().__init__(*shapes)
