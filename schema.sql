create table users
(
    full_name text,
    birthdate date,
    address   text,
    gender    text,
    id        integer generated always as identity
);

alter table users
    owner to postgres;

create unique index users_id_uindex
    on users (id);

create table phone_number
(
    user_id     integer,
    number_type text,
    number      text
);

alter table phone_number
    owner to postgres;

create unique index phone_number_user_id_uindex
    on phone_number (user_id);

create table email
(
    user_id integer,
    type    text,
    email   text
);

alter table email
    owner to postgres;

create unique index email_user_id_uindex
    on email (user_id);

