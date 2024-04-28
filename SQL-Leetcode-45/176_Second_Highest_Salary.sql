/*
176. Second Highest Salary

leetcode: https://leetcode.com/problems/second-highest-salary/?envType=list&envId=e97a9e5m
# https://www.sqltutorial.org/sql-limit/

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

 

Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

The result format is in the following example.

 

Example 1:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+

Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

Example 2:

Input: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+

Output: 
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+

*/

/*
In this syntax:
    The LIMIT row_count determines the number of rows (row_count) returned by the query.
    The OFFSET offset clause skips the offset rows before beginning to return the rows.
*/

-- query soltuion:

select 
(select distinct(salary) from Employee 
order by salary DESC limit 1 offset 1) 
as SecondHighestSalary;
