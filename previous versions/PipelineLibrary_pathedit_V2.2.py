import os
import json
import shutil

data = {
    "string": "some string",
    "number": 12,
    "bool": True,
    "list": [1, 2, 3],
    "object": {"name": "Paul"}
}


class DataRepository:
    def __init__(self, name, creator, filePath):
        self.name = name
        self.creator = creator
        self.filePath = filePath

        path=os.path.join(self.filePath) # if only 1 argument, useful for turning \ into /

        if os.path.exists(path) == True:
            print("This file path already exists")
        else:
            print("============================== Updated Directory ============================== ")
            print(f"Added directory: {path}")
            os.makedirs(path)
    
    def get_basicInfo(self):
        print(f"============================== Basic Info: {self.name} ==============================")
        print(f"title: {self.name}")
        print(f"creator: {self.creator}")

    #def makeFilePath(self, contentName, *args):
        #path=os.path.join(self.filePath, contentName, "/".join(args))
        #return path

    def makePath(self,*pathargs):
       path=os.path.join(self.filePath, "/".join(pathargs))
       return path

    def add_content(self, *args):
        print(f"============================== Added: {self.name} ============================== ")
        newpath=self.makePath(*args)

        if os.path.exists(newpath) == True:
            print("This file path already exists")
        else:
            print(f"Added show: {newpath}")
            os.makedirs(newpath)


    def get_content(self, *args):
        print(f"============================== Content: {self.name} ==============================")
        newpath=self.makePath(*args)

        #newpath=os.path.join(self.filePath, "/".join(args))
        contents=os.listdir(newpath)
        print(f"Contents of {newpath}: \n {contents}")

    def add_file(self, *args):
        print(f"============================== Updated: {self.name} ============================== ")
        newpath=self.makePath(*args)
        with open(newpath,'w') as file:
            json.dump(data, file, indent=4)
        print(f"added a file at {newpath}")

    def remove_file(self,*args):
        print(f"============================== Updated: {self.name} ============================== ")
        newpath=self.makePath(*args)
        if os.path.exists(newpath):
            os.remove(newpath)
            print(f"{newpath} was removed")
        else:
            print("File does not exist.")
    
    def remove_folder(self, *args):
        print(f"============================== Updated: {self.name} ============================== ")
        newpath=self.makePath(*args)
        #path=os.path.join(self.filePath, "/".join(args))
        shutil.rmtree(newpath)    
        print(f"removed a directory and its contents at {newpath}")

        

class DirectoryOfShows(DataRepository):
    def __init__(self, name, creator, filePath, assigned):
        super().__init__(name, creator, filePath)
        self.assigned=assigned
        

    def get_basicInfo(self):
        super().get_basicInfo()
        print(f"assigned maintenance contact: {self.assigned}")



class Show(DataRepository):
    def __init__(self, name, creator, filePath, producer, director):
        super().__init__(name, creator, filePath)
        self.producer = producer
        self.director = director

        #print(f"============================== Added Show: {self.name} ============================== ")

    
    # def get_shotList(self):
    #     print(self.contentList)

    def get_basicInfo(self):
        super().get_basicInfo()
        print(f"producer: {self.producer}")
        print(f"director: {self.director}")

class Shot(DataRepository):
    def __init__(self, name, creator, filePath, shotNumber):
        super().__init__(name, creator, filePath)
        self.shotNumber = shotNumber

    def get_basicInfo(self):
        super().get_basicInfo()
        print(f"Shot Number: {self.shotNumber}")

    
#myDir=DirectoryOfShows("Directory1", "Me","C:/Users/jpark/Desktop/TestDirectory/content1")
myDir=DirectoryOfShows("Directory1", "Me",r"C:\Users\jpark\Desktop\TestDirectory", "someone else")
#print("============================== first report ============================== ")
myDir.get_basicInfo()

#print("============================== Add Show ============================== ")

FirstShow=Show("Show1","me", r"C:\Users\jpark\Desktop\TestDirectory\Show1", "Producer1", "Director1")
SecondShow=Show("Show2","me", r"C:\Users\jpark\Desktop\TestDirectory\Show2", "Producer2", "Director2")

#print("============================== second report ==============================")
myDir.get_content()

FirstShow.get_basicInfo()
FirstShow.get_content()

#print("============================== Add Shot ============================== ")
ShotA=Shot("Test Shot", "me", r"C:\Users\jpark\Desktop\TestDirectory\Show1\Test Shot", "0001")


#print("============================== third report ==============================")
#print("eeeeeeeeeeeeeeeeeeeeee")
FirstShow.get_basicInfo()
FirstShow.get_content()
#print("eeeeeeeeeeeeeeeeeeeeee")
ShotA.get_basicInfo()
ShotA.get_content()
#print("eeeeeeeeeeeeeeeeeeeeee")


ShotA.add_file("File A")
ShotA.add_file("File B")

ShotA.get_content()
#ShotA.remove_file("File A")
#SecondShow.remove_folder()


