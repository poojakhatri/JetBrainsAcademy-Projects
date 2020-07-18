class Mountain:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    # create convert_height here
    def convert_height(self):
        Meter = self.height
        Foot = Meter/0.3048
        return Foot
