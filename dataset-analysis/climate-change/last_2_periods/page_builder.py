
class PageBuilder:

    def __init__(self, result_dict, no_years):
        self.result_dict = result_dict
        self.no_years = no_years

    def build(self):
        page_list = list()
        temp_cnt = 1
        temp_dict = dict()
        for key in sorted(self.result_dict.keys(), reverse=False):
            if temp_cnt > self.no_years:
                page_list.append(temp_dict)
                temp_dict = dict()
                temp_cnt = 1
            temp_dict[key] = self.result_dict[key]
            temp_cnt += 1
        page_list.append(temp_dict)
        return page_list