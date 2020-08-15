show open tables where in_use>0; --See list of locked tables
show processlist; --see the list of the current processes, one of them is locking your table(s)
kill 80; --Kill one of these processes

show tables;

select * from accidental_drug LIMIT 10;
select count(*) from accidental_drug;
truncate accidental_drug;
drop table accidental_drug;

create index i_race on accidental_drug(race);

CREATE TABLE accidental_drug (
	drug_id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	id VARCHAR(9),
    ddate DATETIME,
    datetype VARCHAR(50),
    age INT(2),
    sex VARCHAR(50),
    race VARCHAR(50),
    residencecity VARCHAR(100),
    residencecounty VARCHAR(100),
    residencestate VARCHAR(5),
    deathcity VARCHAR(50),
    deathcounty VARCHAR(50),
    location VARCHAR(100),
    locationifother VARCHAR(100),
    descriptionofinjury VARCHAR(100),
    injuryplace VARCHAR(50),
    injurycity VARCHAR(100),
    injurycounty VARCHAR(100),
    injurystate VARCHAR(50),
    cod VARCHAR(200),
    othersignifican VARCHAR(100),
    heroin TINYINT(1),
    cocaine TINYINT(1),
    fentanyl TINYINT(1),
    fentanylanalogue TINYINT(1),
    oxycodone TINYINT(1),
    oxymorphone TINYINT(1),
    ethanol TINYINT(1),
    hydrocodone TINYINT(1),
    benzodiazepine TINYINT(1),
    methadone TINYINT(1),
    amphet TINYINT(1),
    tramad TINYINT(1),
    morphine_notheroin TINYINT(1),
    hydromorphone TINYINT(1),
    other  TINYINT(1),
    opiatenos TINYINT(1),
    anyopioid TINYINT(1),
    mannerofdeath VARCHAR(200),
    deathcitygeo VARCHAR(200),
	residencecitygeo VARCHAR(200),
    injurycitygeo VARCHAR(200)
);

insert into accidental_drug(id, ddate, datetype, age, sex, race, residencecity, residencecounty, residencestate, deathcity, deathcounty, location, locationifother, descriptionofinjury, injuryplace, injurycity, injurycounty, injurystate, cod, othersignifican, heroin, cocaine, fentanyl, fentanylanalogue, oxycodone, oxymorphone, ethanol, hydrocodone, benzodiazepine, methadone, amphet, tramad, morphine_notheroin, hydromorphone, other, opiatenos, anyopioid, mannerofdeath, deathcitygeo, residencecitygeo, injurycitygeo)
values ('13-0102','2013-03-21 12:00:00','DateofDeath',48,'Male','Black','NORWALK','','','NORWALK','FAIRFIELD','Hospital','','','','','','','Cocaine Intoxication','',false,true,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,'Accident','Norwalk, CT(41.11805, -73.412906)','NORWALK, CT(41.11805, -73.412906)','CT(41.575155, -72.738288)');

select * from accidental_drug where id = '14-0273';
select count(*) from accidental_drug;
truncate table accidental_drug;

insert into accidental_drug(id, ddate, datetype, age, sex, race, residencecity, residencecounty, residencestate, deathcity, deathcounty, location, locationifother, descriptionofinjury, injuryplace, injurycity, injurycounty, injurystate, cod, othersignifican, heroin, cocaine, fentanyl, fentanylanalogue, oxycodone, oxymorphone, ethanol, hydrocodone, benzodiazepine, methadone, amphet, tramad, morphine_notheroin, hydromorphone, other, opiatenos, anyopioid, mannerofdeath, deathcitygeo, residencecitygeo, injurycitygeo) 
values ('18-1009','2018-12-28 12:00:00','DateofDeath',24,'Male','White','SOUTHWICK','HAMPDEN','MA','WETHERSFIELD','HARTFORD','Other','','Substance Abuse','Friends Residence','','','','Acute Intoxication due to the Combined Effects of Acetyl Fentanyl Fentanyl and Mitragynine','',0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,'Accident','WETHERSFIELD| CT(41.712487| -72.663607)','SOUTHWICK| CT(41.984699| -72.516098)','CT(41.575155| -72.738288)');

insert into accidental_drug(id, ddate, datetype, age, sex, race, residencecity, residencecounty, residencestate, deathcity, deathcounty, location, locationifother, descriptionofinjury, injuryplace, injurycity, injurycounty, injurystate, cod, othersignifican, heroin, cocaine, fentanyl, fentanylanalogue, oxycodone, oxymorphone, ethanol, hydrocodone, benzodiazepine, methadone, amphet, tramad, morphine_notheroin, hydromorphone, other, opiatenos, anyopioid, mannerofdeath, deathcitygeo, residencecitygeo, injurycitygeo) 
values ('16-0134','2016-02-27 12:00:00','DateofDeath',64,'Male','White','STRATFORD','FAIRFIELD','CT','MILFORD','','Other','Friends Residence','substance abuse','Friends Residence','MILFORD','','','Cocaine Heroin and Alcohol Intoxication','',1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,'Accident','MILFORD| CT(41.224276| -73.057564)','STRATFORD| CT(41.200888| -73.131323)','MILFORD| CT(41.224276| -73.057564)');

