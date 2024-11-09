from Person import Person
from Floor import Floor
import queue

class Elevator:
    counter = 0

    def __init__(self, size = 0 , currentFloor = 1, directionUp = True, maxsize = 25):
        Elevator.counter += 1
        self.elevatorNumber = Elevator.counter
        self.size = size
        self.currentFloor = currentFloor
        self.maxSize = maxsize
        self.directionUp = directionUp
        self.floorsVisited = set()
        self.destinationQueue = queue.Queue()
        self.waitTime = 0
        # {DestinationFloor: Person objects}
        self.peopleByDestinationFloor = {}

    def peopleLeave(self):
        people = self.peopleByDestinationFloor[self.currentFloor]
        # It take 3 seconds for elevator to open and for people to leave
        self.waitTime += 3
        if len(people) > 0:
            for person in people:
                self.size -= 1
                Person.removeFromTotalRequests()
                person.setEndTime(self.waitTime)
                # print(f"Dropped {person.getID()} at Floor {self.currentFloor}")
            self.destinationQueue.get()
            self.floorsVisited.remove(self.currentFloor)
            self.peopleByDestinationFloor[self.currentFloor] = []
            
    def addPerson(self, person: Person):
        self.size += 1
        if person.getDestination() not in self.floorsVisited:
            self.destinationQueue.put(person.getDestination())
            self.floorsVisited.add(person.getDestination())
        self.peopleByDestinationFloor[person.getDestination()].append(person)
        # print(f"Picked up {person.getID()} at Floor {self.currentFloor}")

    def peopleEnter(self, floor: Floor):
        people = floor.getPeople(self.maxSize - self.size)
        if len(people) != 0:
            # It take 3 seconds for people to enter
            self.waitTime += 3
            for person in people:
                self.addPerson(person)

    def setFloor(self, currentFloor):
        self.currentFloor = currentFloor

    def setDirection(self, directionUp):
        self.directionUp = directionUp

    def addFloor(self, floor):
        self.peopleByDestinationFloor[floor.getLevel()] = []

    def getDirection(self):
        return self.directionUp
    
    def getFloor(self):
        return self.currentFloor
    
    def getDestinationQueue(self):
        return self.destinationQueue
    
    def getFloorsVisitedSet(self):
        return self.floorsVisited
    
    def getPeopleByDestinationFloor(self):
        return self.peopleByDestinationFloor
    
    def fullElevator(self):
        if self.size == 25:
            return True
        return False
    
    def addWaitTime(self, time):
        self.waitTime += time