from utils import D3Point, D2Point, D3Angle
from math import cos, sin, tan, sqrt, atan, degrees, pi


S = pi / 4


class Camera:
    def __init__(self, position: D3Point, angle: D3Angle, relative: D3Point):
        self.position = position
        self.angle = angle
        self.relative = relative

    def _render_point(self, point: D3Point):
        cx, cy, cz = self.position
        ax, ay, az = point
        x, y, z = ax - cx, ay - cy, az - cz
        cosx, cosy, cosz = map(cos, self.angle)
        sinx, siny, sinz = map(sin, self.angle)

        dx = cosy * (sinz * y + cosz * x) - siny * z
        dy = sinx * (cosy * z + siny * (sinz * y + cosz * x)) + cosx * (cosz * y - sinz * x)
        dz = cosx * (cosy * z + siny * (sinz * y + cosz * x)) - sinx * (cosz * y - sinz * x)

        return (dx, dy, dz)

    def render_point(self, point: D3Point) -> D2Point:
        ex, ey, ez = self.relative
        dx, dy, dz = self._render_point(point)

        bx = (ez * dx) / dz + ex
        by = (ez * dy) / dz + ey

        return D2Point(bx, by)

    def can_render_from_distance(self, point: D3Point):
        return self.distance(point) <= 80

    def can_render(self, point: D3Point):
        x2, y2, z2 = self._render_point(point)
        if x2 < -60 or x2 > 60 or y2 < -60 or y2 > 60 or z2 < 0 or z2 > 80:
            return False
        return True

    def rotate(self, tx, ty, tz):
        self.angle.tx += tx
        self.angle.ty += ty
        self.angle.tz += tz

    def forward(self, d):
        tx, ty, tz = self.angle
        x, y, z = self.position
        dx, dy, dz = map(sin, (tx, ty, tz))
        self.position.z += d

    def distance(self, point):
        x1, y1, z1 = self.position
        x2, y2, z2 = point
        return sqrt(
            (x1 - x2) ** 2 +
            (y1 - y2) ** 2 +
            (z1 - z2) ** 2
        )

