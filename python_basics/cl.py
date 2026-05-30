class car:
    max_speed = 120
    def __init__(self, make,model,color,speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed
    def accelerate(self, acceleration):
        if self.speed + acceleration <=car.max_speed:
            self.speed += acceleration
        else:
            print(f'cannot accelerate by {acceleration}')
            self.speed = car.max_speed
    def get_speed(self):
        return self.speed
# my_car = car('Toyota', 'Camry', 'Red')
# print(f'My car is a {my_car.color} {my_car.make} {my_car.model} with a current speed of {my_car.get_speed()} km/h.')
# my_car.accelerate(50)
# print(f'After accelerating, my car speed is {my_car.get_speed()} km/h.')
# my_car.accelerate(80)
# print(f'After accelerating again, my car speed is {my_car.get_speed()} km/h.')
toyota_car=car('Toyota','Camry','Red')
toyota_car.accelerate(90)
honda_car=car('Honda','Exter','Green')
honda_car.accelerate(80)
honda_car.accelerate(80)
honda_car.accelerate(80)
honda_car.accelerate(80)
print(f'{toyota_car.color} {toyota_car.make} {toyota_car.model} is moving with {toyota_car.get_speed()} KM/hr')
print(f'{honda_car.color} {honda_car.make} {honda_car.model} is moving with {honda_car.get_speed()} KM/hr')