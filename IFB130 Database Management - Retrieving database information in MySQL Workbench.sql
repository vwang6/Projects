SELECT firstName, surname, studentID, email
FROM student
WHERE suburb LIKE 'Everton%';

SELECT *
FROM student
WHERE buddyID IS NOT NULL 
ORDER BY surname;

SELECT t.staffID, firstName, surname, COUNT(ut.unitID) as unitNum
FROM tutor t
NATURAL JOIN unittutor ut
NATURAL JOIN unit u 
GROUP BY t.staffID;

SELECT a.assignmentID, a.assignmentName, MIN(grade), MAX(grade), AVG(grade), COUNT(g.assignmentID) as submissionNum 
FROM assignment a
JOIN grade g 
ON a.assignmentID = g.assignmentID
GROUP BY a.assignmentID;

SELECT CONCAT(t.firstName, ' ', t.surname) AS fullName, t.email
FROM tutor t
WHERE NOT EXISTS (SELECT * FROM unittutor WHERE t.staffID = unittutor.staffID);

SELECT sleepID, sp.studentID, dueDate, timeAsleep, g.assignmentID, grade, AVG(timeAsleep) as Average
FROM sleeppatterns sp
NATURAL JOIN grade g
NATURAL JOIN assignment a
WHERE MONTH(date)= 4
GROUP BY sp.studentID
HAVING AVG(sp.timeAsleep) < 6
AND MONTH(dueDate)= 4

INSERT INTO unit (unitName, unitCode, semester, year)
VALUES('Advanced Database Management', 'IFB801', '1', '2019');

SET SQL_SAFE_UPDATES = 0;

DELETE FROM phonenumber
WHERE phoneNumber LIKE '02%';

UPDATE student
SET streetNumber = '72', streetName = 'Evergreen Terrace', suburb = 'Springfield'
WHERE streetNumber = '180' AND streetName = 'Zelda Street'AND suburb = 'Linkburb'
AND surname = '%Smith%'; 

CREATE INDEX assignmentIndex ON assignment (assignmentName);

DROP VIEW IF EXISTS studentnotenrolled;
CREATE VIEW studentnotenrolled AS 
SELECT s.studentID, s.firstName, s.surname 
FROM student s
NATURAL JOIN enrolments e
LEFT JOIN unit u 
ON e.unitID = u.unitID; 

DROP USER IF EXISTS nikki@localhost;
CREATE USER nikki@localhost
IDENTIFIED BY 'secret';

GRANT INSERT 
ON pulselearning.student
TO nikki@localhost;

GRANT DELETE 
ON pulselearning.student
TO nikki@localhost;

DROP USER IF EXISTS jake@localhost;
CREATE USER jake@localhost
IDENTIFIED BY 'secret';

GRANT INSERT 
ON pulselearning.student
TO jake@localhost;

GRANT DELETE 
ON pulselearning.student
TO jake@localhost;

REVOKE INSERT
ON pulselearning.student
FROM jake@localhost;

REVOKE DELETE
ON pulselearning.student
FROM jake@localhost;