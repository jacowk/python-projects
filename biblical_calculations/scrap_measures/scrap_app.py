import scrap_measures.scrap as s
import scrap_measures.scrap_lengths as sl

class ScrapApp:

    def scrap(self):
        filename = "measures.htm"
        scrap = s.ScrapMeasures(filename)
        soup = scrap.scrap()

        #Scrape the Lengths
        scrap_lengths = sl.ScrapLengths(soup)
        scrap_lengths.scrap()

scrap_app = ScrapApp()
scrap_app.scrap()


