import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, p2):
        return ((p2.x - self.x) ** 2 + (p2.y - self.y) ** 2) ** 0.5
