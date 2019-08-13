create table users(
    username char(255) unique not null,
    password char(255) not null
);

insert into users(username, password) values ("admin", "password is including whitespace so you cannot login :p");
