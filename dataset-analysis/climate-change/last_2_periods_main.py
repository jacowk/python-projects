import last_2_periods.build_city_data as bcd
import last_2_periods.page_builder as pb
import last_2_periods.average_calculator as ac
import last_2_periods.period_analyzer as pa
import last_2_periods.file_names_retriever as fnr
import utils as u

print("Started")

# Prepare parameters
filename = "/home/jaco/python-data/datasets/climate_data/GlobalLandTemperaturesByCity/Accra.csv"
#filepath = "/home/jaco/python-data/datasets/climate_data/test/"
filepath = "/home/jaco/python-data/datasets/climate_data/GlobalLandTemperaturesByCity/"
month = "03"
no_years = 70

class LastTwoPeriods:

    def __init__(self, month, no_years):
        self.month = month
        self.no_years = no_years

    def execute_one(self, filename):
        #Retrieve the data
        build_city_data = bcd.BuildCityData(filename, self.month)
        result_dict = build_city_data.build_data()

        #Build page list
        page_builder = pb.PageBuilder(result_dict, self.no_years)
        page_list = page_builder.build()

        #Calculate averages
        average_calculator = ac.AverageCalculator(page_list)
        average_dict = average_calculator.calculate()

        #Analyze Data
        period_analyzer = pa.PeriodAnalyzer(average_dict, u.get_filename(filename))
        period_analyzer.analyze()

    def execute_all(self, filepath):
        total_up = 0
        total_down = 0
        total_none = 0
        #Retrieve filenames
        filenames_retriever = fnr.FileNamesRetriever(filepath)
        filenames = filenames_retriever.retrieve()
        for filename in filenames:
            fullname = "{}{}".format(filepath, filename)

            #Retrieve the data
            build_city_data = bcd.BuildCityData(fullname, self.month)
            result_dict = build_city_data.build_data()

            #Build page list
            page_builder = pb.PageBuilder(result_dict, self.no_years)
            page_list = page_builder.build()

            #Calculate averages
            average_calculator = ac.AverageCalculator(page_list)
            average_dict = average_calculator.calculate()

            #Analyze Data
            period_analyzer = pa.PeriodAnalyzer(average_dict, u.get_filename(filename))
            result = period_analyzer.analyze()

            if result == "up":
                total_up += 1
            elif result == "down":
                total_down += 1
            else:
                total_none += 1

        print("Total Up: {}".format(total_up))
        print("Total Down: {}".format(total_down))
        print("Total None: {}".format(total_none))

#last_two_periods = LastTwoPeriods(month, no_years)
#last_two_periods.execute_one(filename)

months = { '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12' }
for month_x in sorted(months):
    print("\nMonth: {}".format(month_x))
    last_two_periods = LastTwoPeriods(month_x, no_years)
    last_two_periods.execute_all(filepath)
