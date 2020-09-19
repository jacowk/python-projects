import bs4
import os

class ScrapMeasures:

    def __init__(self, filename):
        self.filename = filename

    def scrap(self):
        print("Parsing {}".format(self.filename))
        print(os.getcwd())
        file = open(self.filename, "r")
        soup = bs4.BeautifulSoup(file, 'html.parser')
        return soup

