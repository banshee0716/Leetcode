class Vector2D:
    def __init__(self, v: List[List[int]]):
        self.v = [i for row in reversed(v) for i in reversed(row)]

    def next(self) -> int:
        return self.v.pop()

    def hasNext(self) -> bool:
        return self.v
