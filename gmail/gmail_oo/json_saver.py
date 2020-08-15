"""
@author: Jaco Koekemoer
@date: 2020-08-14
"""
import json

class JSONSaver:

    def save(self, json_filename, json_data):
        print("Saving")
        json_format = json.dumps(json_data)
        f = open(json_filename, 'w')
        f.write(json_format)