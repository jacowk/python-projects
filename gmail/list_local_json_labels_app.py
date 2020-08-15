"""
@author: Jaco Koekemoer
@date: 2020-08-15
"""
import gmail_oo.list_local_json_labels as lj

class ListLocalJSONLabelsApp:

    def run(self):
        local_json = lj.ListLocalJSONLabels()
        local_json.list()

if __name__ == '__main__':
    list_local = ListLocalJSONLabelsApp()
    list_local.run()
