drop table if exists Users;
drop table if exists Servers;
drop table if exists Strings;

create table Servers (
	serverName varchar(255) not null,
	primary key (serverName)
);

create table Strings (
	strValue varchar(255) not null,
    primary key (strValue)
);

create table Users (
	id varchar(255) not null, 
	userId varchar(255) not null, 
	serverName varchar(255) not null, 
    keyString varchar(255) not null,
	primary key (id) 
-- 	foreign key (serverName) references Servers(serverName),
--     foreign key (keyString) references Strings(strValue)
);

-- insert into Servers (serverName) values ('first server');
-- insert into Servers (serverName) values ('second server');

-- insert into Strings (strValue) values ("test-string");
-- insert into Strings (strValue) values ("another-test-string");

insert into Users (id, userId, serverName, keyString) values ("20first server",20,"first server","test-string");
insert into Users (id, userId, serverName, keyString) values ("21first server",21,"first server", "test-string");
insert into Users (id, userId, serverName, keyString) values ("22second server",22,"second server","another-test-string");
insert into Users (id, userId, serverName, keyString) values ("20second server",20,"second server", "something");

-- insert into Users (userId, serverName, keyString) values (22,"second server","another-test-string2") ON DUPLICATE KEY UPDATE userId=22 and serverName="second server";
replace into Users (id, userId, serverName, keyString) values ("22second server", 22,"second server","another-test-string2");
-- insert ignore into Users (id, userId, serverName, keyString) values ("22second server", 22,"second server","another-test-string2");


select keyString from Users where serverName="first server";

-- select userId, strValue from Users, Strings where Strings.strValue = Users.keyString;