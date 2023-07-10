
class DirectoryOfShows:
    def __init__(self, name, listOfShows):
        self.name = name
        self.listOfShows=listOfShows
    
    def get_listOfShows(self):
        return self.listOfShows

    def addShow(self, show):
        self.listOfShows.append(show)

    def removeShow(self, show):
        self.listOfShows.remove(show)

class Show:
    def __init__(self, name, listofShots, dataList):
        self.name = name
        self.listofShots=listofShots
        self.dataList=dataList
    
    def get_listOfShots(self):
        return self.listofShots
        


myDirectory=DirectoryOfShows("testDirectory",["spongebob","sailor moon"])
print(myDirectory.get_listOfShows())

myDirectory.addShow("Top Gear")
print(myDirectory.get_listOfShows())

myDirectory.removeShow("sailor moon")
print(myDirectory.get_listOfShows())