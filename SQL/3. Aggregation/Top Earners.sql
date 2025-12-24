SELECT MAX(salary*months) ,COUNT(Employee_id)
FROM EMployee
WHERE 
salary*months = (SELECT MAX(salary*months) FROM EMployee);