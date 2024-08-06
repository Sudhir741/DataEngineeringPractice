-- Write a query to display all the first_name  in upper case
select upper(FIRST_NAME) 
from Worker;

-- Write a querty to display unique department from workers table
select distinct DEPARTMENT 
from Worker;

-- Write an SQL query to print the first three characters of FIRST_NAME from Worker table
select  substr(first_name,1,3) 
from Worker;

-- Write an SQL query to find the position of the alphabet (‘a’) in the first name column ‘Amitabh’ from Worker table.
SELECT POSITION('a' IN first_name) AS Position
FROM Worker
WHERE first_name = 'Amitabh';

-- Write an SQL query that fetches the unique values of DEPARTMENT from Worker table and prints its length
select distinct length(department) Length, department 
from Worker;

-- Write an SQL query to print all Worker details from the Worker table order by FIRST_NAME Ascending and DEPARTMENT Descending
select * from Worker 
order by FIRST_NAME Asc, DEPARTMENT Desc;

-- Write a query to get workers whose name are Vipul and Satish
 select * from Worker 
 where FIRST_NAME in ("Vipul","Satish");

-- Write an SQL query to print details of the Workers whose FIRST_NAME contains 'a'
 select * from Worker 
 where FIRST_NAME like "%a%";

-- Write an SQL query to print details of the Workers whose FIRST_NAME ends with ‘h’ and contains six alphabets
 select * from Worker 
 where FIRST_NAME like "_____h";
 
-- Write an SQL query to print details of the Workers whose SALARY lies between 100000 and 500000
select * from Worker 
where salary between 100000 and 500000;

-- Write an SQL query to print details of the Workers who have joined in Feb’2014
select * from Worker where YEAR(joining_date) = 2014 AND MONTH(joining_date) = 2;
select * from worker where joining_data like "2014-02-%"

-- Write an SQL query to fetch the count of employees working in the department ‘Admin’
select count(*) Employees 
from Worker 
group by department 
having department ="admin";

-- Write an SQL query to fetch the no. of workers for each department in the descending order
select count(*) Workers,department 
from Worker 
group by department 
order by count(*) desc;

-- Write a query to display workers who are managers
select first_name as emp, Worker_title as manager 
from title join worker on worker_id= worker_ref_id 
where worker_title = 'Manager'

-- Write query to find duplicate rows title table
select count(*), WORKER_TITLE 
from title 
group by WORKER_TITLE 
having count(*) > 1;

-- Write an SQL query to show all workers who got the bonus along with bonus amount
select first_name, bonus_amount 
from worker inner join bonus on  worker_id = worker_ref_id

-- Write a query to find employees in worker table that do not exist in bonus table (ie did not get bonus)
select first_name,bonus_amount 
from worker left join bonus on  worker_id = worker_ref_id 
where bonus_amount is null;

-- Write a query to find the highest 2 salaries
select distinct salary 
from worker 
order by salary desc limit 2;

-- Find 2nd highest without using TOP or LIMIT
select max(salary) from worker where salary < (select max(salary) from worker) ;

-- Find people who have the same salary
select * from Worker where salary in 
(select salary
    from Worker
    group by salary
    having count(*) > 1
);
   
-- Write a query to fetch 1st 50% records without using Top


-- Write a query to select a department with more than 3 people in worker table
select count(*) Workers, department 
from worker 
group by department 
having count(*) >3;

-- Write a query to select 1st and last row of a worker table
(SELECT * 
 FROM worker 
 ORDER BY worker_id ASC 
 LIMIT 1)
UNION ALL
(SELECT * 
 FROM worker 
 ORDER BY worker_id DESC 
 LIMIT 1);

-- Write a query to select last 5 entries from worker table
SELECT * 
FROM worker 
ORDER BY worker_id DESC 
LIMIT 5;

-- Write a query to select people with highest salary in each group
select * from worker 
where salary in (select max(salary) 
from worker 
group by department);


-- Write a query to fetch departments along with the total salaries paid for each of them
select sum(salary),department 
from worker 
group by department

-- Write a query to fetch the names of workers who earn the highest salary
select * from worker 
where salary in ( select max(salary) from worker)


 
 




