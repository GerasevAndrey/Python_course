class Car:

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is going.')

    def stop(self):
        print(f'{self.name} is stoping.')

    def turn(self, direction):
        print(f'{self.name} is turning {direction}')

    def show_speed(self):
        print(f'Your speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'Your speed is higher than allow! Your speed is {self.speed}')
        else:
            print(f'Speed of {self.name} is normal')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'Your speed is higher than allow! Your speed is {self.speed}')
        else:
            print(f'Speed of {self.name} is normal')


class PoliceCar(Car):
    pass


town_car = TownCar('BMW', 70, 'blue', False)

sport_car = SportCar('Ferrari', 170, 'red', False)

work_car = WorkCar('KAMAZ', 30, 'red', False)

police_car = PoliceCar('Skoda', 100, 'yellow', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('left')
