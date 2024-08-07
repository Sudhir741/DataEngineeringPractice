
CREATE TABLE Student (
StdID INT(4) PRIMARY KEY, 
StdName VARCHAR(30) NOT NULL,
Sex VARCHAR(1), 
Percentage DECIMAL(5,2), 
SClass INT , 
Sec VARCHAR(1), 
Stream VARCHAR(10), 
DOB DATE );

INSERT INTO STUDENT (StdID, StdName, Sex, Percentage, SClass, Sec, Stream, DOB) VALUES
-- (1001, 'AKSHRA AGARWAL', 'F', 70, 11, 'A', 'Science', '1996/10/13'), 
(1002, 'ANJANI SHARMA', 'F', 75, 11, 'A', 'Commerce', '1996/09/18'), 
(1003, 'ANSHUL SAXENA', 'M', 78, 11, 'A', 'Commerce', '1996/11/19'), 
(1004, 'AISHWARYA SINGH', 'F', 79, 11, 'A', 'Commerce', '1996/11/01'), 
(1005, 'AKRITI SAXENA', 'F', 76, 11, 'A', 'Commerce', '1996/09/20'), 
(1006, 'KHUSHI AGARWAL', 'F', 77, 11, 'A', 'Commerce', '2003/09/14'), 
(1007, 'MAAHI AGARWAL', 'F', 74, 11, 'A', 'Science', '1997/04/21'), 
(1008, 'MITALI GUPTA', 'F', 78, 12, 'A', 'Science', '1997/11/26'), 
(1009, 'NIKUNJ AGARWAL', 'M', 58, 12, 'A', 'Science', '1997/07/12'), 
(1010, 'PARKHI', 'F', 59, 12, 'A', 'Commerce', '1997/12/20'), 
(1011, 'PRAKHAR TIWARI', 'M', 43, 12, 'A', 'Science', '1997/04/22'), 
(1012, 'RAGHAV GANGWAR', 'M', 58, 12, 'A', 'Commerce', '1997/12/21'), 
(1013, 'SAHIL SARASWAT', 'M', 57, 12, 'A', 'Commerce', '1997/08/13'), 
(1014, 'SWATI MISHRA', 'F', 98, 11, 'A', 'Science', '1996/08/13'), 
(1015, 'HARSH AGARWAL', 'M', 58, 11, 'B', 'Science', '2003/08/28'), 
(1016, 'HARSHIT KUMAR', 'M', 98, 11, 'B', 'Science', '2003/05/22'), 
(1017, 'JAHANVI KAPOOR', 'M', 65, 11, 'B', 'Science', '1997/01/10'),
(1018, 'STUTI MISHRA', 'M', 66, 11, 'C', 'Commerce', '1996/01/10'),
(1019, 'SURYANSH KUMAR AGARWAL', 'M', 85, 11, 'C', 'Commerce', '2007/08/22'), 
(1020, 'TANI RASTOGI', 'F', 75, 12, 'C', 'Commerce', '1998/01/15'),
(1021, 'TANISHK GUPTA', 'M', 55, 12, 'C', 'Science', '1998/04/11'),
(1022, 'TANMAY AGARWAL', 'M', 57, 11, 'C', 'Commerce', '1998/06/28'), 
(1023, 'YASH SAXENA', 'M', 79, 11, 'C', 'Science', '1998/03/13'),
(1024, 'YESH DUBEY', 'M', 85, 12, 'C', 'Commerce', '1998/04/03')

-- Lab Activity 2

-- 1 To display all the records form STUDENT table. 
SELECT * FROM student ;

-- 2. To display ony name and date of birth from the table STUDENT. 
SELECT StdName, DOB FROM student ;

-- 3. To display all students record where percentage is greater of equal to 80 FROM student table. 
SELECT * FROM student WHERE percentage >= 80;

-- 4. To display student name, stream and percentage where percentage of student is more than 80 
SELECT StdName, Stream, Percentage WHERE percentage > 80;

-- 5. To display all records of science students whose percentage is more than 75 form student table. 
SELECT * FROM student WHERE stream = 'Science' AND percentage > 75;


-- Lab Activity 3

--  To display the STUDENT table structure.
DESCRIBE Student;

--  To add a column (FIELD)in the STUDENT table,for example TeacherID as VARCHAR(20);
ALTER TABLE Student ADD TeacherID VARCHAR(20);

-- To modify the TeacherID data type form character to integer.
ALTER TABLE Student MODIFY TeacherID INT ; 


