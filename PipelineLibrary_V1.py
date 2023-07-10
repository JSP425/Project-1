import os

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
        #print(self.filePath)
        #contents=os.listdir(self.filePath)
        #print(contents)

    def add_content(self, contentName):
        #self.contentList.append(content)
        #print(f"Add: folder name is {folderName} and file path is {filePath}")
        #function for creating folder

        path=os.path.join(self.filePath, contentName)

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

class DirectoryOfShows(DataRepository):
    def __init__(self, name, creator, filePath):
        super().__init__(name, creator, filePath)
        #self.something = something
    
    def get_creator(self):
        print(f"The creator of {self.name} is {self.creator}")

    def get_basicInfo(self):
        super().get_basicInfo()
        #print(self.filePath)
        contents=os.listdir(self.filePath)
        #print(contents)
        print(f"Contents of {self.filePath}: \n {contents}")


class Show(DataRepository):
    def __init__(self, name, contentList, producer):
        super().__init__(name, contentList)
        self.producer = producer

    def get_producer(self):
        print(f"The producer of {self.name} is {self.producer}")
    
    def get_shotList(self):
        print(self.contentList)

    def get_basicInfo(self):
        super().get_basicInfo()
        print(f"producer: {self.producer}")
    


#myDir=DirectoryOfShows("Directory1", "Me","C:/Users/jpark/Desktop/TestDirectory/content1")
myDir=DirectoryOfShows("Directory1", "Me",r"C:\Users\jpark\Desktop\TestDirectory")
print("===============initial report===============")
myDir.get_basicInfo()

print("===============Add Show===============")
myDir.add_content("Show1")
myDir.add_content("Show2")
myDir.get_basicInfo()