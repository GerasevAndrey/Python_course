class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calculate_mass(self):
        mass = self._length * self._width * 25 * 5 / 1000
        return mass


my_road = Road(20, 5000)
print(my_road.calculate_mass(), 'Т')
