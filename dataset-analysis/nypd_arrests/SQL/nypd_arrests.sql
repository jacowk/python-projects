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
	arrest_key INT(9),
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