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

INSERT INTO Photo VALUES(
    "wizard",
    "wizard.png",
    "PNG",
    "2014-12-15"
);

INSERT INTO User VALUES(
    "sportslover",
    "Paul",
    "Walker",
    "sports",
    "sportslover@hotmail.com",
    "wizard"
);

INSERT INTO User VALUES(
    "traveler",
    "Rebecca",
    "Travolta",
    "traveler",
    "rebt@explorer.org",
    NULL
);

INSERT INTO User VALUES(
    "spacejunkie",
    "Bob",
    "Spacey",
    "space",
    "bspace@spacejunkies.net",
    NULL
);

INSERT INTO User VALUES(
    "fubUmich",
    "Binghong",
    "Fu",
    "19920725",
    "fub@umich.edu",
    "wizard"
)

INSERT INTO Album(title, created, lastupdated, username, coverid, access) VALUES(
    "I love sports",
    "2015-02-05",
    "2015-08-30",
    "sportslover",
    NULL,
    "public"
);

INSERT INTO Album(title, created, lastupdated, username, coverid, access) VALUES(
    "I love football",
    "2015-02-05",
    "2015-12-30",
    "sportslover",
    "football_s3",
    "public"
);

INSERT INTO Album(title, created, lastupdated, username, coverid, access) VALUES(
    "Around The World",
    "2014-05-12",
    "2016-01-01",
    "traveler",
    NULL,
    "public"
);

INSERT INTO Album(title, created, lastupdated, username, coverid, access) VALUES(
    "Cool Space Shots",
    "2013-08-24",
    "2015-01-02",
    "spacejunkie",
    "space_EagleNebula",
    "public"
);

INSERT INTO Contain(albumid, picid, caption) VALUES(
    2,
    "football_s1",
    "football s1"
);
