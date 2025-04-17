-- Get all courses that have the same faculty member

SELECT *
FROM Course
WHERE Course.fid = :fid

-- Get all Prereqs of a Course
SELECT Course.*
FROM Prereqs JOIN Course ON Prereqs.prereq_course_code = Course.course_code
WHERE Prereqs.course_code = :main_course_code;

-- Get all Coreqs of a Course
(SELECT Course.*
FROM Coreqs JOIN Course ON Coreqs.CRN1 = Course.CRN
WHERE Coreqs.CRN2 = :main_crn OR Coreqs.CRN1 = :main_crn)
UNION
(SELECT Course.*
FROM Coreqs JOIN Course ON Coreqs.CRN2 = Course.CRN
WHERE Coreqs.CRN2 = :main_crn OR Coreqs.CRN1 = :main_crn);

-- Add the conflict numbers into database after running algorithm

INSERT INTO Conflict_no (:course_code, :conflict_number);

-- Reset the Conflict_no table (Used when the course data has changed)
DELETE FROM Conflict_no;


-- Assertion that each configuration must be configured by atleast 1 person
-- Load all Configurations, Load the Configured_by table, and check that each Configuration is in the Configured_by table

CREATE ASSERTION no_empty_configurations
CHECK (
    ((SELECT COUNT(config_id) FROM Configuration) = 
    (SELECT COUNT(DISTINCT config_id) FROM Configured_by))
);

-- Load all the configuration data from the faculty who configures a configuration

SELECT Configuration.*
FROM Configuration NATURAL JOIN Configured_by
WHERE fid = :fid;



