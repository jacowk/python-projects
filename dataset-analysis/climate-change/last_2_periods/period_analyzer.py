
class PeriodAnalyzer:

    def __init__(self, average_dict, name):
        self.average_dict = average_dict
        self.name = name

    def analyze(self):
        keys = sorted(self.average_dict.keys(), reverse=True)
        last_average_key = keys[0]
        second_last_average_key = keys[1]

        #print(last_average_key, self.average_dict[last_average_key])
        #print(second_last_average_key, self.average_dict[second_last_average_key])

        value1 = self.average_dict[last_average_key]
        value2 = self.average_dict[second_last_average_key]

        if value1 > value2:
            #print("{}: Up".format(self.name))
            return "up"
        elif value1 < value2:
            #print("{}: Down".format(self.name))
            return "down"
        else:
            #print("{}: No change".format(self.name))
            return "none"
