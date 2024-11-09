from Floor import Floor

class Building:
    def __init__(self, floors = list[Floor]):
        self.listOfFloors = floors
    
    def getListOfFloors(self):
        return self.listOfFloors