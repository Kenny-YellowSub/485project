INSERT INTO User VALUES(
    "sportslover",
    "Paul",
    "Walker",
    NULL,
    "sportslover@hotmail.com"
);

INSERT INTO User VALUES(
    "traveler",
    "Rebecca",
    "Travolta",
    NULL,
    "rebt@explorer.org"
);

INSERT INTO User VALUES(
    "spacejunkie",
    "Bob",
    "Spacey",
    NULL,
    "bspace@spacejunkies.net"
);

INSERT INTO Photo VALUES(
    "football_s1",
    "football_s1.jpg",
    "JPG",
    "2015-12-30"
);

INSERT INTO Photo VALUES(
    "football_s2",
    "football_s2.jpg",
    "JPG",
    "2015-11-25"
);

INSERT INTO Photo VALUES(
    "football_s3",
    "football_s3.jpg",
    "JPG",
    "2015-11-25"
);

INSERT INTO Photo VALUES(
    "space_EagleNebula",
    "space_EagleNebula.jpg",
    "JPG",
    "2015-11-25"
);

INSERT INTO Album(title, created, lastupdated, username, coverid) VALUES(
    "I love sports",
    "2015-02-05",
    "2015-08-30",
    "sportslover",
    NULL
);

INSERT INTO Album(title, created, lastupdated, username, coverid) VALUES(
    "I love football",
    "2015-02-05",
    "2015-12-30",
    "sportslover",
    "football_s3"
);

INSERT INTO Album(title, created, lastupdated, username, coverid) VALUES(
    "Around The World",
    "2014-05-12",
    "2016-01-01",
    "traveler",
    NULL
);

INSERT INTO Album(title, created, lastupdated, username, coverid) VALUES(
    "Cool Space Shots",
    "2013-08-24",
    "2015-01-02",
    "spacejunkie",
    "space_EagleNebula"
);

INSERT INTO Contain(albumid, picid, caption) VALUES(
    2,
    "football_s1",
    "football s1"
);