-- Lab Activity 4
-- 1. To Drop (Delete) a field form a table. For e.g you wantto delete TeacherID field.
ALTER TABLE Student DROP TeacherID;

-- 2. To subtract 5 form all students percentage and display name and percentage.
SELECT name, percentage - 5 FROM Student;

-- 3. Using column alise for example we want to display StdName as Student Name and DOB as Date of Birth then the statement will be.
SELECT StdName AS 'Student Name',
DOB As 'Date of Birth' 
FROM Student;

-- 4. Display the name of all students whose stream is not Science
SELECT StdNameFROMstudent 
WHERE Stream <>'Science';

-- 5. Display all name and percentage where percentage is between 60 and 80
SELECT StdName, percentage 
FROM student 
WHERE percentage >=60 AND percentage<=80 ;

-- Lab Activity 5:
-- 1. To change a studentname from SWATI MISHRA to SWATIVERMA whose StdID is 1014 and also change percentage 86.
UPDATE Student SET StdName = ‘SWATI VERMA’, percentage = 86
WHERE StdId = 1014;

-- 2. To delete the records form student table where StdId is 1016.
DELETE FROM Student WHERE StdID = 1016;

-- 3. Type the following SQL statement and note the output.
SELECT * FROM Student WHERE StdName LIKE 'G_' ; 
SELECT * FROM Student WHERE StdName='G';
SELECT * FROM Student WHERE StdName LIKE 'G%' ; 
SELECT * WHERE Student WHERE StdName='%G%' ;

-- 4. Display all the streams in student table.
SELECT DISTINCT Stream FROM Student;

-- 5. Note the output of the following statement.
SELECT StdName, Sex, Stream FROM Student WHERE percentage BETWEEN 70 AND 80

-- DO IT YOURSELF
CREATE TABLE employeesTable (
    empno INT,
    ename VARCHAR(255),
    job VARCHAR(255),
    mgr INT,
    hiredate DATE,
    sal DECIMAL(10, 2),
    comm DECIMAL(10, 2),
    deptno INT
);

INSERT INTO employeesTable (empno, ename, job, mgr, hiredate, sal, comm, deptno) VALUES
(8369, 'SMITH', 'CLERK', 8902, '1990-12-18', 800.00, NULL, 20),
(8499, 'ANYA', 'SALESMAN', 8698, '1991-02-20', 1600.00, 300.00, 30),
(8521, 'SETH', 'SALESMAN', 8698, '1991-02-22', 1250.00, 500.00, 30),
(8566, 'MAHADEVAN', 'MANAGER', 8839, '1991-04-02', 2985.00, NULL, 20),
(8654, 'MOMIN', 'SALESMAN', 8696, '1991-09-28', 1250.00, 1400.00, 30),
(8698, 'BINA', 'MANAGER', 8839, '1991-05-01', 2850.00, NULL, 30),
(8887, 'SHIVANSH', 'MANAGER', 8839, '1991-06-09', 2450.00, NULL, 10),
(8888, 'SCOTT', 'ANALYST', 8566, '1992-12-09', 3000.00, NULL, 20),
(8839, 'AMIR', 'PRESIDENT', NULL, '1991-11-18', 5000.00, NULL, 10),
(8844, 'KULDEEP', 'SALESMAN', 8698, '1991-09-08', 1500.00, 0.00, 30);


-- a. Write a query to display EName and Sal of employees whose salary are greater than or equal to 2200?
use classicmodels
select ename, sal from employeesTable where sal >= 2200;

-- b. Write a query to display details of employs who are not getting commission?
select * from employeesTable where comm is null;

-- c. Write a query to display employee name and salary of those employees who don’t have their salary in range of 2500 to 4000?
select ename,sal from employeesTable  where sal not in (select sal from employeesTable where sal between 2500 and 4000);

-- d. Write a query to display the name, job title and salary of employees who don’t have manager?
select m.ename as manger, e.ename as employee  from employeesTable m right join employeesTable e on e.empno=m.mgr where m.mgr is null;

-- e. Write a query to display the name of employee whose name contains “A” as third alphabet?
select * from employeesTable where ename like '__a%'

-- f. Write a query to display the name of employee whose name contains “T” as last alphabet?
select * from employeesTable where ename like '%t'

-- g. Write a query to display the name of employee whose name contains ”M” as First and “L” as third alphabet?
select * from employeesTable where ename like 'm_l%'

-- h. Write a query to display details of employs with the text “Not given”, if commission is null
select ename, ifnull(comm,'Not Given') from employeesTable 