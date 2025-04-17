-- Faculty

INSERT INTO Faculty (NAME, auth_level, email, PASSWORD) VALUES ("Kuperman Vladimir", 2, "email1@albany.edu", "kup123");

INSERT INTO Faculty (NAME, auth_level, email, PASSWORD) VALUES ("Hono II Daniel", 2, "email2@albany.edu", "hon123");

INSERT INTO Faculty (NAME, auth_level, email, PASSWORD) VALUES ("Arora Shashank", 2, "email3@albany.edu", "aro123");

INSERT INTO Faculty (NAME, auth_level, email, PASSWORD) VALUES ("Knuth Kevin", 3, "email4@albany.edu", "knu123");

INSERT INTO Faculty (NAME, auth_level, email, PASSWORD) VALUES ("Offutt Jeff", 5, "email5@albany.edu", "off123");




-- Courses

INSERT INTO Course VALUES (3402, "ICSI 201", 1, "Intro Comp Sci", 80, "13:30", "14:50", True);

INSERT INTO Course VALUES (3403, "ICSI 201", 1, "Intro Comp Sci", 55, "9:30", "10:25", False);

INSERT INTO Course VALUES (8722, "ICSI 201", 2, "Intro Comp Sci", 80, "15:00", "16:20", False);

INSERT INTO Course VALUES (8724, "ICSI 201", 2, "Intro Comp Sci", 55, "9:30", "10:25", False);

INSERT INTO Course VALUES (6371, "ICSI 213", 3, "Data Structures", 80, "9:00", "10:20", True);

INSERT INTO Course VALUES (9324, "ICSI 213", 3, "Data Structures", 80, "18:00", "19:20", False);

INSERT INTO Course VALUES (4038, "ICSI 451", 4, "Bayesian Data Analy/Signal Pro", 80, "10:30", "11:50", False);

INSERT INTO Course VALUES (5774, "ICSI 418", 3, "Software Engineering", 80, "13:30", "14:50", False);


-- Course Days

INSERT INTO Course_Days VALUES (3402, "T,TH");

INSERT INTO Course_Days VALUES (3403, "M");

INSERT INTO Course_Days VALUES (8722, "M,W");

INSERT INTO Course_Days VALUES (8724, "F");

INSERT INTO Course_Days VALUES (6371, "T,TH");

INSERT INTO Course_Days VALUES (9324, "M");

INSERT INTO Course_Days VALUES (4038, "T,TH");

INSERT INTO Course_Days VALUES (5774, "T,TH");


-- Coreqs

INSERT INTO Coreqs VALUES (3402, 3403);

INSERT INTO Coreqs VALUES (8722, 8724);

-- Prereqs

INSERT INTO Prereqs VALUES ("ICSI 201", "ICSI 213");

INSERT INTO Prereqs VALUES ("ICSI 201", "ICSI 451");


-- Conflict Numbers

INSERT INTO Conflict_no VALUES ("ICSI 201", 0);
INSERT INTO Conflict_no VALUES ("ICSI 213", 1);
INSERT INTO Conflict_no VALUES ("ICSI 451", 2);
INSERT INTO Conflict_no VALUES ("ICSI 418", 4);
INSERT INTO Conflict_no VALUES ("ICSI 213", 4);


-- Comments

INSERT INTO Comment (CRN, fid, time_posted, comment_text) VALUES (3402, 1, TIMESTAMP ("2025-04-01",  "12:00:00"), "This is my course");

INSERT INTO Comment (CRN, fid, time_posted, comment_text) VALUES (6371, 2, TIMESTAMP ("2025-04-02",  "15:15:00"), "This is NOT my course");


-- Configuration

INSERT INTO Configuration (travel_time) VALUES (30);


-- Configured By

INSERT INTO Configured_by VALUES (1, 5);


-- Preferred Days

INSERT INTO Preferred_Days VALUES (1, "M,W");
INSERT INTO Preferred_Days VALUES (1, "T,TH");


-- Preferred Start Times

INSERT INTO Preferred_Start_Times VALUES (1, "9:00");
INSERT INTO Preferred_Start_Times VALUES (1, "9:30");

INSERT INTO Preferred_Start_Times VALUES (1, "13:30");
INSERT INTO Preferred_Start_Times VALUES (1, "15:00");
INSERT INTO Preferred_Start_Times VALUES (1, "18:00");


