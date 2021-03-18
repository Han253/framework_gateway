DROP TABLE IF EXISTS device;
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS service;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
);

CREATE TABLE device(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    tagGlobal TEXT UNIQUE NOT NULL,
    device_name TEXT NOT NULL,
    device_description TEXT
);

CREATE TABLE service(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    service_name TEXT UNIQUE NOT NULL,
    service_description TEXT
);

