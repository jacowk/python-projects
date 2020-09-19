import gmail_oo.gmail_connector as gc
import gmail_oo.get_message as gm

msg_id = ""

gmail_connector = gc.GMailConnector()
service = gmail_connector.connect()

user_id = 'me'
get_message = gm.GetMessage(service, user_id)
message = get_message.get(msg_id)