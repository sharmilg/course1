# Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
# The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor.
# If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up
# or floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one
# floor up or down and tell what floor the elevator is after each move. Test the class by creating an
# elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.

#defiing class:
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor > self.current_floor:
            while self.current_floor < floor:
                self.floor_up()
        elif floor < self.current_floor:
            while self.current_floor > floor:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now going to floor {self.current_floor} up")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now going to floor {self.current_floor} down")
#Testing the values
elevator = Elevator(0, 5)
elevator.go_to_floor(5)
elevator.go_to_floor(0)

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [
            Elevator(bottom_floor, top_floor)
            for i in range(num_elevators)
        ]

# Extend the previous program by creating a Building class. The initializer parameters for the class are the
# numbers of the bottom and top floors and the number of elevators in the building. When a building is
# created, the building creates the required number of elevators. The list of elevators is stored as a
# property of the building. Write a method called run_elevator that accepts the number of the elevator and
# the destination floor as its parameters. In the main program, write the statements for creating a new
# building and running the elevators of the building.
#defining class
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor > self.current_floor:
            while self.current_floor < floor:
                self.floor_up()
        elif floor < self.current_floor:
            while self.current_floor > floor:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now going to floor {self.current_floor} up ")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now going to floor {self.current_floor} down ")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for i in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            if self.bottom_floor <= destination_floor <= self.top_floor:
                print(f"Running elevator {elevator_number + 1} to floor {destination_floor}.")
                self.elevators[elevator_number].go_to_floor(destination_floor)

            else:
                print(f"Error: Elevator {elevator_number + 1} does not exist.")

building = Building(1, 10, 3)
building.run_elevator(0, 8)
building.run_elevator(2, 3)
building.run_elevator(1, 12)


# Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all
# elevators to the bottom floor. Continue the main program by causing a fire alarm in your building.

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor > self.current_floor:
            while self.current_floor < floor:
                self.floor_up()
        elif floor < self.current_floor:
            while self.current_floor > floor:
                self.floor_down()

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now going to floor {self.current_floor} up ")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now going to floor {self.current_floor} down ")

class Building:
    def __init__(self, bottom_floor, top_floor, num_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevators = [Elevator(bottom_floor, top_floor) for i in range(num_elevators)]

    def run_elevator(self, elevator_number, destination_floor):
        if 0 <= elevator_number < len(self.elevators):
            if self.bottom_floor <= destination_floor <= self.top_floor:
                print(f"Running elevator {elevator_number + 1} to floor {destination_floor}.")
                self.elevators[elevator_number].go_to_floor(destination_floor)

            else:
                print(f"Error: Elevator {elevator_number + 1} does not exist.")

    def fire_alarm(self):

        print("Fire alarm activated! Moving all elevators to the bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"Moving elevator {i + 1} to the bottom floor.")
            elevator.go_to_floor(self.bottom_floor)


building = Building(1, 10, 3)

building.run_elevator(0, 5)
building.run_elevator(1, 8)
building.run_elevator(2, 3)
building.run_elevator(1, 12)

building.fire_alarm()

#This exercise continues the previous car race exercise from the last exercise set. Write a Race class that
# has the following properties: name, distance in kilometers and a list of cars participating in the race.
# The class has an initializer that receives the name, kilometers, and car list as parameters and sets their
# values to the corresponding properties in the class. The class has the following methods:
#hour_passes, which performs the operations done once per hour in the original exercise: generates a random
# change of speed for each car and calls their drive method.
#print_status, which prints out the current information of each car as a clear, formatted table.
#race_finished, which returns True if any of the cars has reached the finish line, meaning that they have
# driven the entire distance of the race.
#Write a main program that creates an 8000-kilometer race called Grand Demolition Derby. The new race is
# given a list of ten cars similarly to the earlier exercise. The main program simulates the progressing of
# the race by calling the hour_passes in a loop, after which it uses the race_finished method to check if
# the race has finished. The current status is printed out using the print_status method every ten hours
# and then once more at the end of the race.
import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def __str__(self):
        return f"{self.registration_number}, Max Speed: {self.maximum_speed} km/h, Current Speed: {self.current_speed} km/h, Distance: {self.travelled_distance} km"

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def drive(self, number_of_hours):
        self.travelled_distance += self.current_speed * number_of_hours

class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.accelerate(speed_change)
            car.drive(1) # drive for 1 hour

    def print_status(self):
        print(f"{'Car':<10} {'Max Speed (km/h)':<15} {'Current Speed (km/h)':<20} {'Distance (km)':<15}")
        print("-" * 60)
        for car in self.cars:
            print(f"{car.registration_number:<10} {car.maximum_speed:<15} {car.current_speed:<20} {car.travelled_distance:<15}")
        print()

    def race_finished(self):

        return any(car.travelled_distance >= self.distance for car in self.cars)

cars = [Car(f"ABC-{i+1}", random.randint(100, 200)) for i in range(1, 11)]
race = Race("Grand Demolition Derby", 8000, cars)
hours_passed = 0
while not race.race_finished():
    race.hour_passes()
    hours_passed += 1
    if hours_passed % 10 == 0:
        print(f"\n Status at Hour {hours_passed}")
        race.print_status()

print(f"\n Final Status after {hours_passed} hours")
race.print_status()
