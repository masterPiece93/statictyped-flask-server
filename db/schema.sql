DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS notes;

CREATE TABLE user (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    username    TEXT NOT NULL,
    firstname   TEXT NOT NULL,
    lastname    TEXT NOT NULL,
    age         INTEGER,
    email       TEXT NOT NULL,
    created     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by  INTEGER
);

CREATE TABLE notes (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT NOT NULL,
    content     TEXT NOT NULL,
    created     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by  INTEGER NOT NULL,

    FOREIGN KEY(created_by) REFERENCES user(id)
);
