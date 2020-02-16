#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 09:06:48 2020

@author: jaco

https://catalog.data.gov/dataset?tags=crime
https://data.world/jaco-koekemoer/personaldataanalysis

"""
import csv #https://docs.python.org/3/library/csv.html
import stats_utils as su

filename = "nypd_arrests.csv"
race_statistics = {}
gender_statistics = {}
pd_dict = {}
pd_desc_statistics = {}
age_group_statistics = {}

# Import csv
with open(filename, newline = '') as csvfile:
    datareader = csv.reader(csvfile, delimiter=',')
    cnt = 1
    
    for row in datareader:
        if cnt == 1:
            cnt += 1
            continue #Skip first line with only column names
        
        ARREST_KEY = row[0]
        #print(ARREST_KEY)
        ARREST_DATE = row[1]
        PD_CD = row[2]
        PD_DESC = row[3]
        KY_CD = row[4]
        OFNS_DESC = row[5]
        LAW_CODE = row[6]
        LAW_CAT_CD = row[7]
        ARREST_BORO = row[8]
        ARREST_PRECINCT = row[9]
        JURISDICTION_CODE = row[10]
        AGE_GROUP = row[11]
        PERP_SEX = row[12]
        PERP_RACE = row[13]
        """X_COORD_CD = row[14]
        Y_COORD_CD = row[15]
        Latitude = row[16]
        Longitude = row[17]"""

        # Prep race statistics
        PERP_RACE = su.scrub_data(PERP_RACE)
        race_statistics = su.prep_stats(PERP_RACE, race_statistics)
        
        # Prep gender statistics
        PERP_SEX = su.scrub_data(PERP_SEX)
        gender_statistics = su.prep_stats(PERP_SEX, gender_statistics)
        
        # Harvest pd_cd and pd_desc values
        pd_dict = su.harvest_dict_values(PD_CD, PD_DESC, pd_dict)
        
        # Prep pd_desc statistics
        PD_DESC = su.scrub_data(PD_DESC)
        pd_desc_statistics = su.prep_stats(PD_DESC, pd_desc_statistics)
        
        # Prep age group statistics
        AGE_GROUP = su.scrub_data(AGE_GROUP)
        age_group_statistics = su.prep_stats(AGE_GROUP, age_group_statistics)

#su.output_sorted_dict("Race statistics:", race_statistics)
#su.output_sorted_dict("\nGender statistics:", gender_statistics)
#su.output_sorted_dict("\nPD Desc statistics:", pd_desc_statistics)
#su.output_sorted_dict("\nAge Group statistics:", age_group_statistics)
#su.output_sorted_dict("\nPD CD and PD Desc:", pd_dict)


"""
Total: 942096 nypd_arrests.csv


Race statistics:
american indian/alaskan native :: 2236
asian / pacific islander :: 45683
black :: 450559
black hispanic :: 80117
unknown :: 9231
white :: 114847
white hispanic :: 239422


Gender statistics:
f :: 161841
m :: 780254


Age Group statistics:
18-24 :: 238778
25-44 :: 455664
45-64 :: 179911
65+ :: 9012
<18 :: 58730


PD Desc statistics:
 :: 2713
