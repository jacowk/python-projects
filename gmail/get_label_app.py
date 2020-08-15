"""
@author: Jaco Koekemoer
@date: 2020-08-15
"""
import gmail_oo.gmail_connector as gc
import gmail_oo.get_label_for_name as gl
import gmail_oo.utils as u

class RetrieveLabelApp:

    def run(self):
        # Connect to GMail
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()
        user_name = 'me'

        get_label_for_name = gl.GetLabelForName(service, user_name)
        label = get_label_for_name.get(u.GmailEnum.LABEL_NAME.value)

        print(label)

if __name__ == '__main__':
    retrieve_label_app = RetrieveLabelApp()
    retrieve_label_app.run()
