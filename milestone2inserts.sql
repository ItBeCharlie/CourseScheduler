# Faculty

INSERT INTO Faculty (0, "Kuperman Vladimir", 2, "email1@albany.edu", "kup123");

INSERT INTO Faculty (1, "Hono II Daniel", 2, "email2@albany.edu", "hon123");

INSERT INTO Faculty (2, "Arora Shashank", 2, "email3@albany.edu", "aro123");

INSERT INTO Faculty (16, "Knuth Kevin", 3, "email4@albany.edu", "knu123");

INSERT INTO Faculty (29, "Offutt Jeff", 5, "email5@albany.edu", "off123");




# Courses

INSERT INTO Course (3402, "ICSI 201", 0, "Intro Comp Sci", 80, "13:30", "14:50", True);

INSERT INTO Course (3403, "ICSI 201", 0, "Intro Comp Sci", 55, "9:30", "10:25", False);

INSERT INTO Course (8722, "ICSI 201", 1, "Intro Comp Sci", 80, "15:00", "16:20", False);

INSERT INTO Course (8724, "ICSI 201", 1, "Intro Comp Sci", 55, "9:30", "10:25", False);

INSERT INTO Course (6371, "ICSI 213", 2, "Data Structures", 80, "9:00", "10:20", True);

INSERT INTO Course (9324, "ICSI 213", 2, "Data Structures", 80, "18:00", "19:20", False);

INSERT INTO Course (4038, "ICSI 451", 16, "Bayesian Data Analy/Signal Pro", 80, "10:30", "11:50", False);

INSERT INTO Course (5774, "ICSI 418", 2, "Software Engineering", 80, "13:30", "14:50", False);


# Course Days

INSERT INTO Course_Days (3402, "T,TH");

INSERT INTO Course_Days (3403, "M");

INSERT INTO Course_Days (8722, "M,W");

INSERT INTO Course_Days (8724, "F");

INSERT INTO Course_Days (6371, "T,TH");

INSERT INTO Course_Days (9324, "M");

INSERT INTO Course_Days (4038, "T,TH");

INSERT INTO Course_Days (5774, "T,TH");


# Coreqs

INSERT INTO Coreqs (3402, 3403);

INSERT INTO Coreqs (8722, 8724);

# Prereqs

INSERT INTO Prereqs ("ICSI 201", "ICSI 213");

INSERT INTO Prereqs ("ICSI 201", "ICSI 451");


# Conflict Numbers

INSERT INTO Conflict_no ("ICSI 201", 0);
;INSERT INTO Conflict_no ("ICSI 213", 1)
INSERT INTO Conflict_no ("ICSI 451", 2);
INSERT INTO Conflict_no ("ICSI 418", 4);
INSERT INTO Conflict_no ("ICSI 213", 4);


# Comments

INSERT INTO Comment (0, 3402, 0, TIMESTAMP("2025-04-01",  "12:00:00"), "This is my course");

INSERT INTO Comment (0, 6371, 1, TIMESTAMP("2025-04-02",  "15:15:00"), "This is NOT my course");


# Configuration

INSERT INTO Configuration (0, 30);


# Configured By

INSERT INTO Configured_by (0, 29);


# Preferred Days

INSERT INTO Preferred_Days (0, "M,W");
INSERT INTO Preferred_Days (0, "T,TH");


# Preferred Start Times

INSERT INTO Preferred_Start_Times (0, "9:00");
INSERT INTO Preferred_Start_Times (0, "9:30");

INSERT INTO Preferred_Start_Times (0, "13:30");
INSERT INTO Preferred_Start_Times (0, "15:00");
INSERT INTO Preferred_Start_Times (0, "18:00");


