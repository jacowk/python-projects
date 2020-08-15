#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:06:48 2020

@author: jaco

https://catalog.data.gov/dataset?tags=crime
https://data.world/jaco-koekemoer/personaldataanalysis

"""
import csv #https://docs.python.org/3/library/csv.html
import mysql.connector as mysql
from datetime import datetime
import utils as u

db = mysql.connect(host="localhost",  # your host
                     user="root",       # username
                     passwd="password",     # password
                     db="python_base")   # name of the database

filename = "/home/jaco/python-data/datasets/accidental_drug/Accidental_Drug_Related_Deaths_2012-2018.csv"

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print ("Database version : %s " % data)

errors = []

# Import csv
with open(filename, newline = '') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    cnt = 1

    for row in datareader:
        if cnt == 1:
            cnt += 1
            continue #Skip first line with only column names

        ID = row[0]
        Date = u.format_date(row[1])
        DateType = row[2]
        Age = u.format_integer(row[3])
        Sex = row[4]
        Race = u.format_race(row[5])
        ResidenceCity = row[6]
        ResidenceCounty = row[7]
        ResidenceState = row[8]
        DeathCity = row[9]
        DeathCounty = row[10]
        Location = row[11]
        LocationifOther = u.format_single_quote(row[12])
        DescriptionofInjury = u.format_single_quote(row[13])
        InjuryPlace = row[14]
        InjuryCity = row[15]
        InjuryCounty = row[16]
        InjuryState = row[17]
        COD = row[18]
        OtherSignifican = row[19]
        Heroin = u.format_boolean(row[20])
        Cocaine = u.format_boolean(row[21])
        Fentanyl = u.format_boolean(row[22])
        FentanylAnalogue = u.format_boolean(row[23])
        Oxycodone = u.format_boolean(row[24])
        Oxymorphone = u.format_boolean(row[25])
        Ethanol = u.format_boolean(row[26])
        Hydrocodone = u.format_boolean(row[27])
        Benzodiazepine = u.format_boolean(row[28])
        Methadone = u.format_boolean(row[29])
        Amphet = u.format_boolean(row[30])
        Tramad = u.format_boolean(row[31])
        Morphine_NotHeroin = u.format_boolean(row[32])
        Hydromorphone = u.format_boolean(row[33])
        Other = u.format_boolean(row[34])
        OpiateNOS = u.format_boolean(row[35])
        AnyOpioid = u.format_boolean(row[36])
        MannerofDeath = row[37]
        DeathCityGeo = u.format_geo(row[38])
        ResidenceCityGeo = u.format_geo(row[39])
        InjuryCityGeo = u.format_geo(row[40])

        """
        print('ID: ', ID)
        print('Date: ', Date)
        print('DateType: ', DateType)
        print('Age: ', Age)
        print('Sex: ', Sex)
        print('Race: ', Race)
        print('ResidenceCity: ', ResidenceCity)
        print('ResidenceCounty: ', ResidenceCounty)
        print('ResidenceState: ', ResidenceState)
        print('DeathCity: ', DeathCity)
        print('DeathCounty: ', DeathCounty)
        print('Location: ', Location)
        print('LocationifOther: ', LocationifOther)
        print('DescriptionofInjury: ', DescriptionofInjury)
        print('InjuryPlace: ', InjuryPlace)
        print('InjuryCity: ', InjuryCity)
        print('InjuryCounty: ', InjuryCounty)
        print('InjuryState: ', InjuryState)
        print('COD: ', COD)
        print('OtherSignifican: ', OtherSignifican)
        print('Heroin: ', Heroin)
        print('Cocaine: ', Cocaine)
        print('Fentanyl: ', Fentanyl)
        print('FentanylAnalogue: ', FentanylAnalogue)
        print('Oxycodone: ', Oxycodone)
        print('Oxymorphone: ', Oxymorphone)
        print('Ethanol: ', Ethanol)
        print('Hydrocodone: ', Hydrocodone)
        print('Benzodiazepine: ', Benzodiazepine)
        print('Methadone: ', Methadone)
        print('Amphet: ', Amphet)
        print('Tramad: ', Tramad)
        print('Morphine_NotHeroin: ', Morphine_NotHeroin)
        print('Hydromorphone: ', Hydromorphone)
        print('Other: ', Other)
        print('OpiateNOS: ', OpiateNOS)
        print('AnyOpioid: ', AnyOpioid)
        print('MannerofDeath: ', MannerofDeath)
        print('DeathCityGeo: ', DeathCityGeo)
        print('ResidenceCityGeo: ', ResidenceCityGeo)
        print('InjuryCityGeo: ', InjuryCityGeo)
        """


        # prepare a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare SQL query to INSERT a record into the database.
        sql = "insert into accidental_drug(id, ddate, datetype, age, sex, race, residencecity, residencecounty, residencestate, deathcity, deathcounty, location, locationifother, descriptionofinjury, injuryplace, injurycity, injurycounty, injurystate, cod, othersignifican, heroin, cocaine, fentanyl, fentanylanalogue, oxycodone, oxymorphone, ethanol, hydrocodone, benzodiazepine, methadone, amphet, tramad, morphine_notheroin, hydromorphone, other, opiatenos, anyopioid, mannerofdeath, deathcitygeo, residencecitygeo, injurycitygeo) values (" \
            "'{:s}'," \
            "'{:%Y-%m-%d %H:%M:%S}'," \
            "'{:s}'," \
            "{:d}," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "{:d}," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}'," \
            "'{:s}');".format(
            ID,
            Date,
            DateType,
            Age,
            Sex,
            Race,
            ResidenceCity,
            ResidenceCounty,
            ResidenceState,
            DeathCity,
            DeathCounty,
            Location,
            LocationifOther,
            DescriptionofInjury,
            InjuryPlace,
            InjuryCity,
            InjuryCounty,
            InjuryState,
            COD,
            OtherSignifican,
            Heroin,
            Cocaine,
            Fentanyl,
            FentanylAnalogue,
            Oxycodone,
            Oxymorphone,
            Ethanol,
            Hydrocodone,
            Benzodiazepine,
            Methadone,
            Amphet,
            Tramad,
            Morphine_NotHeroin,
            Hydromorphone,
            Other,
            OpiateNOS,
            AnyOpioid,
            MannerofDeath,
            DeathCityGeo,
            ResidenceCityGeo,
            InjuryCityGeo);

        #print("{}: {}".format(cnt, sql))

        try:
           # Execute the SQL command
           cursor.execute(sql)
           # Commit your changes in the database
           db.commit()
        except Exception as e:
           # Rollback in case there is any error
           print ("An error occured, rolling back for {:s}: {}".format(ID, str(e)))
           print("Error: {}".format(sql))
           errors.append(sql)
           db.rollback()

        cnt += 1

        """
        print('\n')
        key = input("Press any key to continue, or 'q' to quite...")
        print('\n')
        if key == 'q':
            break
        """

# disconnect from server
db.close()

for error in errors:
    print("Error: {}".format(error))