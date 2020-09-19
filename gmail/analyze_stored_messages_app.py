"""
@author: Jaco Koekemoer
@date: 2020-09-13

Using a previously stored list of messages ids, retrieve those message contents, and store them in a file.
"""
import os.path
import gmail_oo.json_retriever as jr
import gmail_oo.json_saver as js
import gmail_oo.utils as u

class AnalyzeStoredMessagesApp:

    def __init__(self, store_directory):
        self.store_directory = store_directory

    def run(self):
        result_path = "/home/jaco/python-data/gmail/inbox_analysis.csv"
        json_filename = "/home/jaco/python-data/gmail/inbox_analysis.json"

        # Get a list of all the files
        file_list = os.listdir(self.store_directory)
        print("Count: {}".format(len(file_list)))
        email_result = dict()

        # Loop the files
        total = len(file_list)
        count = 0
        for file in file_list:
            count += 1
            path = "{}/{}".format(self.store_directory, file)
            #print ("Procesing {} of {}: {}, {}".format(count, total, path, file))

            # Parse JSON
            json_retriever = jr.JSONRetriever()
            message = json_retriever.retrieve(path)

            # Get the email addresses
            payload = message['payload']
            headers = payload['headers']

            # Get message info
            subject = ""
            date_received = ""
            from_email = ""
            to_email = ""
            for header in headers:
                if header['name'] == "Subject":
                    subject = header['value']
                if header['name'] == "From":
                    from_email = header['value']
                if header['name'] == "Date":
                    date_received = header['value']
                if header['name'] == "To":
                    to_email = header['value']
            #print("From Email: {}".format(from_email))
            #print (u.strip_email_address(from_email))

            from_email_stripped = u.strip_email_address(from_email)

            if from_email_stripped in email_result.keys():
                message_list = email_result[from_email_stripped]
                message_list.append(file)
                email_result[from_email_stripped] = message_list
                #email_result[from_email_stripped] = email_result[from_email_stripped] + 1
            else:
                message_list = [ file ]
                email_result[from_email_stripped] = message_list
                #email_result[from_email_stripped] = 1


            # Print section header
            #u.print_section_divider()

            # Terminate early
            #if count == 5:
            #   break


        json_saver = js.JSONSaver()
        json_saver.save(json_filename, email_result)

        #f = open(result_path, 'a')
        #for key in email_result.keys():
        #    output = "{},{}\n".format(key, email_result[key])
        #    print(output)
        #    f.write(output)

        print("Done")


if __name__ == '__main__':
    store_directory = "/home/jaco/python-data/gmail/inbox"
    app = AnalyzeStoredMessagesApp(store_directory)
    app.run()