insert into accidental_drug(id, ddate, datetype, age, sex, race, residencecity, residencecounty, residencestate, deathcity, deathcounty, location, locationifother, descriptionofinjury, injuryplace, injurycity, injurycounty, injurystate, cod, othersignifican, heroin, cocaine, fentanyl, fentanylanalogue, oxycodone, oxymorphone, ethanol, hydrocodone, benzodiazepine, methadone, amphet, tramad, morphine_notheroin, hydromorphone, other, opiatenos, anyopioid, mannerofdeath, deathcitygeo, residencecitygeo, injurycitygeo) 
values ('18-1009','2018-12-28 12:00:00','DateofDeath',24,'Male','White','SOUTHWICK','HAMPDEN','MA','WETHERSFIELD','HARTFORD','Other','','Substance Abuse','Friends Residence','','','','Acute Intoxication due to the Combined Effects of Acetyl Fentanyl Fentanyl and Mitragynine','',0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,'Accident','WETHERSFIELD| CT(41.712487| -72.663607)','SOUTHWICK| CT(41.984699| -72.516098)','CT(41.575155| -72.738288)');

insert into accidental_drug(id, ddate, datetype, age, sex, race, residencecity, residencecounty, residencestate, deathcity, deathcounty, location, locationifother, descriptionofinjury, injuryplace, injurycity, injurycounty, injurystate, cod, othersignifican, heroin, cocaine, fentanyl, fentanylanalogue, oxycodone, oxymorphone, ethanol, hydrocodone, benzodiazepine, methadone, amphet, tramad, morphine_notheroin, hydromorphone, other, opiatenos, anyopioid, mannerofdeath, deathcitygeo, residencecitygeo, injurycitygeo) 
values ('16-0134','2016-02-27 12:00:00','DateofDeath',64,'Male','White','STRATFORD','FAIRFIELD','CT','MILFORD','','Other','Friends Residence','substance abuse','Friends Residence','MILFORD','','','Cocaine Heroin and Alcohol Intoxication','',1,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,'Accident','MILFORD| CT(41.224276| -73.057564)','STRATFORD| CT(41.200888| -73.131323)','MILFORD| CT(41.224276| -73.057564)');


/* Grouped by gender */
select count(ad.id) as cnt, ad.sex
from accidental_drug ad
group by ad.sex
order by cnt desc;

/* Grouped by race */
select count(ad.id) as cnt, ad.race
from accidental_drug ad
group by ad.race
order by cnt desc;

/* Grouped by race and gender */
select count(ad.id) as cnt, ad.race
from accidental_drug ad
where ad.sex like 'Male'
group by ad.race
order by cnt desc;


/* How many people use heroine */
select count(ad.id) as cnt, ad.heroin
from accidental_drug ad
where ad.heroin = true
group by ad.heroin
order by cnt desc;


/* Grouped by deathcity */
select count(ad.id) as cnt, ad.deathcity
from accidental_drug ad
group by ad.deathcity
order by cnt desc;

/* Grouped by residencecounty */
select count(ad.id) as cnt, ad.residencecounty, ad.race
from accidental_drug ad
group by ad.residencecounty, ad.race
order by ad.residencecounty desc, cnt desc;

/* Grouped by residencecounty, by race */
select count(ad.id) as cnt, ad.residencecounty
from accidental_drug ad
where ad.race like 'Black'
group by ad.residencecounty, ad.race
having count(ad.id) > 100
order by cnt desc;


/* Grouped by location */
select count(ad.id) as cnt, ad.location
from accidental_drug ad
group by ad.location
order by cnt desc;

/* Grouped by injurystate */
select count(ad.id) as cnt, ad.injurystate
from accidental_drug ad
group by ad.injurystate
order by cnt desc;

/* Grouped by descriptionofinjury */
select count(ad.id) as cnt, ad.descriptionofinjury
from accidental_drug ad
group by ad.descriptionofinjury
order by cnt desc;

/* Grouped by age */
select count(ad.id) as cnt, ad.age
from accidental_drug ad
where ad.race like 'Black'
group by ad.age
order by cnt desc
limit 10;

select * from accidental_drug ad;


/* All drugs */
select count(ad.id) as cnt, 
ad.heroin, 
ad.cocaine,
ad.fentanyl,
ad.fentanylanalogue,
ad.oxycodone,
ad.oxymorphone,
ad.ethanol,
ad.hydrocodone,
ad.benzodiazepine,
ad.methadone,
ad.amphet,
ad.tramad,
ad.morphine_notheroin,
ad.hydromorphone,
ad.other,
ad.opiatenos,
ad.anyopioid
from accidental_drug ad
where ad.race = 'Black'
and (ad.heroin = true
or ad.heroin = true
or ad.cocaine = true
or ad.fentanyl = true
or ad.fentanylanalogue = true
or ad.oxycodone = true
or ad.oxymorphone = true
or ad.ethanol = true
or ad.hydrocodone = true
or ad.benzodiazepine = true
or ad.methadone = true
or ad.amphet = true
or ad.tramad = true
or ad.morphine_notheroin = true
or ad.hydromorphone = true
or ad.other = true
or ad.opiatenos = true
or ad.anyopioid = true)
group by ad.heroin, ad.cocaine,
ad.fentanyl,
ad.fentanylanalogue,
ad.oxycodone,
ad.oxymorphone,
ad.ethanol,
ad.hydrocodone,
ad.benzodiazepine,
ad.methadone,
ad.amphet,
ad.tramad,
ad.morphine_notheroin,
ad.hydromorphone,
ad.other,
ad.opiatenos,
ad.anyopioid
order by cnt desc;
