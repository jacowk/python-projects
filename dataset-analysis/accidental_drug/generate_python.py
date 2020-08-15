def generate_csv_init():
    fields = ['ID', 'Date', 'DateType', 'Age', 'Sex', 'Race', 'ResidenceCity', 'ResidenceCounty', 'ResidenceState', 'DeathCity', 'DeathCounty', 'Location', 'LocationifOther', 'DescriptionofInjury', 'InjuryPlace', 'InjuryCity', 'InjuryCounty', 'InjuryState', 'COD', 'OtherSignifican', 'Heroin', 'Cocaine', 'Fentanyl', 'FentanylAnalogue', 'Oxycodone', 'Oxymorphone', 'Ethanol', 'Hydrocodone', 'Benzodiazepine', 'Methadone', 'Amphet', 'Tramad', 'Morphine_NotHeroin', 'Hydromorphone', 'Other', 'OpiateNOS', 'AnyOpioid', 'MannerofDeath', 'DeathCityGeo', 'ResidenceCityGeo', 'InjuryCityGeo']
    cnt = 0
    for field in fields:
        print("{} = row[{}]".format(field, cnt))
        cnt += 1

def generate_print_statements():
    fields = ['ID', 'Date', 'DateType', 'Age', 'Sex', 'Race', 'ResidenceCity', 'ResidenceCounty', 'ResidenceState', 'DeathCity', 'DeathCounty', 'Location', 'LocationifOther', 'DescriptionofInjury', 'InjuryPlace', 'InjuryCity', 'InjuryCounty', 'InjuryState', 'COD', 'OtherSignifican', 'Heroin', 'Cocaine', 'Fentanyl', 'FentanylAnalogue', 'Oxycodone', 'Oxymorphone', 'Ethanol', 'Hydrocodone', 'Benzodiazepine', 'Methadone', 'Amphet', 'Tramad', 'Morphine_NotHeroin', 'Hydromorphone', 'Other', 'OpiateNOS', 'AnyOpioid', 'MannerofDeath', 'DeathCityGeo', 'ResidenceCityGeo', 'InjuryCityGeo']
    for field in fields:
        print("print('{}: ', {})".format(field, field))

def scrub_items():
    fields = ['ID', 'Date', 'DateType', 'Age', 'Sex', 'Race', 'ResidenceCity', 'ResidenceCounty', 'ResidenceState',
              'DeathCity', 'DeathCounty', 'Location', 'LocationifOther', 'DescriptionofInjury', 'InjuryPlace',
              'InjuryCity', 'InjuryCounty', 'InjuryState', 'COD', 'OtherSignifican', 'Heroin', 'Cocaine', 'Fentanyl',
              'FentanylAnalogue', 'Oxycodone', 'Oxymorphone', 'Ethanol', 'Hydrocodone', 'Benzodiazepine', 'Methadone',
              'Amphet', 'Tramad', 'Morphine_NotHeroin', 'Hydromorphone', 'Other', 'OpiateNOS', 'AnyOpioid',
              'MannerofDeath', 'DeathCityGeo', 'ResidenceCityGeo', 'InjuryCityGeo']
    for field in fields:
        print("{},".format(field.lower()))

def create_insert_statements():
    fields = ['ID', 'Date', 'DateType', 'Age', 'Sex', 'Race', 'ResidenceCity', 'ResidenceCounty', 'ResidenceState',
              'DeathCity', 'DeathCounty', 'Location', 'LocationifOther', 'DescriptionofInjury', 'InjuryPlace',
              'InjuryCity', 'InjuryCounty', 'InjuryState', 'COD', 'OtherSignifican', 'Heroin', 'Cocaine', 'Fentanyl',
              'FentanylAnalogue', 'Oxycodone', 'Oxymorphone', 'Ethanol', 'Hydrocodone', 'Benzodiazepine', 'Methadone',
              'Amphet', 'Tramad', 'Morphine_NotHeroin', 'Hydromorphone', 'Other', 'OpiateNOS', 'AnyOpioid',
              'MannerofDeath', 'DeathCityGeo', 'ResidenceCityGeo', 'InjuryCityGeo']
    insert_string = 'insert into accidental_drug('
    for field in fields:
        insert_string += "{}, ".format(field.lower())
    print(insert_string)

def compare_values():
    columns = ['id','ddate','datetype','age','sex','race','residencecity','residencecounty','residencestate','deathcity','deathcounty','location','locationifother','descriptionofinjury','injuryplace','injurycity','injurycounty','injurystate','cod','othersignifican','heroin','cocaine','fentanyl','fentanylanalogue','oxycodone','oxymorphone','ethanol','hydrocodone','benzodiazepine','methadone','amphet','tramad','morphine_notheroin','hydromorphone','other','opiatenos','anyopioid','mannerofdeath','deathcitygeo','residencecitygeo','injurycitygeo']
    values = ['18-1009','2018-12-28 12:00:00','DateofDeath','24','Male','White','SOUTHWICK','HAMPDEN','MA','WETHERSFIELD','HARTFORD','Other','','Substance Abuse','Friends Residence','','','','Acute Intoxication due to the Combined Effects of Acetyl Fentanyl Fentanyl and Mitragynine','',0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,'Accident','WETHERSFIELD| CT(41.712487| -72.663607)','SOUTHWICK| CT(41.984699| -72.516098)','CT(41.575155| -72.738288)']
    print("Columns: {}".format(len(columns)))
    print("Values: {}".format(len(values)))
    print("")
    for i in range(0, len(columns)):
        print("{}: {}".format(columns[i], values[i]))
        #print("{},".format(columns[i]))

def split_values():
    values = "ad.heroin,ad.cocaine,ad.fentanyl,ad.fentanylanalogue,ad.oxycodone,ad.oxymorphone,ad.ethanol,ad.hydrocodone,ad.benzodiazepine,ad.methadone,ad.amphet,ad.tramad,ad.morphine_notheroin,ad.hydromorphone,ad.other,ad.opiatenos,ad.anyopioid"
    values_split = values.split(",")
    new_string = ""
    for value in values_split:
        new_string += "'{}',".format(value.lstrip("ad."))
        #print("'{}',".format(value))
    print(new_string)

#generate_csv_init()
#generate_print_statements()
#scrub_items()
#create_insert_statements()
#compare_values()
split_values()