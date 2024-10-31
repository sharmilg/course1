#Write an Elevator class that receives the numbers of the bottom and top floors as initializer parameters.
# The elevator has methods go_to_floor, floor_up and floor_down. A new elevator is always at the bottom floor.
# If you make elevator h for example the method call h.go_to_floor(5), the method calls either the floor_up
# or floor_down methods as many times as it needs to get to the fifth floor. The methods run the elevator one
# floor up or down and tell what floor the elevator is after each move. Test the class by creating an
# elevator in the main program, tell it to move to a floor of your choice and then back to the bottom floor.

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            return "Invalid floor"

        if self.current_floor < floor:
            while self.current_floor < floor:
                self.floor_up()
        elif self.current_floor > floor:
            while self.current_floor > floor:
                self.floor_down()

        return f"You are on floor {self.current_floor}"

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("Elevator is already at the top floor")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"Elevator is now on floor {self.current_floor}")
        else:
            print("Elevator is already at the bottom floor")

h = Elevator(0, 5)
print(h.go_to_floor(5))
print(h.go_to_floor(0))

#Extend the previous program by creating a Building class. The initializer parameters for the class are the
# numbers of the bottom and top floors and the number of elevators in the building. When a building is
# created, the building creates the required number of elevators. The list of elevators is stored as a
# property of the building. Write a method called run_elevator that accepts the number of the elevator and
# the destination floor as its parameters. In the main program, write the statements for creating a new
# building and running the elevators of the building.
class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            return "Invalid floor"

        if self.current_floor < floor:
            while self.current_floor < floor:
                self.floor_up()
        elif self.current_floor > floor:
            while self.current_floor > floor:
                self.floor_down()

        return f"You are on floor {self.current_floor}"

    def floor_up(self):
        if self.current_floor < self.top_floor:
            self.current_floor += 1
            print(f"You are now on floor {self.current_floor}")
        else:
            print("You are already at the top floor")

    def floor_down(self):
        if self.current_floor > self.bottom_floor:
            self.current_floor -= 1
            print(f"You are now on floor {self.current_floor}")
        else:
            print(" You are at the bottom floor")

class Building:
    def __init__(self, bottom_floor, top_floor, number):

        self.bottom_floor = bottom_floor
        self.top_floor = top_floor

        self.elevators = [Elevator(bottom_floor, top_floor)
    for i  in range(number)]

    def run_elevator(self, elevator_number, destination_floor):

        if elevator_number < 0 or elevator_number >= len(self.elevators):
            return "Invalid number"

        elevator = self.elevators[elevator_number]
        return elevator.go_to_floor(destination_floor)


building = Building(0, 10, 3)

print(building.run_elevator(0, 5))
print(building.run_elevator(1, 8))
print(building.run_elevator(2, 3))

print(building.run_elevator(3, 4))


#Extend the program again by adding a method fire_alarm that does not receive any parameters and moves all
# elevators to the bottom floor. Continue the main program by causing a fire alarm in your building.

class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        if floor < self.bottom_floor or floor > self.top_floor:
            return "Invalid floor"
        self.current_floor = floor
        return f"Elevator is now on floor {self.current_floor}"


class Building:
    def __init__(self, num_elevators):
        # All elevators in the building go between floor 0 and floor 10
        self.elevators = [Elevator(0, 10) for _ in range(num_elevators)]

    def use_elevator(self, elevator_number, floor):
        if 0 <= elevator_number < len(self.elevators):
            return self.elevators[elevator_number].go_to_floor(floor)
        return "Invalid elevator number"

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.go_to_floor(0)
        return "All elevators moved to the ground floor"


# Example usage:
building = Building(3)

# Move elevator 1 to floor 5
print(building.use_elevator(1, 5))

# Trigger fire alarm
print(building.fire_alarm())


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
    def __init__(self, name, top_speed):
        self.name = name
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def random_speed(self):

        self.current_speed += random.randint(-10, 15)

        if self.current_speed < 0:
            self.current_speed = 0
        elif self.current_speed > self.top_speed:
            self.current_speed = self.top_speed

    def drive(self):

        self.distance_traveled += self.current_speed


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.randomize_speed()
            car.drive()

    def print_status(self):
        print("Car Name      | Top Speed | Current Speed | Distance Traveled")
        print("-" * 55)
        for car in self.cars:
            print(f"{car.name:<12} | {car.top_speed:<9} | {car.current_speed:<13} | {car.distance_traveled}")

    def race_finished(self):

        for car in self.cars:
            if car.distance_traveled >= self.distance:
                return True
        return False


def main():

    cars = []
    for i in range(10):
        car = Car("Car " + str(i + 1), random.randint(100, 200))
        cars.append(car)

    race = Race("Grand Demolition Derby", 8000, cars)

    hours_passed = 0
    while not race.race_finished():
        race.hour_passes()
        hours_passed += 1

        if hours_passed % 10 == 0:
            print(f"\nStatus after {hours_passed} hours:")
            race.print_status()

    print("\nFinal race status:")
    race.print_status()

main()
