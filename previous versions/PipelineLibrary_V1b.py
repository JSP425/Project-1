class DataRepository:
    def __init__(self, name, contentList):
        self.name = name
        self.contentList= contentList
    
    def get_basicInfo(self):
        print(f"title: {self.name}")
        print(f"content list: {self.contentList}")

    def add_content(self, content, folderName, filePath):
        self.contentList.append(content)
        print(f"Add: folder name is {folderName} and file path is {filePath}")
        #function for creating folder

    def remove_content(self, content, folderName, filePath):
        self.contentList.remove(content)
        print(f"Delete: folder name is {folderName} and located at {filePath}")

class DirectoryOfShows(DataRepository):
    def __init__(self, name, contentList, creator):
        super().__init__(name, contentList)
        self.creator = creator
    
    def get_creator(self):
        print(f"The creator of {self.name} is {self.creator}")

    def get_basicInfo(self):
        super().get_basicInfo()
        print(f"creator: {self.creator}")


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
    


myDir=DirectoryOfShows("firstDirectory",["Breaking Bad","GoT","Top Gear"],"Me")
myShow=Show("ProjectShow1", ["file1", "file2", "file3", "file4"], "BigShotProducer")

print("===============Directory Data============================")
myDir.get_basicInfo()
print("===============Add Show============================")
myDir.add_content("South Park","South Park Folder","C:/user/stuff/stuff")
myDir.get_basicInfo()
print("===============Remove Show============================")
myDir.remove_content("GoT","GoT Folder","C:/user/stuff/stuff")
myDir.get_basicInfo()

print(" ******************************************************************************************************************** ")

print("===============Show Data============================")
myShow.get_basicInfo()
print("===============Add File============================")
myShow.add_content("file5", "File5.mb", "C:/user/stuff/morestuff")
myShow.get_basicInfo()
print("===============Remove File============================")
myShow.remove_content("file3", "File3.mb", "C:/user/stuff/morestuff")
myShow.get_basicInfo()