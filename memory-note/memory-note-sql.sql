create database memory-note;
use memory-note;

drop table memory_note;

/* Create memory note table */
CREATE TABLE IF NOT EXISTS memory_note (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
note TEXT NOT NULL,
status INT(6) NOT NULL,
category INT(6) NOT NULL,
stage INT(6) NOT NULL,
odd_even VARCHAR(4),
week_day VARCHAR(10),
month_day VARCHAR(3),
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

/* Insert memory */
truncate table memory_note;
insert into memory_note(note, status, category, stage) values ("Test note 1", 1, 1, 1);
insert into memory_note(note, status, category, stage) values ("Test note 2", 1, 1, 1);
insert into memory_note(note, status, category, stage, odd_even) values ("Test note 3", 2, 2, 2, "Odd");
insert into memory_note(note, status, category, stage, odd_even) values ("Test note 4", 2, 2, 2, "Even");
insert into memory_note(note, status, category, stage) values ("Test note 5", 3, 3, 1);

/* id, note, status, category, stage, odd_even, week_day, month_day */
truncate table memory_note;
insert into memory_note(note, status, category, stage) values ("Test Stage 1", 1, 1, 1);
insert into memory_note(note, status, category, stage) values ("Test Stage 1", 1, 1, 1);
insert into memory_note(note, status, category, stage) values ("Test Stage 1", 1, 1, 1);
insert into memory_note(note, status, category, stage) values ("Test Stage 1", 1, 2, 1);

insert into memory_note(note, status, category, stage, odd_even) values ("Test Stage 2", 1, 1, 2, "Odd");
insert into memory_note(note, status, category, stage, odd_even) values ("Test Stage 2", 1, 1, 2, "Even");
insert into memory_note(note, status, category, stage, odd_even) values ("Test Stage 2", 1, 1, 2, "Even");
insert into memory_note(note, status, category, stage, odd_even) values ("Test Stage 2", 1, 2, 2, "Even");

insert into memory_note(note, status, category, stage, week_day) values ("Test Stage 3", 1, 1, 3, "Mon");
insert into memory_note(note, status, category, stage, week_day) values ("Test Stage 3", 1, 1, 3, "Tue");
insert into memory_note(note, status, category, stage, week_day) values ("Test Stage 3", 1, 1, 3, "Wed");
insert into memory_note(note, status, category, stage, week_day) values ("Test Stage 3", 1, 2, 3, "Wed");

insert into memory_note(note, status, category, stage, month_day) values ("Test Stage 4", 1, 1, 4, 10);
insert into memory_note(note, status, category, stage, month_day) values ("Test Stage 4", 1, 1, 4, 15);
insert into memory_note(note, status, category, stage, month_day) values ("Test Stage 4", 1, 1, 4, 22);
insert into memory_note(note, status, category, stage, month_day) values ("Test Stage 4", 1, 2, 4, 22);

select * from memory_note where category = 1 and stage = 4;
update memory_note set month_day = 28 where id = 15;


/* Create category table */
CREATE TABLE IF NOT EXISTS category (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
description VARCHAR(30) NOT NULL,
status INT(6) NOT NULL,
aud_create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
aud_modify_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

show tables;

/* Insert categories */
insert into category(description, status) values("Scripture", 2);
insert into category(description, status) values("Vocabulary", 2);
insert into category(description, status) values("Information Technology", 2);

select * from category;

/* Update category */
update category set description = "EIP" where id = 3;


/* Create status table */
CREATE TABLE IF NOT EXISTS status (
id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
description VARCHAR(30) NOT NULL,
aud_create_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
aud_modify_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

drop table status;

/* Insert status */
insert into status(description) values("Pending");
insert into status(description) values("Active");
insert into status(description) values("Deleted");

select * from status;




