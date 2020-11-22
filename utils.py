__all__ = (
    "D3Point",
    "D2Point",
    "D3Angle"
)


class D3Point:
    __slots__ = ("x", "y", "z")
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.z})"



class D2Point:
    __slots__ = ("x", "y")
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getitem__(self, key):
        return (self.x, self.y)[key]

    def __iter__(self):
        return iter((self.x, self.y))

    def __repr__(self):
        return f"({self.x}, {self.y})"



class D3Angle:
    __slots__ = ("tx", "ty", "tz")
    def __init__(self, tx, ty, tz):
        self.tx = tx
        self.ty = ty
        self.tz = tz

    def __iter__(self):
        return iter((self.tx, self.ty, self.tz))

    def __repr__(self):
        return f"({self.tx}, {self.ty}, {self.tz})"