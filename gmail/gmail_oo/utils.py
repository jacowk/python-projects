"""
@author: Jaco Koekemoer
@date: 2020-08-15
"""
import enum

class GmailEnum(enum.Enum):
    FILENAME_SUBSTRING = 'dzone' # Substring of the name where the messages are stored in JSON format
    EMAIL_FROM = 'mailer@dzone.com' # Finding all emails with this from address
    LABELS_FILE = '/home/jaco/python-data/gmail/gmail_labels.json' # A generic file where all email messages are stored
    LABEL_NAME = 'Jaco Koekemoer' # A single label name
    ADD_LABEL_NAMES = [ 'DZone' ] # Label names to add
    DELETE_LABEL_NAMES = [ 'INBOX' ] # Label names to remove

# email_from = 'noreply@steampowered.com'
# email_from = 'no-reply@bounce.slideshare.net'
# email_from = 'no-reply@m.mail.coursera.org'
# email_from = 'info@revelationmedia.com'
# email_from = 'john@johncrestani.com'
# email_from = 'no-reply@property24.com'

# Testing
#print(GmailEnum.FILENAME_SUBSTRING.name)
#print(GmailEnum.FILENAME_SUBSTRING.value)