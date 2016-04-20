CREATE TABLE Photo(
    picid       VARCHAR(40),
    path        VARCHAR(255) NOT NULL,
    format      CHAR(3) NOT NULL,
    date        DATE,
    CONSTRAINT pk_picid PRIMARY KEY(picid)
);

CREATE TABLE User(
    username    VARCHAR(20),
    firstname   VARCHAR(20),
    lastname    VARCHAR(20),
    password    VARCHAR(20) NOT NULL,
    email       VARCHAR(40),
    avatar      VARCHAR(40),
    CONSTRAINT pk_username PRIMARY KEY(username),
    CONSTRAINT fk_avatar FOREIGN KEY(avatar) REFERENCES Photo(picid)
        ON DELETE SET NULL
);

CREATE TABLE Album(
    albumid     INTEGER NOT NULL AUTO_INCREMENT,
    title       VARCHAR(50),
    created     DATE,
    lastupdated DATE,
    username    VARCHAR(20),
    coverid     VARCHAR(40),
    access      VARCHAR(7) NOT NULL,
    CONSTRAINT pk_albumid PRIMARY KEY(albumid),
    CONSTRAINT fk_username FOREIGN KEY(username) REFERENCES User(username)
        ON DELETE CASCADE,
    CONSTRAINT fk_coverid FOREIGN KEY(coverid) REFERENCES Photo(picid)
        ON DELETE SET NULL,
    CONSTRAINT ck_access CHECK(access='public' OR access='private')
);

CREATE TABLE Contain(
    albumid     INTEGER,
    picid       VARCHAR(40),
    caption     VARCHAR(255),
    sequencenum INTEGER,
    CONSTRAINT pk_albumid_picid PRIMARY KEY(albumid, picid),
    CONSTRAINT fk_albumid FOREIGN KEY(albumid) REFERENCES Album(albumid)
        ON DELETE CASCADE,
    CONSTRAINT fk_picid FOREIGN KEY(picid) REFERENCES Photo(picid)
        ON DELETE CASCADE
);

CREATE TABLE AlbumAccess(
    username    VARCHAR(40),
    albumid     INTEGER,
    CONSTRAINT pk_username_albumid PRIMARY KEY(username, albumid),
    CONSTRAINT fk_username_albumaccess FOREIGN KEY(username) REFERENCES User(username)
        ON DELETE CASCADE,
    CONSTRAINT fk_albumid_albumaccess FOREIGN KEY(albumid) REFERENCES Album(albumid)
        ON DELETE CASCADE
);