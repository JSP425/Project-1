import PipelineLibrary_V1 as db
import os
import shutil
import json

targetDirectory="C:/Users/jpark/Desktop/TestDirectory"
targetShow="C:/Users/jpark/Desktop/TestDirectory/Show1"
targetShot="C:/Users/jpark/Desktop/TestDirectory/Show1/Shot0001"
targetDB="C:/Users/jpark/Desktop/TestDirectory/Show1/Shot0001/Shot1 DB"


tempDir=db.DirectoryOfShows(targetDirectory, "Assignee", "Directory1", "Creator1000", "Directory1 DB")
tempShow=db.Show(targetShow, "Producer99", "Director99", "Show1", "Creator99", "Show1 DB")
tempShot=db.Shot(targetShot, 1, 23.97, 1, 40, "testshot", "ArtistName", "Shot1 DB") 


def test_directoryPath():
    
    assert os.path.exists(targetDirectory) == True

def test_write_database():

    assert os.path.isfile(targetDirectory+"/Directory1 DB")


def test_updateDatabase():
    tempDM1=db.DataManager(targetDirectory)
    tempDM1.updateDatabase("Shot1 DB", "assigned animators", ["Artist 1", "Artist 2", "Artist 3"])

    with open(targetDB,'r') as file:
        data = json.load(file)
        data['assigned animators'] = ["Artist 1", "Artist 2", "Artist 3"]

    assert data['assigned animators'] == ["Artist 1", "Artist 2", "Artist 3"]

def test_add_content():
    tempShot.add_content(targetShot+"/MayaFiles")
    assert os.path.exists("C:/Users/jpark/Desktop/TestDirectory/Show1/Shot0001/MayaFiles") == True

def test_moveFile():

    tempShow.move_file(targetShow+"/Show1 DB", targetDirectory)

    assert os.path.exists(targetDirectory+"/Show1 DB")

def test_remove_file():

    tempDM=db.DataManager(targetDirectory)
    tempDM.remove_file(targetDirectory+"/Show1 DB")

    assert os.path.exists(targetDirectory+"/Show1 DB") == False


def test_remove_folder():

    tempDir.remove_folder(targetDirectory)

    assert os.path.exists(targetDirectory) == False, f"{targetDirectory} <-- still exists"



    