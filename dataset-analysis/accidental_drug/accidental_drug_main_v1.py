#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:06:48 2020

@author: jaco

https://catalog.data.gov/dataset?tags=crime
https://data.world/jaco-koekemoer/personaldataanalysis

"""
import csv #https://docs.python.org/3/library/csv.html
#import stats_utils as su

filename = "/home/jaco/python-data/datasets/accidental_drug/Accidental_Drug_Related_Deaths_2012-2018.csv"

# Import csv
with open(filename, newline = '') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    cnt = 1

    values_string = ""
    for row in datareader:
        if cnt == 1:
            cnt += 1
            continue #Skip first line with only column names

        for i in range(0, 41):
            values_string += "'{}',".format(row[i].replace('\n', ''))

        ID = row[0]
        Date = row[1]
        DateType = row[2]
        Age = row[3]
        Sex = row[4]
        Race = row[5]
        ResidenceCity = row[6]
        ResidenceCounty = row[7]
        ResidenceState = row[8]
        DeathCity = row[9]
        DeathCounty = row[10]
        Location = row[11]
        LocationifOther = row[12]
        DescriptionofInjury = row[13]
        InjuryPlace = row[14]
        InjuryCity = row[15]
        InjuryCounty = row[16]
        InjuryState = row[17]
        COD = row[18]
        OtherSignifican = row[19]
        Heroin = row[20]
        Cocaine = row[21]
        Fentanyl = row[22]
        FentanylAnalogue = row[23]
        Oxycodone = row[24]
        Oxymorphone = row[25]
        Ethanol = row[26]
        Hydrocodone = row[27]
        Benzodiazepine = row[28]
        Methadone = row[29]
        Amphet = row[30]
        Tramad = row[31]
        Morphine_NotHeroin = row[32]
        Hydromorphone = row[33]
        Other = row[34]
        OpiateNOS = row[35]
        AnyOpioid = row[36]
        MannerofDeath = row[37]
        DeathCityGeo = row[38].replace('\n', '')
        ResidenceCityGeo = row[39].replace('\n', '')
        InjuryCityGeo = row[40].replace('\n', '')

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

        print("{}: {}".format(cnt, values_string))
        values_string = ''

        cnt += 1

        key = input("Press any key to continue, or 'q' to quite...")
        if key == 'q':
            break
