# Write your MySQL query statement below
SELECT e1.Name As Employee
  FROM Employee e1
  JOIN Employee e2
    ON e1.ManagerId = e2.Id
 WHERE e1.Salary > e2.Salary