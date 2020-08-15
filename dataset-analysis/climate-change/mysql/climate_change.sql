show open tables where in_use>0; --See list of locked tables
show processlist; --see the list of the current processes, one of them is locking your table(s)
kill 80; --Kill one of these processes

show tables;

select * from climate_change LIMIT 10;
select count(*) from climate_change;
truncate climate_change;
drop table climate_change;

create index i_date on climate_change(date);
create index i_average_temperature on climate_change(average_temperature);
create index i_average_temperature_uncertainty on climate_change(average_temperature_uncertainty);
create index i_city on climate_change(city);
create index i_country on climate_change(country);
create index i_latitude on climate_change(latitude);
create index i_longitude on climate_change(longitude);

CREATE TABLE climate_change (
	id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
	date DATE,
	average_temperature DECIMAL(6, 3),
	average_temperature_uncertainty DOUBLE(20, 17),
	city VARCHAR(100),
	country VARCHAR(100),
	latitude VARCHAR(50),
	longitude VARCHAR(50)
);

/* Grouped by gender */
select count(ad.id) as cnt, ad.sex
from accidental_drug ad
group by ad.sex
order by cnt desc;

