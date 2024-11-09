class Person:
    counter = 0
    totalRequests = 0

    def __init__(self, currentFloor, destinationFloor):
        Person.counter += 1
        Person.totalRequests += 1
        self.id = Person.counter
        self.currentFloor = currentFloor
        self.destinationFloor = destinationFloor
        self.endTime = 0
    
    def getID(self):
        return self.id
    
    def getDestination(self):
        return self.destinationFloor
   
    def getCurrentFloor(self):
        return self.currentFloor
    
    def setEndTime(self, time):
        self.endTime = time
    
    def getWaitTime(self):
        return self.endTime
    
    @staticmethod
    def removeFromTotalRequests():
        Person.totalRequests -= 1

    @staticmethod
    def getTotalRequests():
        return Person.totalRequests