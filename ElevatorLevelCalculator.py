from Floor import Floor
from Elevator import Elevator
from Building import Building
from Person import Person
import heapq

class ElevatorLevelCalculator:
    def getNextLevel(self, building: Building, Elevator: Elevator):
        """
        Go to up each floor and down each floor until all requests are handled
        Returns None, None if there are no requests in the building
        """
        currentFloor = Elevator.getFloor()
        directionUp = Elevator.getDirection()
        if directionUp:
            if currentFloor < len(building.getListOfFloors()):
                currentFloor += 1
            else:
                currentFloor -= 1
                directionUp = False
        else:
            if currentFloor > 1:
                currentFloor -= 1
            else:
                currentFloor += 1
                directionUp = True
        # Return Nothing is there are no more requests
        if Person.getTotalRequests() == 0:
            return None, None     
        return currentFloor, directionUp
         
            
class ElevatorLevelCalculationWithQueues(ElevatorLevelCalculator):
    def getNextLevel(self, building: Building, Elevator: Elevator):
        """
        Go to floor that the first person in requested. If elevator is empty go to closet floor with request
        """
        ElevatorQueue = Elevator.getDestinationQueue()
        if not ElevatorQueue.empty():
            firstDestination = ElevatorQueue.queue[0]
            if firstDestination > Elevator.getFloor():
                return firstDestination, True
            return firstDestination, False
        else:
            return super().getNextLevel(building, Elevator)
    
class ElevatorLevelCalculationWithHeaps(ElevatorLevelCalculator):
    def getNextLevel(self, building: Building, Elevator: Elevator):
        """
        Go to floor that most people are making a request
        """
        if Person.getTotalRequests() == 0:
            return None, None
        minHeap = []
        for floor in building.getListOfFloors():
            # Use negative values becacuse it is a min heap
            peopleRequestingforFloor = len(Elevator.getPeopleByDestinationFloor()[floor.getLevel()]) * -1
            peopleRequestingforFloor -= floor.getPeopleQueueSize()
            if peopleRequestingforFloor != 0:
                heapq.heappush(minHeap, (peopleRequestingforFloor, floor.getLevel()))
        nextFloor = heapq.heappop(minHeap)[1]
        # Choose another floor if elevator is full and no one wants to get off that floor
        while nextFloor not in Elevator.getFloorsVisitedSet() and Elevator.fullElevator():
            nextFloor = heapq.heappop(minHeap)[1]
        if nextFloor > Elevator.getFloor():
            return nextFloor, True
        return nextFloor, False
    
class ElevatorLevelCalculationWithHeapsV2(ElevatorLevelCalculator):
    def getNextLevel(self, building: Building, Elevator: Elevator):
        """
        Go to closest floor with person waiting or stop at floor if Person is waiting to get off
        """
        if Person.getTotalRequests() == 0:
            return None, None
        minHeap = []
        for floor in building.getListOfFloors():
            # Use negative values becacuse it is a min heap
            closestFloor = (len(building.getListOfFloors()) - abs(Elevator.getFloor() - floor.getLevel())) * -1
            # Add to heap if someone in the elevator wants to go or somone wants to get on elevator
            if floor.getLevel() in Elevator.getFloorsVisitedSet() or floor.getPeopleQueueSize() > 0:
                heapq.heappush(minHeap, (closestFloor, floor.getLevel()))
        if len(minHeap) == 0:
            return None, True
        nextFloor = heapq.heappop(minHeap)[1]
        # Choose another floor if elevator is full and no one wants to get off that floor
        while nextFloor not in Elevator.getFloorsVisitedSet() and Elevator.fullElevator():
            nextFloor = heapq.heappop(minHeap)[1]
        if nextFloor > Elevator.getFloor():
            return nextFloor, True
        return nextFloor, False
