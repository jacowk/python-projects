import csv

filename = "/home/jaco/python-data/datasets/climate_data/GlobalLandTemperaturesByCity.csv"

#['Date', 'AverageTemperature', 'AverageTemperatureUncertainty', 'City', 'Country', 'Latitude', 'Longitude']
#['1743-11-01', '6.068', '1.7369999999999999', 'Århus', 'Denmark', '57.05N', '10.33E']

# Import csv
with open(filename, newline = '') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    cnt = 1

    values_string = ""
    for row in datareader:
        #if cnt == 1:
        #    cnt += 1
        #    continue #Skip first line with only column names

        print(row)

        cnt += 1

        key = input("Press any key to continue, or 'q' to quite...")
        if key == 'q':
            break
