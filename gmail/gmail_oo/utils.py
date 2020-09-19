"""
@author: Jaco Koekemoer
@date: 2020-08-15
"""
import enum

class GmailEnum(enum.Enum):
    USER_ID = 'me'
    LABELS_FILE = '/home/jaco/python-data/gmail/gmail_labels.json' # A generic file where all email messages are stored

    # For create_label_oo.py
    LABEL_NAME = 'Shilin' # A single label name

    # For list_messages_query_app.py
    FILENAME_SUBSTRING = 'tripadvisor' # Substring of the name where the messages are stored in JSON format
    EMAIL_FROM = 'member@expm.tripadvisor.com' # Finding all emails with this from address
    ADD_LABEL_NAMES = [ 'Tripadvisor' ] # Label names to add
    DELETE_LABEL_NAMES = [ 'INBOX' ] # Label names to remove

    # Structure: "file_postfix": ["GMail Label Name": "From email address"]
    RELABEL_LIST = {

    }

    """RELABEL_LIST = {
        "unitedwithisrael": ["United with Israel", "news@unitedwithisrael.org"],
        "lifestylebymyowndesign": ["Lifestyle By My Own Design", "mail@lifestylebymyowndesign.com"],
        "moneymorning_1": ["Money Morning", "moneymorning@newsletter.fsp.co.za"],
        "pinterest_1": ["Pinterest", "pinbot@explore.pinterest.com"],
        "moneymorning_2": ["Money Morning", "moneymorning@newsletters.fspinvest.co.za"],
        "pinterest_2": ["Pinterest", "pinbot@notifications.pinterest.com"],
        "worldisraelnews_1": ["World Israel News", "news@worldisraelnews.com"],
        "worldisraelnews_2": ["World Israel News", "offers@worldisraelnews.com"],
        "envato": ["Envato", "market.news@envato.com"],
        "amazon_10": ["Amazon", "store-news@amazon.com"],
        "depositphotos": ["Deposit Photos", "mail@depositphotos.com"],
        "linkedin_10": ["LinkedIn", "invitations@linkedin.com"],
        "wpelevation": ["WP Elevation", "troy@wpelevation.com"],
        "shopify": ["Shopify", "email@email.shopify.com"],
        "mailchimp_10": ["MailChimp", "whatsinstore@mailchimp.com"],
        
        "absa": ["ABSA", "officialemail@absa.co.za"],
        "absarewards": ["ABSA", "absa@email.absarewards.co.za"],
        "absamuneera": ["ABSA", "Muneera.Ismail@absa.africa"],
        "absaodp": ["ABSA", "ODPMail@absa.co.za"],
        "afriforum_1": ["AfriForum", "no-reply@afriforum.co.za"],
        "afriforum_2": ["AfriForum", "no-reply@afriforum.org"],
        "afriforum_3": ["AfriForum", "ledenavorsing@afriforum.co.za"],
        "afrihostnoreply1": ["Afrihost", "no-reply@afrihost.com"],
        "afrihostnoreply2": ["Afrihost", "noreply@afrihost.com"],
        "afrihost_fibre": ["Afrihost", "fibre@afrihost.com"],
        "afrihost_support": ["Afrihost", "support@afrihost.com"],
        "ajay": ["Ajays Art Classes", "info@ajaysart.co.za"],
        "alunhill": ["Alun Hill", "alunhill@getrevue.co"],
        "amazonaccount": ["Amazon", "account-update@amazon.com"],
        "amazonfnasatti": ["Amazon", "fnasatti@amazon.com"],
        "amazonaws": ["Amazon", "aws-apac-marketing@amazon.com"],
        "amazonreviews": ["Amazon", "customer-reviews-messages@amazon.com"],
        "andrewwalker": ["Andrew Walker", "SAPropertyInvestorNetworkPretoria-announce@meetup.com"],
        "apple": ["Apple", "noreply@email.apple.com"],
        "avis": ["Avis", "noreply@avisbudget.co.za"],
        "babbel": ["Babbel", "members@service.babbel.com"],
        "bitly": ["Bitly", "team@accounts.bitly.com"],
        "britannica": ["Britannica", "noreply@email.britannica.com"],
        "bmw": ["BMW", "newsletter@sandton-bmw.co.za"],
        "cartrack": ["Cartrack", "noreply@cartrack.com"],
        "coj": ["City of Johannesburg", "no-reply@cojestatements.co.za"],
        "clickbank": ["ClickBank", "noreply@mail.clickbank.com"],
        "clickbankuni": ["ClickBank", "no-email@clickbankuniversity.com"],
        "coursera": ["Coursera", "no-reply@t.mail.coursera.org"],
        "covenanteyes": ["Covenant Eyes", "resources@covenanteyes.com"],
        "crystalcove": ["Crystal Cove", "info@tjcadmin.co.za"],
        "crystalcovesupport": ["Crystal Cove", "support@tjcadmin.co.za"],
        "dailyclaims": ["Discovery", "dailyclaims@discovery.co.za"],
        "dischem": ["Dischem", "no-reply@dischem.co.za"],
        "discovery": ["Discovery", "noreply@discovery.co.za"],
        "discoveryqueries": ["Discovery", "alldiscoveryqueries@discovery.co.za"],
        "discoverynoach": ["Discovery", "ryannoach@discovery.co.za"],
        "discoveryinvest": ["Discovery Invest", "invest_servicing_support@discovery.co.za"],
        "discoveryinfo": ["Discovery", "Discoveryinfo@discovery.co.za"],
        "discoveryhealth_1": ["Discovery Health", "infohealth@discovery.co.za"],
        "discoveryhealth_2": ["Discovery Health", "yourhealth@email.discovery.co.za"],
        "discoverychronic": ["Discovery Health", "chronicqueries@discovery.co.za"],
        "discoveryars": ["Discovery Vitality", "ARS_Testing@discovery.co.za"],
        "discoveryreward": ["Discovery Vitality", "rewardstatement@discovery.co.za"],
        "discoverycovid19": ["Discovery", "covid19updates@email.discovery.co.za"],
        "discoverylife_1": ["Discovery Life", "lifenews@discovery.co.za"],
        "discoverylife_2": ["Discovery Life", "lifecampaigns@discovery.co.za"],
        "docker_1": ["Docker", "events@docker.com"],
        "docker_2": ["Docker", "dockercon@docker.com"],
        "docker_3": ["Docker", "do-not-reply@docker.com"],
        "dropbox": ["Dropbox", "no-reply@dropbox.com"],
        "dropboxmail": ["Dropbox", "no-reply@dropboxmail.com"],
        "dzone": ["DZone", "mailer@dzone.com"],
        "easyequities": ["Easy Equities", "campaigns@easyequities.co.za"],
        "easyequitiesnoreply": ["Easy Equities", "noreply@easyequities.co.za"],
        "ebay": ["eBay", "AskEPN@mail.ebaypartnernetwork.com"],
        "ebenpagan": ["Eben Pagan", "help@ebenpagan.com"],
        "elize": ["Elize Begeman", "elizeb@littlefalls.co.za"],
        "enneagram": ["Enneagram", "results@enneagramtest.net"],
        "evernote": ["Evernote", "team@emails.evernote.com"],
        "flipboard": ["Flipboard", "security-notification@flipboard.com"],
        "franticmommy": ["Franticmommy", "rebecca@franticmommy.com"],
        "gilangork": ["Gilan Gork", "direct@gilangork.com"],
        "google": ["Google", "no-reply@google.com"],
        "googlepartners": ["Google", "partners-noreply@google.com"],
        "googlemaps": ["Google", "google-maps-noreply@google.com"],
        "googleaccounts": ["Google", "no-reply@accounts.google.com"],
        "googleutos": ["Google", "noreply-utos@google.com"],
        "harshagrawal": ["Harsh Agrawal", "hello@shoutmeloud.com"],
        "itickets": ["iTickets", "help@itickets.co.za"],
        "israel365": ["Israel365", "israel365@israel365.com"],
        "israel365promotions": ["Israel365", "promotions@israel365.com"],
        "jvzoonews": ["JVZoo", "News@jvzoo.com"],
        "jacogmail": ["Jaco Koekemoer", "jaco.wk@gmail.com"],
        "jacokoekemoer": ["Jaco Koekemoer", "JacoK@discovery.co.za"],
        "jvzoo": ["JVZoo", "jvzoo@jvzoo.com"],
        "jvzoosupport": ["JVZoo", "support@jvzoo.com"],
        "kaggle": ["Kaggle", "alexis.cook@kaggle.intercom-mail.com"],
        "kcm_1": ["Kenneth Copeland", "kennethcopelandministries@e1.kcm.org"],
        "kcmza": ["Kenneth Copeland", "partners@kcmza.org"],
        "kcmweb": ["Kenneth Copeland", "webmaster@kcm.org.za"],
        "kcmvictory": ["Kenneth Copeland", "social@govictory.com"],
        "liberty": ["Liberty", "info@liberty.co.za"],
        "lightstonejen": ["Lightstone", "jennyh@lightstone.co.za"],
        "linkedin_1": ["LinkedIn", "notifications-noreply@linkedin.com"],
        "linkedin_2": ["LinkedIn", "inmail-hit-reply@linkedin.com"],
        "linkedinjobs": ["LinkedIn", "jobs-listings@linkedin.com"],
        "linkedinmessages": ["LinkedIn", "messages-noreply@linkedin.com"],
        "lfcc_1": ["LFCC", "no-reply@churchcenter.com"],
        "lfcc_2": ["LFCC", "noreply@churchcenter.com"],
        "lfcclittlefalls": ["LFCC", "littlefalls@churchcenter.com"],
        "luno": ["Luno", "noreply@mailer.luno.com"],
        "mailchimp": ["MailChimp", "legalnotice@mailchimp.co"],
        "mailchimp": ["MailChimp", "alerts@mailchimp.com"],
        "mailchimplegal": ["MailChimp", "legalnotice@mailchimp.com"],
        "mandysart": ["Mandysart", "info@mandysart.co.za"],
        "mary": ["Mary Eberendu", "maeberendu@gmail.com"],
        "mariettenoreply", ["Mariette Janse van Rensburg", "no-reply@work.za.com"],
        "mealsonwheels": ["Meals on Wheels", "admin@mealsonwheels.co.za"],
        "meetup": ["Meetup", "info@meetup.com"],
        "moneyweb": ["Moneyweb", "help@moneyweb.co.za"],
        "mtnmtn": ["MTN", "mtn@mtn.com"],
        "mtn": ["MTN", "CustomerCare@mtn.com"],
        "mtn_1": ["MTN", "MTN@mtn.co.za"],
        "mtnshop": ["MTN", "shop@mtn.co.za"],
        "mtnnoreply": ["MTN", "noreply@mtn.co.za"],
        "mtnconstellation": ["MTN", "system@constellationrms.com"],
        "mtnbusiness": ["MTN", "mtnbusiness@mtn.com"],
        "mwb": ["Mission Without Borders", "jdekock@mwbi.org"],
        "namecheap": ["Namecheap", "hello@namecheap.com"],
        "nedbank": ["Nedbank", "TP-campaigns@nedbank.co.za"],
        "nedbankcard": ["Nedbank", "cardnoreply@nedbank.co.za"],
        "offervault": ["Offervault", "mark@offervault.com"],
        "onedrive": ["One Drive", "email@mail.onedrive.com"],
        "people": ["People", "updates@people.io"],
        "phil": ["Phil Pustejovsky", "phil@freedommentor.com"],
        "pinterest_1": ["Pinterest", "pinbot@account.pinterest.com"],
        "pinterest_2": ["Pinterest", "noreply@account.pinterest.com"],
        "postman": ["Postman", "noreply@notifications.getpostman.com"],
        "proko": ["Proko", "support@proko.com"],
        "property24": ["Property24", "no-reply@property24.com"],
        "rabbitulyweisz": ["Rabbi Tuly Weisz", "rabbituly@israel365.com"],
        "realpython": ["Real Python", "info@realpython.com"],
        "reshmachanda": ["Reshma Ansary", "Chanda.Prinsloo@dfc.discovery.co.za"],
        "samanthasmit": ["Samantha Smit", "Emsreply@absa.co.za"],
        "sars": ["SARS", "NOREPLY@sars.gov.za"],
        "saseeding": ["SA Seeding", "no-reply@saseeding.co.za"],
        "satrixnews": ["Satrix", "satrixnews@satrix.co.za"],
        "seedtime": ["SeedTime", "bob@seedtime.com"],
        "scienceofpeople": ["Science of People", "support@scienceofpeople.com"],
        "sherrifhq": ["SheriffHQ", "admin@sheriffhq.co.za"],
        "shilin": ["Shilin", "contact@shilin.co.za"],
        "steers": ["Steers", "hello@yumbi.com"],
        "stephanbester": ["Dr Stephan Bester", "michelle@besterpractice.co.za"],
        "satrixnews": ["Satrix", "satrixnews@satrix.co.za"],
        "saproperty": ["SA Property Investor", "accounts@sapropertynetwork.com"],
        "sapropertyevents": ["SA Property Investor", "events@sapropertynetwork.com"],
        "scienceofpeople": ["Science of People", "support@scienceofpeople.com"],
        "spekfin": ["Spekfin", "admin@spekfin.co.za"],
        "takealot": ["Takealot", "info@takealot.com"],
        "tanya": ["Tanya Koekemoer", "tanya.horn1975@gmail.com"], 
        "telkom": ["Telkom", "do_not_reply@telkom.co.za"],
        "telkomreply": ["Telkom", "Do_Not_Reply@telkom.co.za"],
        "telkomonline": ["Telkom", "telkom-online@telkom.co.za"],
        "theartist": ["The Artist", "Info@theartist.co.za"],
        "thelifestyleteam": ["The Lifestyle Team", "mail@aspirewithchris.com"],
        "tracey": ["Tracey du Plessis", "tracey@tjcadmin.co.za"],
        "theartist": ["The Artist", "denise@theartist.co.za"],
        "thepropertycollab": ["The Property Collab", "The-Property-Collab-announce@meetup.com"],
        "thepropertycollablist": ["The Property Collab", "The-Property-Collab-list@meetup.com"],
        "tripadvisormember": ["Tripadvisor", "MemberUpdate@mp1.tripadvisor.com"],
        "tripadvisormember_1": ["Tripadvisor", "members@mp1.tripadvisor.com"],
        "tripadvisormember_2": ["", "member@expm.tripadvisor.com"],
        "tjcadmin": ["Crystal Cove", "info@tjcadmin.co.za"],
        "typeform": ["Typeform", "no-reply@typeform.com"],
        "quora": ["Quora", "curiosity-noreply@quora.com"],
        "quoracovid": ["Quora", "covid-noreply@quora.com"],
        "quoradigest": ["Quora", "digest-noreply@quora.com"],
        "rabbituly": ["Rabbi Tuly Weisz", "RabbiTuly@israel365.com"],
        "revelationmedia": ["RevelationMedia", "system@revelationmedia.com"],
        "reshma": ["Reshma Ansary", "ReshmaA@discovery.co.za"],
        "sake": ["SAKE", "sake@sa-chamber.co.za"],
        "studiopress": ["StudioPress", "news@studiopress.com"],
        "surveymonkey": ["Survey Monkey", "no-reply@core.co.za"],
        "tigerwheel": ["Tiger Wheel", "workflow@tiauto.co.za"],
        "torgaoptical": ["Torga Optical", "customercare@torgaoptical.co.za"],
        "udemy": ["Udemy", "udemy@email.udemy.com"],
        "udemymail": ["Udemy", "no-reply@e.udemymail.com"],
        "unity": ["Unity", "info@unity3d.com"],
        "unitedisrael": ["United with Israel", "info@unitedwithisrael.org"],
        "unsplash": ["Unsplash", "delivery@unsplash.com"],
        "upwork": ["Upwork", "upwork@e.upwork.com"],
        "vumatel": ["Vumatel", "scheduling@vumatel.co.za"],
        "wish": ["Wish", "offers@wish.com"],
        "yahoo": ["Yahoo", "no-reply@cc.yahoo-inc.com"],
        "yahooinfo": ["Yahoo", "info@service.comms.yahoo.net"],
        "youtube": ["YouTube", "no-reply@youtube.com"],
        "youversion": ["YouVersion", "no-reply@youversion.com"],
        "zoom": ["Zoom", "support@zoom.us"],
        "zoomnoreply": ["Zoom", "no-reply@zoom.us"]
    }"""

    DELETE_LIST = {
        "anik_1": ["Anik Singal", "support@lurn.com"],
        "anik_2": ["Anik Singal", "support @ lurn.com"],
        "anik_3": ["Anik Singal", "anik@lurnation.com"],
        "anik_4": ["Anik Singal", "anik@lurnnation.com"],
        "anik_5": ["Anik Singal", "support @ lurn.com"],
        "anik_6": ["Anik Singal", "anik@inboxblueprint.com"],
        "anik_7": ["Anik Singal", "aniktheleadfighter@lurn.com"],
        "php": ["PHP", "PHP-Johannesburg-Meetup-Group-announce@meetup.com"],
        "depositphotos": ["Deposit Photos", "no-reply@depositphotos.com"],
        "bni": ["BNI", "BusinessNetworkingJohannesburg-announce@meetup.com"]
    }

# email_from = 'noreply@steampowered.com'
# email_from = 'no-reply@bounce.slideshare.net'
# email_from = 'no-reply@m.mail.coursera.org'
# email_from = 'info@revelationmedia.com'
# email_from = 'john@johncrestani.com'
# email_from = 'no-reply@property24.com'

# Testing
#print(GmailEnum.FILENAME_SUBSTRING.name)
#print(GmailEnum.FILENAME_SUBSTRING.value)

def delete_confirmation():
    confirmation = input("Do you want to continue deleting the messages? (Y/N) ")
    if confirmation.lower() == 'y':
        return True
    return False

def confirmation(display_message):
    confirmation = input("{} (Y/N) ".format(display_message))
    if confirmation.lower() == 'y':
        return True
    return False

def print_section_divider():
    print("==" * 20)

def strip_email_address(value):
    #Pinterest <pinbot@explore.pinterest.com>
    delimiter = "<"
    if delimiter in value:
        split_value = value.split("<")
        email_address = split_value[1]
        return email_address[0:len(email_address) - 1]
    else:
        return value
