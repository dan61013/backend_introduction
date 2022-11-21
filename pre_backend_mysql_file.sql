CREATE SCHEMA sql_test;
show databases;
use sql_test;
CREATE Table `Bboy`(
	`Name` VARCHAR(30),
    `Age` INT,
    `Skills` VARCHAR(1000)
);
show databases;
describe `Bboy`;
ALTER TABLE `Bboy` ADD `Crew` VARCHAR(100);
ALTER TABLE `Bboy` DROP COLUMN `Crew`;
DROP TABLE `Bboy`;
insert into `Bboy` values('Dan', 27, 'Windmill', '無團隊');
insert into `Bboy` values('Ken', 22, 'Flare', 'Test001');
select * from `Bboy`;
select `Name`, `Crew` from `Bboy`;
select * from `Bboy` where `Name`='Dan';
set SQL_safe_updates=0;
update `Bboy` set `Crew`='無團隊';
update `Bboy` set `Name`='David' where `name`='Ken';
CREATE Table `Bboy_Not_Null`(
	`Name` VARCHAR(30) NOT NULL,
    `Age` INT
);
describe Bboy_Not_Null;
insert into `Bboy_Not_Null` values('Ben', '23');
SELECT * FROM `Bboy_Not_Null`;
ALTER table `Bboy_Not_Null` ADD `Code` INT UNIQUE;
update `Bboy_Not_Null` set `Code`='1' where `name`='Ben';
use `Bboy_test`;
describe `Bboy_list`;
SELECT * from `Bboy_list`;