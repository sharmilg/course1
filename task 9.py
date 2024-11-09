#Write a Car class that has the following properties: registration number, maximum speed, current speed and
# travelled distance. Add a class initializer that sets the first two of the properties based on parameter values.
# The current speed and travelled distance of a new car must be automatically set to zero. Write a main program
# where you create a new car (registration number ABC-123, maximum speed 142 km/h). Finally, print out all the
# properties of the new car.

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, target_floor):
        if target_floor > self.current_floor:
            while self.current_floor < target_floor:
                self.floor_up()
        elif target_floor < self.current_floor:
            while self.current_floor > target_floor:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator {self.current_floor} up")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator {self.current_floor} down")

# main program
elevator = Elevator(1, 7)
elevator.go_to_floor(7)
elevator.go_to_floor(5)

class Car:
    count = 0

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        Car.count += 1

    def __str__(self):
        return f'{self.registration_number},{self.maximum_speed},{self.current_speed},{self.travelled_distance}'

    # Getter and setter to manipulate data:
    def get_registration_number(self):
        return self.registration_number

    def get_maximum_speed(self):
        return self.maximum_speed

    def set_maximum_speed(self, maximum_speed):
        self.maximum_speed = maximum_speed

    def set_registration_number(self, registration_number):
        self.registration_number = registration_number

New_car = Car("ABC-123", 142)

print(f"Registration number: {New_car.registration_number}, Maximum speed: {New_car.maximum_speed},"
      f" Travelled distance: {New_car.travelled_distance}, Current speed: {New_car.current_speed}")



#Extend the program by adding an accelerate method into the new class. The method should receive the change of speed
# (km/h) as a parameter. If the change is negative, the car reduces speed. The method must change the value of the
# speed property of the object. The speed of the car must stay below the set maximum and cannot be less than zero.
# Extend the main program so that the speed of the car is first increased by +30 km/h, then +70 km/h and finally +50
# km/h. Then print out the current speed of the car. Finally, use the emergency brake by forcing a -200 km/h change
# on the speed and then print out the final speed. The  travelled distance does not have to be updated yet.

class Car:
    count = 0

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        Car.count += 1

    def __str__(self):
        return f'{self.registration_number},{self.maximum_speed},{self.current_speed},{self.travelled_distance}'

    # Getter and setter to manipulate data:
    def get_registration_number(self):
        return self.registration_number

    def get_maximum_speed(self):
        return self.maximum_speed

    def set_maximum_speed(self, maximum_speed):
        self.maximum_speed = maximum_speed

    def set_registration_number(self, registration_number):
        self.registration_number = registration_number
#Adding an Accelerating method:
    def accelerate(self,speed):
        self.current_speed += speed

        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0
New_car = Car("ABC-123", 142)

print(New_car)
New_car.accelerate(30)
New_car.accelerate(70)
New_car.accelerate(50)
print(f"The current speed is {New_car.current_speed}km/h")
New_car.accelerate(-200)
print(f"Final speed after emergency break is {New_car.current_speed}km/h")

print(f"Registration number: {New_car.registration_number}, Maximum speed: {New_car.maximum_speed},"
      f" Travelled distance: {New_car.travelled_distance}, Current speed: {New_car.current_speed}")
#Again, extend the program by adding a new drive method that receives the number of hours as a parameter. The method
# increases the travelled distance by how much the car has travelled in constant speed in the given time. Example:
# The travelled distance of car object is 2000 km. The current speed is 60 km/h. Method call car.drive(1.5)
# increases the travelled distance to 2090 km.
class Car:
    count = 0

    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
        Car.count += 1

    def __str__(self):
        return f'{self.registration_number}, {self.maximum_speed}, {self.current_speed}, {self.travelled_distance}'

    # Getter and setter to manipulate data:
    def get_registration_number(self):
        return self.registration_number

    def get_maximum_speed(self):
        return self.maximum_speed

    def set_maximum_speed(self, maximum_speed):
        self.maximum_speed = maximum_speed

    def set_registration_number(self, registration_number):
        self.registration_number = registration_number

# Adding new drive method:
    def drive(self, number_of_hours):
        self.travelled_distance += self.current_speed * number_of_hours


New_car = Car("ABC-123", 142)
New_car.drive(1.5)
print(f"The travelled distance after driving 1.5 hours is: {New_car.travelled_distance} km")

#The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
# This is done using the accerelate method. Each car is made to drive for one hour. This is done with the drive
# method. The race continues until one of the cars has advanced at least 10,000 kilometers. Finally, the properties
#of each car are printed out formatted into a clear table.
import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return f'{self.registration_number}, {self.maximum_speed}, {self.current_speed}, {self.travelled_distance}'

    def get_registration_number(self):
        return self.registration_number

    def get_maximum_speed(self):
        return self.maximum_speed

    def set_maximum_speed(self, maximum_speed):
        self.maximum_speed = maximum_speed

    def set_registration_number(self, registration_number):
        self.registration_number = registration_number

    def accelerate(self, speed):
        self.current_speed += speed
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, number_of_hours):
        self.travelled_distance += self.current_speed * number_of_hours


cars = []
for i in range(1, 11):
    registration_number = f"ABC-{i}"
    maximum_speed = random.randint(100, 200)
    cars.append(Car(registration_number, maximum_speed))

race_finished = False
while not race_finished:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_finished = True
            break

# Printing out the properties of each car formatted into a clear table
print(f'{"Registration":>12} {"Max Speed (km/h)":>15} {"Current Speed (km/h)":>20} {"Travelled Distance (km)":>25}')
for car in cars:
    print(f'{car.registration_number:>12} {car.maximum_speed:>15} {car.current_speed:>20} {car.travelled_distance:>25}')

