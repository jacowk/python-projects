from os import listdir
from os.path import isfile, join

class FileNamesRetriever:

    def __init__(self, path):
        self.path = path

    def retrieve(self):
        onlyfiles = [f for f in listdir(self.path) if isfile(join(self.path, f))]
        return onlyfiles

#filename = "/home/jaco/python-data/datasets/climate_data/GlobalLandTemperaturesByCity/"
filename = "/home/jaco/python-data/datasets/climate_data/test/"
fn = FileNamesRetriever(filename)
files = fn.retrieve()
print(files)