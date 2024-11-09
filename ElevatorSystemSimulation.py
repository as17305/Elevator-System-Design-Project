from Person import Person
from Elevator import Elevator
from Floor import Floor
from Building import Building
from ElevatorController import ElevatorController
import random

def createfile(numberOfFloors, numberOfElevators, numberOfRequests, filename):
    L = [str(numberOfFloors), str(numberOfElevators)]
    for i in range(numberOfRequests):
        current = random.randint(1, numberOfFloors)
        destination = random.randint(1, numberOfFloors)
        while current == destination:
            destination = random.randint(1, numberOfFloors)
        L.append(f"{current} {destination}")
    file = open(filename, 'w')
    for line in L:
        file.write(line + "\n")
    file.close()

def run(filename):
    # read file
    file = open(filename, 'r')
    listOfLines = []
    while True:
        line = file.readline()
        if not line:
            break
        listOfLines.append(line.strip())
    floors = []
    people = []
    elevators = []
    numberOfFloors = int(listOfLines[0])
    numberOfElevators = int(listOfLines[1])
    print(f"There are {numberOfFloors} floors in the building.")
    print(f"There are {numberOfElevators} elevator in the building.")
    floorToPerson = {}
    for i in range(1, numberOfFloors + 1):
        floorToPerson[i] = []
    for i in range(2, len(listOfLines)):
        requestInfo = listOfLines[i].split(" ")
        current = int(requestInfo[0])
        destination = int(requestInfo[1])
        person = Person(current, destination)
        floorToPerson[current].append(person)
        people.append(person)
    for i in range(1, numberOfFloors + 1):
        floor = Floor()
        for person in floorToPerson[i]:
            floor.addPerson(person)
        floors.append(floor)
    b1 = Building(floors)
    for i in range(numberOfElevators):
        e = Elevator()
        elevators.append(e)
    contr = ElevatorController(b1, elevators)
    contr.runSimulationWithMultipleElevators()
    # Get Wait Time
    total = 0
    for person in people:
        print(f"Person {person.getID()} took {person.getWaitTime()} seconds to travel from Floor {person.getCurrentFloor()} to Floor {person.getDestination()}.")
        total += person.getWaitTime()
    print(f"The average wait time was {total // len(people)} seconds.")


# createfile(10, 1, 40, "smallInput1.txt")
# createfile(10, 3, 40, "smallInput2.txt")
# createfile(1000, 1, 5000, "largeInput1.txt")
# createfile(1000, 5, 5000, "largeInput2.txt")
run("largeInput2.txt")
