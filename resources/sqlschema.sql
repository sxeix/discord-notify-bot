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
	id int auto_increment not null, 
	userId int not null, 
	serverName varchar(255) not null, 
    spaces int default 3,
    keyString1 varchar(255),
    keyString2 varchar(255),
    keyString3 varchar(255),
	primary key (id), 
	foreign key (serverName) references Servers(serverName),
    foreign key (keyString1) references Strings(strValue),
    foreign key (keyString2) references Strings(strValue),
    foreign key (keyString3) references Strings(strValue)
);

insert into Servers (serverName) values ('first server');
insert into Servers (serverName) values ('second server');

insert into Strings (strValue) values ("test-string");
insert into Strings (strValue) values ("another-test-string");

insert into Users (userId, serverName, keyString1, spaces) values (20,"first server","test-string", 2);
insert into Users (userId, serverName, keyString1, spaces) values (21,"first server", "test-string", 2);
insert into Users (userId, serverName, keyString1, spaces) values (22,"second server","another-test-string", 2);
insert into Users (userId, serverName) values (20,"second server");

update Users set spaces = spaces + 1, keyString1 = null where userId = 20 and serverName = "first server" and keyString1 = "test-string";

select * from Users;