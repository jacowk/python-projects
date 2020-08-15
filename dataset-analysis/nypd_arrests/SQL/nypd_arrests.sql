show open tables where in_use>0; --See list of locked tables
show processlist; --see the list of the current processes, one of them is locking your table(s)
kill 80; --Kill one of these processes


show tables;

select * from nypd_arrests_2015 LIMIT 10;
select * from nypd_arrests_2016 LIMIT 10;
select count(*) from nypd_arrests_2017;
truncate nypd_arrests_2015;
drop table nypd_arrests_2015;

create index i_arrest_key on nypd_arrests_2015(arrest_key);
create index i_arrest_key on nypd_arrests_2016(arrest_key);
create index i_arrest_key on nypd_arrests_2017(arrest_key);

create index i_arrest_year on nypd_arrests_2015(arrest_year);
create index i_arrest_year on nypd_arrests_2016(arrest_year);
create index i_arrest_year on nypd_arrests_2017(arrest_year);

create index i_pd_cd on nypd_arrests_2015(pd_cd);
create index i_pd_cd on nypd_arrests_2016(pd_cd);
create index i_pd_cd on nypd_arrests_2017(pd_cd);

create index i_age_group on nypd_arrests_2015(age_group);
create index i_age_group on nypd_arrests_2016(age_group);
create index i_age_group on nypd_arrests_2017(age_group);

create index i_perp_sex on nypd_arrests_2015(perp_sex);
create index i_perp_sex on nypd_arrests_2016(perp_sex);
create index i_perp_sex on nypd_arrests_2017(perp_sex);

create index i_perp_race on nypd_arrests_2015(perp_race);
create index i_perp_race on nypd_arrests_2016(perp_race);
create index i_perp_race on nypd_arrests_2017(perp_race);

CREATE TABLE nypd_arrests_2017 (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	id VARCHAR(10),
	arrest_date DATE,
	arrest_year INT(4),
	pd_cd INT(3),
	pd_desc VARCHAR(50),
	ky_cd INT(3),
	ofns_desc VARCHAR(50),
	law_code VARCHAR(10),
	law_cat_cd VARCHAR(1),
	arrest_boro VARCHAR(1),
	arrest_precinct INT(3),
	jurisdiction_code INT(1),
	age_group VARCHAR(5),
	perp_sex VARCHAR(1),
	perp_race VARCHAR(30),
	x_coord_cd DECIMAL(30, 20),
	y_coord_cd DECIMAL(30, 20),
	latitude DECIMAL(30, 20),
	longitude DECIMAL(30, 20)
);

ID:  14-0273
Date:  06/28/2014 12:00:00 AM
DateType:  DateReported
Age:
Sex:
Race:
ResidenceCity:
ResidenceCounty:
ResidenceState:
DeathCity:
DeathCounty:
Location:
LocationifOther:
DescriptionofInjury:  substance
InjuryPlace:
InjuryCity:
InjuryCounty:
InjuryState:
COD:  Acute fent, hydrocod, benzodiazepine
OtherSignifican:
Heroin:
Cocaine:
Fentanyl:  Y
FentanylAnalogue:
Oxycodone:
Oxymorphone:
Ethanol:
Hydrocodone:  Y
Benzodiazepine:  Y
Methadone:
Amphet:
Tramad:
Morphine_NotHeroin:
Hydromorphone:
Other:
OpiateNOS:
AnyOpioid:
MannerofDeath:  Accident
DeathCityGeo:  CT
(41.575155, -72.738288)
ResidenceCityGeo:  CT
(41.575155, -72.738288)
InjuryCityGeo:  CT
(41.575155, -72.738288)


Press any key to continue, or 'q' to quite...