-- 1. Faculty
CREATE TABLE Faculty (
    fid INT,
    NAME VARCHAR(100),
    auth_level VARCHAR(50),
    email VARCHAR(100) UNIQUE,
    PASSWORD VARCHAR(100),
    PRIMARY KEY (fid)
);

-- 2. Course 
CREATE TABLE Course (
    CRN INT,
    course_code VARCHAR(20),
    fid INT NOT NULL,
    NAME VARCHAR(100),
    duration INT,
    start_time TIME,
    end_time TIME,
    is_pinned BOOLEAN,
    PRIMARY KEY (CRN),
    FOREIGN KEY (fid) REFERENCES Faculty(fid),
);

-- 3. Course_Days
CREATE TABLE Course_Days (
    CRN INT,
    days VARCHAR(10),
    PRIMARY KEY (CRN),
    FOREIGN KEY (CRN) REFERENCES Course(CRN)
);

-- 4. Conflict_no
CREATE TABLE Conflict_no (
    course_code VARCHAR(20),
    conflict_no INT,
    PRIMARY KEY (course_code),
    FOREIGN KEY (course_code) REFERENCES Course(course_code)
);

-- 5. Coreqs
CREATE TABLE Coreqs (
    CRN1 INT,
    CRN2 INT,
    PRIMARY KEY (CRN1, CRN2),
    FOREIGN KEY (CRN1) REFERENCES Course(CRN),
    FOREIGN KEY (CRN2) REFERENCES Course(CRN)
);

-- 6. Prereqs
CREATE TABLE Prereqs (
    prereq_course_code VARCHAR(20),
    course_code VARCHAR(20),
    PRIMARY KEY (prereq_course_code, course_code),
    FOREIGN KEY (prereq_course_code) REFERENCES Course(course_code),
    FOREIGN KEY (course_code) REFERENCES Course(course_code)
);

-- 7. Comment
CREATE TABLE Comment (
    cid INT,
    CRN INT,
    fid INT,
    time_posted TIMESTAMP,
    comment_text TEXT,
    PRIMARY KEY (cid,CRN,fid),
    FOREIGN KEY (CRN) REFERENCES Course(CRN),
    FOREIGN KEY (fid) REFERENCES Faculty(fid)
);

-- 8. Configuration
CREATE TABLE Configuration (
    config_id INT,
    travel_time INT,
    PRIMARY KEY (config_id)
);

-- 9. Configured_by
CREATE TABLE Configured_by (
    config_id INT,
    fid INT,
    PRIMARY KEY (config_id),
    FOREIGN KEY (config_id) REFERENCES Configuration(config_id),
    FOREIGN KEY (fid) REFERENCES Faculty(fid)
);

-- 10. Preferred_Days
CREATE TABLE Preferred_Days (
    config_id INT,
    days VARCHAR(10),
    PRIMARY KEY (config_id),
    FOREIGN KEY (config_id) REFERENCES Configuration(config_id)
);

-- 11. Preferred_Start_Times
CREATE TABLE Preferred_Start_Times (
    config_id INT,
    times TIME,
    PRIMARY KEY (config_id),
    FOREIGN KEY (config_id) REFERENCES Configuration(config_id)
);
