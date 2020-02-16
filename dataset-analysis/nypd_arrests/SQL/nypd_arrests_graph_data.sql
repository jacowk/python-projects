/* No of arrests per race, per gender, per age group */
select count(na.id) as cnt, na.age_group 
from nypd_arrests_2015 na
where na.perp_sex = 'F'
group by na.age_group
order by cnt desc;


/* No of male and female arrests */
select count(na.id) as cnt, na.perp_sex
from nypd_arrests_2015 na
group by na.perp_sex;

/* No of arrests per race */
select count(na.id) as cnt, na.perp_race
from nypd_arrests_2015 na
group by na.perp_race
order by cnt desc;

/* No of arrests per arrest date */
select count(na.id) as cnt, na.arrest_date
from nypd_arrests_2015 na
group by na.arrest_date
order by cnt desc;

/* No of arrests per race, per gender */
select count(na.id) as cnt, na.perp_sex, na.perp_race
from nypd_arrests_2015 na
group by na.perp_sex, na.perp_race
order by cnt desc;

/* No of arrests per race, per gender, per age group */
select count(na.id) as cnt, na.perp_sex, na.perp_race, na.age_group 
from nypd_arrests_2015 na
group by na.perp_sex, na.perp_race, na.age_group
order by cnt desc;

/* No of arrests per race, per gender, per age group - with specific criteria */
select count(na.id) as cnt, na.perp_sex, na.perp_race, na.age_group 
from nypd_arrests_2015 na
where na.perp_sex = 'M'
and na.perp_race = 'BLACK'
group by na.perp_sex, na.perp_race, na.age_group
order by cnt desc;

/* No of arrests per race, per gender, per age group, per pd_cd */
select count(na.id) as cnt, na.perp_sex, na.perp_race, na.age_group, na.pd_cd, na.pd_desc
from nypd_arrests_2015 na
where na.perp_sex = 'M'
and na.perp_race = 'WHITE'
and na.age_group = '18-24'
group by na.perp_sex, na.perp_race, na.age_group, na.pd_cd, na.pd_desc
order by cnt desc
limit 10;

511	CONTROLLED SUBSTANCE, POSSESSION 7
567	MARIJUANA, POSSESSION 4 & 5
478	THEFT OF SERVICES, UNCLASSIFIED
339	LARCENY,PETIT FROM OPEN AREAS,UNCLASSIFIED
101	ASSAULT 3
849	NY STATE LAWS,UNCLASSIFIED VIOLATION
782	WEAPONS, POSSESSION, ETC
922	TRAFFIC,UNCLASSIFIED MISDEMEAN
503	CONTROLLED SUBSTANCE,INTENT TO SELL 3
258	CRIMINAL MISCHIEF 4TH, GRAFFITI


/* No of arrests per race, per gender, per age group, per pd_cd */
select count(na.id) as cnt, na.perp_sex, na.perp_race, na.age_group, na.pd_cd, na.pd_desc
from nypd_arrests_2015 na
where na.perp_sex = 'M'
and na.perp_race = 'WHITE'
--and (na.perp_race = 'WHITE' or na.perp_race = 'BLACK')
and na.pd_cd = 258
group by na.perp_sex, na.perp_race, na.age_group, na.pd_cd, na.pd_desc
order by cnt desc;

/*
<18
18-24
25-44
45-64
65+
*/

select * from nypd_arrests_2015 na limit 10;
select distinct na.age_group from nypd_arrests_2015 na;
