#BuildCityData (Loop through rows and built result_dict)

import csv
import utils as u

class BuildCityData:

    def __init__(self, filename, month):
        self.filename = filename
        self.month = month
        self.result_dict = dict()

    def build_data(self):
        cnt = 1
        with open(self.filename, newline='') as csvfile:
            datareader = csv.reader(csvfile, delimiter=',')

            for row in datareader:
                if cnt == 1:
                    cnt += 1
                    continue  # Skip first line with only column names

                #print(row)

                if len(row[1]) > 0:
                    self.Date = u.format_date(row[0])
                    self.AverageTemperature = u.scrub_decimal(row[1])

                    # Build dictionary for the selected month
                    if u.is_month(self.Date, self.month):
                        self.result_dict[self.Date] = round(self.AverageTemperature, 2)
                        cnt += 1
        return self.result_dict
