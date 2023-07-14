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
            print(f"Added directory: {path}")
            os.makedirs(path)
    
    def get_basicInfo(self):
        print(f"title: {self.name}")
        print(f"creator: {self.creator}")


    def add_content(self, contentName, *args):
        #self.contentList.append(content)
        #print(f"Add: folder name is {folderName} and file path is {filePath}")
        #function for creating folder

        path=os.path.join(self.filePath, contentName, "/".join(args))

        if os.path.exists(path) == True:
            print("This file path already exists")
        else:
            print(f"Added show: {path}")
            os.makedirs(path)

    def remove_content(self, content, folderName, filePath):
        self.contentList.remove(content)
        print(f"Delete: folder name is {folderName} and located at {filePath}")

        path=filePath
        #os.remove(filePath) #[WinError 5] Access is denied: 'C:/Users/jpark/Desktop/TestBox2/SubTest2'
        #shutil.rmtree() # deletes entire directory? including everything on desktop?

    def get_content(self,*args):
        path=os.path.join(self.filePath, "/".join(args))
        contents=os.listdir(path)
        print(f"Contents of {path}: \n {contents}")

    def add_file(self, *args):
        path=os.path.join(self.filePath, "/".join(args))
        with open(path,'w') as file:
            json.dump(data, file, indent=4)
        print(f"added a file at {path}")

    def remove_file(self,*args):
        path=os.path.join(self.filePath, "/".join(args))
        if os.path.exists(path):
            os.remove(path)
            print(f"{path} was removed")
        else:
            print("File does not exist.")
    
    def remove_folder(self, *args):
        path=os.path.join(self.filePath, "/".join(args))
        shutil.rmtree(path)    
        print(f"removed a directory and its contents at {path}")

        

class DirectoryOfShows(DataRepository):
    def __init__(self, name, creator, filePath, assigned):
        super().__init__(name, creator, filePath)
        self.assigned=assigned


    def get_basicInfo(self):
        super().get_basicInfo()
        print(f"assigned maintenance contact: {self.assigned}")



class Show(DataRepository):
    def __init__(self, name, contentList, producer):
        super().__init__(name, contentList)
        self.producer = producer

    
    def get_shotList(self):
        print(self.contentList)

    def get_basicInfo(self):
        super().get_basicInfo()
        print(f"producer: {self.producer}")
    

    
#myDir=DirectoryOfShows("Directory1", "Me","C:/Users/jpark/Desktop/TestDirectory/content1")
myDir=DirectoryOfShows("Directory1", "Me",r"C:\Users\jpark\Desktop\TestDirectory", "someone else")
print("============================== first report ============================== ")
myDir.get_basicInfo()

print("============================== Add Show ============================== ")
myDir.add_content("Show1")
myDir.add_content("Show2")

print("============================== second report ==============================")
myDir.get_basicInfo()
myDir.get_content()

print("============================== Add Shot ============================== ")
myDir.add_content("Show2","Shot1")
myDir.add_content("Show2","Shot2")

print("============================== third report ==============================")
myDir.get_basicInfo()
myDir.get_content("Show2")


print("============================== Add File ============================== ")
myDir.add_file("Show2", "Shot2","myFirstFile")
myDir.add_file("Show2", "Shot2","mySecondFile")
#myDir.remove_file("Show2", "Shot2","myFirstFile")
myDir.remove_folder("Show2", "Shot2")

print("============================== third report ==============================")
myDir.get_basicInfo()
myDir.get_content("Show2")
