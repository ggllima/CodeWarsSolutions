-- that will return the Minimum and Maximum ages out of all the people.

-- people table schema
-- id
-- name
-- age
-- select table schema
-- age_min (minimum of ages)
-- age_max (maximum of ages)
-- NOTE: Your solution should use pure SQL. Ruby is used within the test cases to do the actual testing.

SELECT MAX(age) AS age_max, MIN(age) AS age_min
FROM people


