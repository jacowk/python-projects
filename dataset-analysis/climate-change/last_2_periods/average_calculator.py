
class AverageCalculator:

    def __init__(self, page_list):
        self.page_list = page_list

    def calculate(self):
        average_dict = dict()
        for temp_dict in self.page_list:
            total = 0
            cnt = 0
            temp_key = ''
            for key in sorted(temp_dict.keys(), reverse=False):
                total += temp_dict[key]
                cnt += 1
                temp_key = key
            average_dict[temp_key] = round(total / cnt, 2)
        return average_dict