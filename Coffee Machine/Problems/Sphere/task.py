class Sphere:
    # finish class Sphere here
    PI = 3.1415

    def __init__(self, radius):
        self.radius = radius
        vol = Sphere.PI
        self.volume = (4 / 3 * vol * radius ** 3)
