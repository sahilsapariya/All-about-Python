drop table if exists users;

create table users (
    id text primary key,
    username text not null,
    password text not null
);