a.b.c.,false proof of age :: 46
abortion 1 :: 4
absconding from work release 2 :: 2
accosting,fraudulent :: 445
adm.code,unclassified misdemea :: 46
adm.code,unclassified violatio :: 1593
adm.code,unclassified violation :: 8436
aggravated criminal contempt :: 456
aggravated harassment 1 :: 209
aggravated harassment 2 :: 11964
agriculture & markets law,uncl :: 1
agriculture & markets law,unclassified :: 248
alcoholic beverage control law :: 1327
appearance ticket fail to respond :: 117
arson 1 :: 8
arson 2,3,4 :: 289
assault 2,1,peace officer :: 3245
assault 2,1,unclassified :: 36189
assault 3 :: 81123
assembly,unlawful :: 405
bail jumping 1 & 2 :: 807
bail jumping 3 :: 1897
bicycle(traf.infrac. unclass.) :: 32
bribery,commercial :: 27
bribery,fraud :: 18
bribery,public administration :: 3348
burglars tools,unclassified :: 2338
burglary,residence,night :: 1715
burglary,unclassified,unknown :: 16
burglary,unclassified,unknown time :: 11858
check,bad :: 12
child abandonment :: 98
child, endangering welfare :: 5154
child,licensed premises :: 18
child,offenses against,unclass :: 3
child,offenses against,unclassified :: 330
coercion 1 :: 204
coercion 2 :: 40
computer tamper/tresspass :: 25
computer unauth. use/tamper :: 10
conspiracy 2, 1 :: 822
conspiracy 4, 3 :: 201
conspiracy 6, 5 :: 19
contempt,criminal :: 10028
controlled substance, intent to sell 5 :: 2816
controlled substance, possessi :: 5
controlled substance, possession 4 :: 1142
controlled substance, possession 5 :: 1659
controlled substance, possession 7 :: 43979
controlled substance, sale 4 :: 116
controlled substance, sale 5 :: 557
controlled substance,intent to sell 3 :: 17991
controlled substance,possess. 1 :: 1483
controlled substance,possess. 2 :: 1041
controlled substance,possess. 3 :: 391
controlled substance,possess. of procursers :: 14
controlled substance,sale 1 :: 370
controlled substance,sale 2 :: 363
controlled substance,sale 3 :: 12078
course of sexual conduct against a child :: 190
credit card,unlawful use of :: 14
criminal contempt 1 :: 1557
criminal disposal firearm 1 & :: 61
criminal disposal firearm 1 & 2 :: 58
criminal mischief 4th, graffiti :: 4909
custodial interference 1 :: 19
custodial interference 2 :: 36
dis. con.,aggravated :: 9
disorderly conduct subd 1,2,3,4,5,6,7 :: 2571
drug paraphernalia,   possesse :: 1
drug paraphernalia,   possesses or sells 1 :: 82
drug paraphernalia,   possesses or sells 2 :: 4160
drug, injection of :: 7
eavesdropping :: 10
endangering vulnerable elderly :: 38
enterprise corruption :: 154
escape 2,1 :: 56
escape 3 :: 35
exposure of a person :: 12
f.c.a. order of protection :: 1
f.o.a. non-support :: 3
fac. sexual offense w/controlled substance :: 1
facilitation 3,2,1, criminal :: 10
facilitation 4, criminal :: 116
false alarm fire :: 50
false report 1,fire :: 36
false report bomb :: 5
false report unclassified :: 982
fireworks prev conv 5 years :: 5
fireworks, possess/use :: 47
fireworks, sale :: 135
following too closely :: 7
forgery,etc.,unclassified-felony :: 17502
forgery,etc.-misd. :: 4019
forgery,m.v. registration :: 229
forgery,prescription :: 67
forgery-illegal possession,veh :: 14
forgery-illegal possession,vehicle ident. nu :: 241
fraud,unclassified-felony :: 579
fraud,unclassified-misdemeanor :: 28
fraud,unclassified-misdemeanor,part 1 :: 299
fraud,unclassified-misdemeanor-part 2 :: 2
fugitive,from other jurisdiction in ny state :: 87
fugitive,from other states :: 1188
gambling 1,promoting,bookmaking :: 92
gambling 1,promoting,policy :: 150
gambling 2, promoting, bookmaking :: 58
gambling 2, promoting, policy-lottery :: 131
gambling 2,promoting,unclassified :: 1618
gambling, device, possession :: 672
general business law / unclassified :: 36
general business law,unclassified :: 38
harassment,subd 1,civilian :: 136
harassment,subd 3,4,5 :: 107
health code,violation :: 417
healthcare/rent.reg. :: 23
homicide, negligent, vehicle, :: 14
homicide, negligent, vehicle, intox driver :: 3
homicide,negligent,unclassified :: 59
identity thft-1 :: 339
identity thft-2 :: 120
impaired driving, drugs :: 52
impaired driving,alcohol :: 87
impaired driving,drug :: 586
impersonation 1, police officer :: 203
impersonation 2, public servan :: 8
impersonation 2, public servant :: 3978
imprisonment 1,unlawful :: 150
imprisonment 2,unlawful :: 516
improper passing :: 5
incompetent person,knowingly endangering :: 93
incompetent person,recklessy endangering :: 100
intoxicated driving,alcohol :: 20888
jostling :: 126
kidnapping 1 :: 34
kidnapping 2 :: 50
larceny,grand by credit card use :: 51
larceny,grand by extortion :: 331
larceny,grand from building,unclassified :: 11
larceny,grand from open areas, :: 1016
larceny,grand from open areas,unclassified :: 23817
larceny,grand from person,unclassified :: 4162
larceny,grand of auto :: 3519
larceny,petit from open areas,unclassified :: 72950
leaving scene-accident-persona :: 1193
leaving scene-accident-prop. damage :: 369
lewdness,public :: 1672
licensing firearms :: 5
lights,improper :: 506
loitering 1st degree for drug purposes :: 32
loitering for prostitution or to patronize :: 338
loitering,gambling,other :: 75
loitering,masquerading :: 11
loitering,school :: 10
loitering,transportation facility :: 36
manslaughter,unclassified - non negligent :: 139
manufacture unauthorized recor :: 35
manufacture unauthorized recordings :: 58
marijuana, possession :: 1992
marijuana, possession 1, 2 & 3 :: 1605
marijuana, possession 4 & 5 :: 52631
marijuana, sale 1, 2 & 3 :: 396
marijuana, sale 4 & 5 :: 11578
material              offensive display :: 20
menacing 1st degree (vict not :: 225
menacing 1st degree (vict not peace officer) :: 305
menacing,unclassified :: 13341
mischief 1,criminal,explosive :: 46
mischief, criminal 3 & 2, of motor vehicle :: 206
mischief, criminal 4, by fire :: 40
mischief, criminal 4, of motor vehicle :: 76
mischief,criminal     unclassified 4th deg :: 13962
mischief,criminal,    uncl 2nd :: 7266
mischief,criminal,    uncl 2nd deg 3rd deg :: 3948
money laundering 1 & 2 :: 57
money laundering 3 :: 9
murder,unclassified :: 2633
noise,unecessary :: 124
nuisance, criminal :: 31
nuisance,criminal,unclassified :: 111
ny city,unclassified warrant :: 8
ny state laws,unclassified fel :: 679
ny state laws,unclassified felony :: 3372
ny state laws,unclassified mis :: 3
ny state laws,unclassified misdemeanor :: 8664
ny state laws,unclassified vio :: 81
ny state laws,unclassified violation :: 23483
ny state,parole :: 27
ny state,probation :: 2
ny state,unclassified :: 35
obscene material - under 17 ye :: 5
obscene material - under 17 years of age :: 307
obscenity 1 :: 50
obscenity, material 3 :: 5
obscenity, performance 3 :: 21
obstr breath/circul :: 10064
one-way street :: 40
parking,unclassified :: 45
parkr&r,unclassified violation :: 716
peddling,unlawful :: 399
pedestrian,unclassified :: 2
pedestrian,walk/dont walk :: 3
perjury 2,1,etc :: 62
perjury 3,etc. :: 208
possession anti-security item :: 94
possession hypodermic instrument :: 486
posting advertisements :: 4
privacy,offenses against,unclassified :: 3
promoting a sexual performance :: 13
promoting a sexual performance by a child :: 141
promoting suicide attempt :: 2
prostitution :: 3186
prostitution 1, under 11 :: 2
prostitution 2, compulsory :: 14
prostitution 2, under 16 :: 21
prostitution 3, promoting under 19 :: 67
prostitution 3,promoting busin :: 1
prostitution 3,promoting business :: 130
prostitution 4,promoting&securing :: 271
prostitution, patronizing 2, 1 :: 2
prostitution, patronizing 4, 3 :: 2844
prostitution,permitting :: 32
public administation,unclass m :: 24
public administation,unclass misdemean 4 :: 6191
public administration,unclassified felony :: 22527
public health law,unclassified misdemeanor :: 192
public safety,unclassified mis :: 102
public safety,unclassified misdemeanor :: 52
radio devices,unlawful possession :: 26
rape 1 :: 1384
rape 2 :: 286
rape 3 :: 582
reckless driving :: 1050
reckless endangerment 1 :: 2639
reckless endangerment 2 :: 3716
reckless endangerment of property :: 44
records,falsify-tamper :: 101
resisting arrest :: 10751
right of way,pedestrian :: 1
right of way,vehicle :: 8
riot 1 :: 60
riot 2/inciting :: 190
robbery,carjacking of mv other than truck :: 82
robbery,gas station :: 6
robbery,unclassified,open area :: 84
robbery,unclassified,open areas :: 30467
safety belts :: 45
sale of unauthorized recording :: 2
sale of unauthorized recordings :: 87
sale school grounds :: 1199
sale school grounds 4 :: 28
sales of prescription :: 13
sexual abuse 1 :: 771
sexual abuse 3,2 :: 3301
sexual misconduct,deviate :: 21
sexual misconduct,intercourse :: 182
signal,fail to :: 189
sodomy 1 :: 408
sodomy 2 :: 56
sodomy 3 :: 116
solicitation 3,2,1, criminal :: 1
solicitation 4, criminal :: 6
solicitation 5,criminal :: 1
speeding :: 38
spillback :: 5
stolen property 2,1,possession,unclassified :: 3117
stolen property 2,possession by licensed dea :: 14
stolen property 3,possession :: 3970
stolen property-motor veh 2nd, 1st possess :: 415
stop,fail to,on signal :: 141
strangulation 1st :: 5460
supp. act terrorism 2nd :: 1
tampering 1,criminal :: 2811
tampering 3,2, criminal :: 210
tampering with a witness :: 31
tax law :: 2037
terrorist threat :: 255
theft of services, unclassified :: 76903
theft of services- cable tv service :: 106
theft,related offenses,unclass :: 42
theft,related offenses,unclassified :: 231
traffic,unclassified infractio :: 494
traffic,unclassified infraction :: 15425
traffic,unclassified misdemean :: 45992
traffic,unclassified misdemeanor :: 10920
trespass 1,criminal :: 86
trespass 2, criminal :: 5711
trespass 3, criminal :: 17612
trespass 4,criminal :: 724
turn,improper :: 2
unauthorized use vehicle 2 :: 908
unauthorized use vehicle 3 :: 2514
unclassified :: 3
unlawful poss. weapon upon school grounds :: 2
unlawful sale synthetic marijuana :: 130
unlicensed operator :: 576
us code,unclassified :: 3064
use of a child in a sexual per :: 2
use of a child in a sexual performance :: 17
use of cellular telephone while driving :: 51
using slugs, 2nd :: 1
usury,criminal :: 6
vehicular assault (intox drive :: 151
violation of order of protecti :: 17
weapons possession 1 & 2 :: 9288
weapons possession 3 :: 10105
weapons, possession, etc :: 16489
weapons,disposition of :: 9
weapons,mfr,transport,etc. :: 58
weapons,prohibited use :: 15
weapons,prohibited use imitation pistol :: 1


"""

