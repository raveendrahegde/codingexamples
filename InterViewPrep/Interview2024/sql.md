# Simple SQL engine

SQL (structured query language) is a standard way of querying a database. In
this interview we're going to write a very simple SQL engine.

Our simplified version of SQL allows you to write statements like this:

``` sql
SELECT title, author FROM library
-- This might return:
--
--  title                        |  author
-- ------------------------------+-----------------------
--  The Ministry for the Future  |  Kim Stanley Robinson
--  Circe                        |  Madeline Miller
--  Song of Achilles             |  Madeline Miller
--  Designing Climate Solutions  |  Hal Harvey

SELECT title, author FROM library WHERE author = 'Madeline Miller'
--  title                        |  author
-- ------------------------------+-----------------------
--  Circe                        |  Madeline Miller
--  Song of Achilles             |  Madeline Miller

SELECT title, author FROM library WHERE author = 'Madeline Miller' AND year > 2015
--  title                        |  author
-- ------------------------------+-----------------------
--  Circe                        |  Madeline Miller

SELECT title, author, year FROM library WHERE year > 2015 ORDER BY year, author
--  title                        |  author                |  year
-- ------------------------------+------------------------+-------
--  Designing Climate Solutions  |  Hal Harvey            |  2018
--  Circe                        |  Madeline Miller       |  2018
--  The Ministry for the Future  |  Kim Stanley Robinson  |  2020
```

## Goal
Our goal is to write a function that can run simple SQL statements over an
in-memory array. It should support the following sorts of queries:

    SELECT ... FROM table
    SELECT ... FROM table WHERE ... (AND ...)
    SELECT ... FROM table ORDER BY ...
    SELECT ... FROM table WHERE ... (AND ...) ORDER BY ...

In order to get you started, here's a regular expression that separates out the
parts of the query, and the `library` dataset from above:

``` python
import re

PARSER = re.compile(r'^SELECT (.*) FROM [a-z]+(?: WHERE (.*?))?(?: ORDER BY (.*?))?$')

# Example
print(PARSER.match("SELECT a FROM library WHERE b = 1 ORDER BY c").groups())
# This prints: ('a', 'b = 1', 'c')

LIBRARY = [
    {
        'title': 'The Ministry for the Future',
        'author': 'Kim Stanley Robinson',
        'year': 2020,
    },
    {
        'title': 'Circe',
        'author': 'Madeline Miller',
        'year': 2018,
    },
    {
        'title': 'Song of Achilles',
        'author': 'Madeline Miller',
        'year': 2012,
    },
    {
        'title': 'Designing Climate Solutions',
        'author': 'Hal Harvey',
        'year': 2018,
    },
]

```

Let's focus on getting something working. You can assume all the queries you're
given are valid, and it's okay to write code that's inefficient.
