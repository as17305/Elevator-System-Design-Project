import queue
import Person

class Floor:
    level = 0

    def __init__(self):
        Floor.level += 1
        self.level = Floor.level
        self.peopleQueue = queue.Queue(maxsize = 100)

    def addPerson(self, person: Person):
        self.peopleQueue.put(person)

    def getPeople(self, numberOfPeople):
        numberAdded = 0
        peopleAdded = []
        while not(self.peopleQueue.empty()) and numberAdded < numberOfPeople:
            peopleAdded.append(self.peopleQueue.get())
            numberAdded += 1
        return peopleAdded

    def getLevel(self):
        return self.level
    
    def checkPeopleQueueEmpty(self):
        return self.peopleQueue.empty()
    
    def getPeopleQueueSize(self):
        return self.peopleQueue.qsize()
