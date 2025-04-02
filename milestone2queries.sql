SELECT CRN
FROM Courses
GROUP BY fid;

SELECT Main.CRN, Prereq.CRN
FROM Courses Main 

