"""
@author: Jaco Koekemoer
@date: 2020-08-14
"""
import json

class JSONRetriever:

    def retrieve(self, json_filename):
        print("Retrieving")
        # Read file
        try:
            f = open(json_filename, 'r')
            json_raw_data = f.read()
            json_data = json.loads(json_raw_data)
            return json_data
        except Exception as e:
            print("File could not be opened: {}".format(e))
