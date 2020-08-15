"""
@author: Jaco Koekemoer
@date: 2020-08-14
"""
import gmail_oo.gmail_connector as gc
import gmail_oo.delete_message as dm

class DeleteGmailApp:

    def run(self):
        gmail_connector = gc.GMailConnector()
        service = gmail_connector.connect()

        user_id = 'me'
        msg_id = '170a44f0500979df'
        delete_message = dm.DeleteMessage(user_id)
        delete_message.delete(msg_id)
        print("Delete is done")

if __name__ == '__main__':
    delete_gmail_app = DeleteGmailApp()
    delete_gmail_app.run()