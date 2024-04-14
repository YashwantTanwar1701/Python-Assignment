#!/usr/bin/env python
# coding: utf-8

# Q: Explain different types of views. Demonstrate with suitable examples.
# 
# Ans. 
# In SQL, views are virtual tables that are based on the result set of a SQL statement. They provide a way to simplify complex queries, encapsulate business logic, and control access to data. There are several types of views in SQL, including:
# 1. Simple Views
# 2. Complex Views
# 3. Indexed Views
# 4. Materialized Views
# 5. Recursive Views
# 
# 
# 
# 1. Simple Views: Simple views are based on a single table and can contain all or a subset of the rows and columns from that table. They are easy to create and maintain.
# 
# CREATE VIEW simple_view AS
# SELECT column1, column2
# FROM table_name
# WHERE condition;
# 
# 
# 
# 2. Complex Views: Complex views are based on multiple tables or other views and can involve joins, aggregates, and subqueries.
# 
# CREATE VIEW complex_view AS
# SELECT t1.column1, t2.column2
# FROM table1 t1
# JOIN table2 t2 ON t1.id = t2.id
# WHERE t1.condition = 'value';
# 
# 
# 3. Indexed Views: Indexed views are stored physically on the disk like tables and can have clustered indexes. They are useful for improving query performance by pre-computing and storing aggregated or frequently used data. 
# 
# CREATE VIEW indexed_view
# WITH SCHEMABINDING
# AS
# SELECT column1, SUM(column2) AS total
# FROM dbo.table1
# GROUP BY column1;
# GO
# 
# CREATE UNIQUE CLUSTERED INDEX index_name
# ON indexed_view (column1);
# 
# 
# 4. Materialized Views: Materialized views store the result set of a query physically, allowing for faster access but potentially slower updates compared to regular views. They are commonly used in data warehousing and reporting scenarios.
# 
# CREATE MATERIALIZED VIEW materialized_view AS
# SELECT column1, AVG(column2) AS average
# FROM table_name
# GROUP BY column1;
# 
# 5. Recursive Views: Recursive views are used to work with hierarchical data structures. They allow a view to reference itself recursively.
# 
# CREATE VIEW recursive_view AS
# WITH RECURSIVE cte AS (
#   SELECT id, parent_id, name
#   FROM table_name
#   WHERE parent_id IS NULL
#   UNION ALL
#   SELECT t.id, t.parent_id, t.name
#   FROM table_name t
#   JOIN cte ON t.parent_id = cte.id
# )
# SELECT * FROM cte;
# 

# 2. What is the difference between function and stored procedure? Write syntax for creating functions and stored procedures.
# Ans: 
# 
# Functions and stored procedures are both database objects used to encapsulate and execute a set of SQL statements. However, they have some key differences in terms of their usage and behavior.
# 
# Stored Procedure:
# 
# A stored procedure is a precompiled collection of SQL statements and procedural logic that is stored in the database.
# It can accept input parameters, perform operations, and return multiple result sets.
# Stored procedures can contain conditional statements, loops, exception handling, and other procedural constructs.
# They are mainly used for performing tasks like data manipulation, data validation, and business logic implementation.
# Function:
# 
# A function is a reusable block of SQL code that accepts input parameters, performs calculations, and returns a single value.
# Functions are deterministic, meaning that for a given set of input parameters, they always return the same output.
# They cannot perform operations like data manipulation or transaction control, but they are ideal for calculations, data formatting, and reusable logic.
# Functions can be used inline within SQL statements, making them convenient for use in queries and expressions.
# Syntax for creating a stored procedure:
# 
# 
# Syntax for creating a stored procedure:
# CREATE PROCEDURE procedure_name
#     [ (parameter1 datatype, parameter2 datatype, ...) ]
# AS
# BEGIN
#     -- SQL statements and procedural logic here
# END;
# 
# example - 
# CREATE PROCEDURE GetEmployeeCount
# AS
# BEGIN
#     SELECT COUNT(*) AS EmployeeCount FROM Employees;
# END;
# 
# ------------------------------------------------------------
# 
# Syntax for creating a function:
# 
# CREATE FUNCTION function_name
#     (parameter1 datatype, parameter2 datatype, ...)
# RETURNS return_datatype
# AS
# BEGIN
#     -- SQL statements and calculations here
#     RETURN return_value;
# END;
# 
# 
# example:
# CREATE FUNCTION CalculateTax
#     (@income DECIMAL(10,2))
# RETURNS DECIMAL(10,2)
# AS
# BEGIN
#     DECLARE @tax DECIMAL(10,2);
#     SET @tax = @income * 0.1; -- Assuming 10% tax rate
#     RETURN @tax;
# END;
# 
# ------------------------------------------------------------
# 

