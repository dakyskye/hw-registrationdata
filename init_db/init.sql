CREATE TABLE cities
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR(32) UNIQUE NOT NULL
);

CREATE TABLE users
(
    id         CHAR(11) PRIMARY KEY CHECK ( length(id) = 11 ),
    first_name VARCHAR(32)     NOT NULL,
    last_name  VARCHAR(32)     NOT NULL,
    age        INT             NOT NULL CHECK ( age > 0 ),
    city       BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (city) REFERENCES cities (id)
);