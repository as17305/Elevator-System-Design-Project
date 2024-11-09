from Elevator import Elevator
from Building import Building
from Person import Person
from ElevatorLevelCalculator import ElevatorLevelCalculator, ElevatorLevelCalculationWithQueues, ElevatorLevelCalculationWithHeaps, ElevatorLevelCalculationWithHeapsV2

class ElevatorController:
    def __init__(self, building: Building, elevators: list[Elevator]):
        self.building = building
        self.listOfFloors = building.getListOfFloors()
        # self.Elevator = elevators[0]
        self.Elevators = elevators
        self.ElevatorCalculator = ElevatorLevelCalculationWithHeapsV2()
        for elev in self.Elevators:
            for i in range(len(self.listOfFloors)):
                elev.addFloor(self.listOfFloors[i])
        self.Elevator = elevators[0]

    def runSimulation(self):
        previousFloor = self.Elevator.currentFloor

        while Person.getTotalRequests() > 0:
            self.Elevator.peopleLeave()
            self.Elevator.peopleEnter(self.listOfFloors[self.Elevator.getFloor() - 1])
            floor, direction = self.ElevatorCalculator.getNextLevel(self.building, self.Elevator)
            if floor != None and direction != None:
                # It takes the Elevator 4 seconds to travel to each floor
                self.Elevator.addWaitTime(abs(floor - previousFloor) * 4)
            previousFloor = floor
            self.Elevator.setFloor(floor)
            self.Elevator.setDirection(direction) 

    def runSimulationWithMultipleElevators(self):
        # The more elevators in use, the longer it takes for program to run, but the waittime is minimized
        closestRequestToElevator = {}
        while Person.getTotalRequests() > 0:
            for i in range(len(self.building.getListOfFloors())):
                closestRequestToElevator[i] = []
            for elevator in self.Elevators:
                nextfloor, nextdirection = self.ElevatorCalculator.getNextLevel(self.building, elevator)
                if nextfloor != None:
                    distance = abs(elevator.getFloor() - nextfloor)
                    closestRequestToElevator[distance].append([elevator, nextfloor, nextdirection])
            # Find closest request to closest elevator
            for key in closestRequestToElevator:
                if closestRequestToElevator[key] != []:
                    nextRequestInfo = closestRequestToElevator[key][0]
                    break
            elevatorInUse = nextRequestInfo[0]
            floorNew = nextRequestInfo[1]
            directionNew = nextRequestInfo[2]
            if floorNew != None and directionNew != None:
                # It takes the Elevator 4 seconds to travel to each floor
                elevatorInUse.addWaitTime(abs(floorNew - elevatorInUse.getFloor()) * 4)
            elevatorInUse.setFloor(floorNew)
            elevatorInUse.setDirection(directionNew) 
            elevatorInUse.peopleLeave()
            elevatorInUse.peopleEnter(self.listOfFloors[elevatorInUse.getFloor() - 1])
            print(f"Requests Remaining: {Person.getTotalRequests()}")
