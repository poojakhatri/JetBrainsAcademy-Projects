class Painting:
    museum = "hangs in the Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        Painting.museum = "hangs in the Louvre."


f_name = input()
l_name = input()
year = input()
pain = Painting(f_name, l_name, year)

print(f'"{pain.title}" by {pain.artist} ({pain.year}) {Painting.museum}')