# 3. What is an index in SQL? What are the different types of indexes in SQL? 
# Ans: 
# In SQL, an index is a database object that improves the speed of data retrieval operations on a table by providing a quick lookup mechanism. It is a data structure associated with a table that allows for efficient querying of rows based on one or more columns.
# 
# Indexes work similar to the index in a book, where the index helps you quickly find information by referring to page numbers. Similarly, in a database, indexes help locate rows efficiently based on the values of indexed columns.
# 
# Different types of indexes in SQL include:
# 
# 1. Primary Index: A primary index is automatically created when a primary key constraint is defined on a table. It ensures that each row in the table is uniquely identifiable and enforces data integrity. Typically, primary indexes are implemented as clustered indexes, meaning the physical order of the rows in the table corresponds to the order of the index.
# 
# 2. Unique Index: A unique index ensures that the values in the indexed columns are unique across the table. Unlike primary keys, unique indexes allow NULL values (except for the primary key). They are often used to enforce uniqueness constraints on columns that are not primary keys.
# 
# 3. Clustered Index: A clustered index determines the physical order of rows in the table based on the indexed column(s). Each table can have only one clustered index because the data rows themselves are physically ordered based on the clustered index key. This means that a table with a clustered index can be thought of as a sorted table.
# 
# 4. Non-Clustered Index: A non-clustered index does not affect the physical order of the rows in the table. Instead, it creates a separate data structure that contains pointers to the actual rows. Non-clustered indexes are useful for improving the performance of SELECT queries by providing a quick lookup mechanism.
# 
# 5. Composite Index: A composite index consists of more than one column. It is used when queries involve multiple columns in the WHERE clause or when you want to enforce uniqueness on combinations of columns.
# 
# 6. Covering Index: A covering index includes all the columns needed to satisfy a query in the index itself. This allows the database engine to retrieve the required data directly from the index without accessing the underlying table, which can significantly improve query performance.
# 
# 7. Bitmap Index: A bitmap index is a special type of index used for columns with a low cardinality (a small number of distinct values). It stores a bitmap for each distinct value in the indexed column, indicating which rows contain that value.
# 
# Each type of index serves a specific purpose and can be used to optimize different types of queries in a database system.
4.Showcase an example of exception handling in SQL stored procedure.
# 5. Create a SQL function to split strings into rows on a given character? 
# Input String: Stephen;peter;berry;Olivier;caroline;
# 
# Stephen
# Peter
# Berry
# Oliver
# Caroline
# 
# CREATE FUNCTION split_string_into_rows(input_string VARCHAR(255), delimiter CHAR(1))
# RETURNS TABLE (part VARCHAR(255))
# BEGIN
#     DECLARE start_pos INT DEFAULT 1;
#     DECLARE end_pos INT DEFAULT 1;
#     DECLARE part_length INT;
# 
#     WHILE end_pos > 0 DO
#         SET end_pos = INSTR(input_string, delimiter, start_pos);
#         IF end_pos = 0 THEN
#             SET part_length = LENGTH(input_string) - start_pos + 1;
#         ELSE
#             SET part_length = end_pos - start_pos;
#         END IF;
#         INSERT INTO RETURN_TABLE (part) VALUES (SUBSTRING(input_string, start_pos, part_length));
#         SET start_pos = end_pos + 1;
#     END WHILE;
#     RETURN;
# END;
# 
# 
# 
# 
# SELECT *
# FROM TABLE(split_string_into_rows('Stephen;peter;berry;Olivier;caroline', ';'));
# 
# 
# This query will return each part of the input string as separate rows.
# 
# 

# 6. What is a temporary and a variable table? Write suitable syntax to create temporary tables and variable tables.
# 
# Temporary tables and table variables are both used to store data temporarily within a session or a batch of queries in SQL Server. However, they have some differences in terms of their scope, behavior, and usage.
# 
# Temporary Tables:
# 
# Temporary tables are physical tables that exist for the duration of a session or a transaction. They can be explicitly created and dropped by the user or system, and they are stored in the tempdb system database. Temporary tables can be accessed by multiple users and can be used across different batches or stored procedures.
# 
# Syntax to create a temporary table:
# CREATE TABLE #temp_table (
#     column1 datatype,
#     column2 datatype,
#     ...
# );
# 
# Example: 
# CREATE TABLE #temp_table (
#     id INT,
#     name VARCHAR(50)
# );
# 
# INSERT INTO #temp_table VALUES (1, 'John'), (2, 'Alice');
# 
# SELECT * FROM #temp_table;
# 
# DROP TABLE #temp_table;
# 
# 
# ----------------------------------------------
# Table Variables:
# 
# Table variables are variables that hold a result set like a table. They are declared and used like any other variable but are limited to the scope of the batch, stored procedure, or function in which they are declared. Table variables reside in memory and are deallocated when the batch or procedure ends, making them efficient for smaller datasets.
# 
# Syntax to declare a table variable:
# DECLARE @table_variable TABLE (
#     column1 datatype,
#     column2 datatype,
#     ...
# );
# 
# Example of using a table variable:
# 
# DECLARE @table_variable TABLE (
#     id INT,
#     name VARCHAR(50)
# );
# 
# INSERT INTO @table_variable VALUES (1, 'John'), (2, 'Alice');
# 
# SELECT * FROM @table_variable;
# 
# 
# It's important to note that table variables cannot have nonclustered indexes, statistics, or constraints defined on them, while temporary tables can. Additionally, temporary tables are generally preferred for larger datasets or when complex operations such as indexing are required, while table variables are suitable for smaller datasets or intermediate results within a procedure or function.
# 
