import os
import json
import shutil

# database = {
#     "name" : "",
#     "creator" : "",
#     "filePath" : "",
#     "assigned" : "",
#     "producer" : "",
#     "director" : ""
# }


data = {
    "string": "some string",
    "number": 12,
    "bool": True,
    "list": [1, 2, 3],
    "object": {"name": "Paul"}
}


class DataRepository:
    def __init__(self, name, creator, filePath, databasename):
        self.name = name
        self.creator = creator
        self.filePath = filePath
        self.databasename = databasename
        
        self.createDatabase(databasename)

        #self.updateDatabase(self.name, self.creator, self.filePath)

        path=os.path.join(self.filePath) # if only 1 argument, useful for turning \ into /

        if os.path.exists(path) == True:
            print("This file path already exists")
        else:
            print("============================== Updated Directory ============================== ")
            print(f"Added directory: {path}")
            os.makedirs(path)

    def createDatabase(self, databasename):
        self.database=databasename
        print(f"============================== Database Created For {self.name}: {self.databasename} ==============================")
        self.database = {
            "name" : self.name ,
            "creator" : self.creator,
            "filePath" : self.filePath,
            "assigned" : "N/A",
            "producer" : "N/A",
            "director" : "N/A"
        }
        #print(self.database)

    def updateDatabase(self, key, value):
        print(f"**** Updated Database {self.name}: {key} : {value} ****")
        self.database.update({key : value})

    def showDatabase(self):
        print(f"============================== Showing {self.databasename} {self.name}: ==============================")
        print(self.database)

    # def updateDatabase(self, name, creator, filePath, *assigned):
    #     #super().__init__(name, creator, filePath)
    #     print("============================== Updated Database ============================== ")
    #     database.update({"name" : name, 
    #                      "creator" : creator, 
    #                      "filePath" : filePath, 
    #                      "assigned" : assigned, 
    #                      #"producer" : self.producer, 
    #                      #"director" : self.director
    #                      })
    
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
    def __init__(self, name, creator, filePath, assigned, databasename):
        super().__init__(name, creator, filePath, databasename)
        self.assigned=assigned

        #self.updateDatabase(assigned , self.assigned)        
    

    def get_basicInfo(self):
        super().get_basicInfo()
        print(f"assigned maintenance contact: {self.assigned}")



class Show(DataRepository):
    def __init__(self, name, creator, filePath, producer, director, databasename):
        super().__init__(name, creator, filePath, databasename)
        self.producer = producer
        self.director = director

        print(f"============================== Added Show: {self.name} ============================== ")

        self.updateDatabase("producer", self.producer)
        self.updateDatabase("director", self.director)

    
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