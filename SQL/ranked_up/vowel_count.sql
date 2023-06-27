-- Return the number (count) of vowels in the given string.

-- We will consider a, e, i, o, u as vowels for this Kata (but not y).

-- The input string will only consist of lower case letters and/or spaces.


-- IN MMSQL
SELECT str, (LENGTH(getcount.str)
- LENGTH(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(str, 'a', ''), 'e', ''), 'i',''), 'o',''), 'u',''))) AS res  FROM getcount

-- IN POSTGRES

SELECT str, LENGTH(REGEXP_REPLACE(str, '[^aeiou]', '', 'num')) AS res FROM getcount