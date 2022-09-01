#!/usr/bin/env python
# coding: utf-8

# Q1) What is a relational database management system (RDBMS)? What are the advantages of a database management system over a file system?
# 
# 1) An RDBMS is a type of database management system (DBMS) that stores data in a row-based table structure which connects related data elements. An RDBMS includes functions that maintain the security, accuracy, integrity and consistency of the data. This is different than the file storage used in a DBMS.
# 
# -->Advantages of a DBMS system over a file system
# 1) Data redundancy and inconsistency: Redundancy is the concept of repetition of data i.e. each data may have more than a single copy. The file system cannot control the redundancy of data as each user defines and maintains the needed files for a specific application to run. 
# 
# 2) Data sharing: The file system does not allow sharing of data or sharing is too complex. Whereas in DBMS, data can be shared easily due to a centralized system.
# 
# 3) Data concurrency: Concurrent access to data means more than one user is accessing the same data at the same time. Anomalies occur when changes made by one user get lost because of changes made by another user. The file system does not provide any procedure to stop anomalies. Whereas DBMS provides a locking system to stop anomalies to occur.
# 
# 4) Data searching: For every search operation performed on the file system, a different application program has to be written. While DBMS provides inbuilt searching operations. The user only has to write a small query to retrieve data from the database.
# 
# 5) Data integrity: There may be cases when some constraints need to be applied to the data before inserting it into the database. The file system does not provide any procedure to check these constraints automatically. Whereas DBMS maintains data integrity by enforcing user-defined constraints on data by itself.
# 
# 6) System crashing: In some cases, systems might have crashed due to various reasons. It is a bane in the case of file systems because once the system crashes, there will be no recovery of the data that’s been lost. A DBMS will have the recovery manager which retrieves the data making it another advantage over file systems. 
# 
# 7) Data security: A file system provides a password mechanism to protect the database but how long can the password be protected? No one can guarantee that. This doesn’t happen in the case of DBMS. DBMS has specialized features that help provide shielding to its data. 
# 
# 8) Backup: It creates a backup subsystem to restore the data if required.
# 
# 9) Interfaces: It provides different multiple user interfaces like graphical user interface and application program interface.
# 
# 10) Easy Maintenance: It is easily maintainable due to its centralized nature.

# In[ ]:





# Q2) In a database management system, explain the ACID properties.
# 
# 1) A transaction is a single logical unit of work that accesses and possibly modifies the contents of a database. Transactions access data using read and write operations. In order to maintain consistency in a database, before and after the transaction, certain properties are followed. These are called ACID properties. 
# 
# 2) Atomicity: By this, we mean that either the entire transaction takes place at once or doesn’t happen at all. There is no midway i.e. transactions do not occur partially. Each transaction is considered as one unit and either runs to completion or is not executed at all. It involves the following two operations. 
#     —Abort: If a transaction aborts, changes made to the database are not visible. 
#     —Commit: If a transaction commits, changes made are visible. 
#     Atomicity is also known as the ‘All or nothing rule’. 
#     
# 3) Consistency: This means that integrity constraints must be maintained so that the database is consistent before and after the transaction. It refers to the correctness of a database.
#     The total amount before and after the transaction must be maintained. 
#     
# 4) Isolation: This property ensures that multiple transactions can occur concurrently without leading to the inconsistency of the database state. Transactions occur independently without interference. Changes occurring in a particular transaction will not be visible to any other transaction until that particular change in that transaction is written to memory or has been committed. This property ensures that the execution of transactions concurrently will result in a state that is equivalent to a state achieved these were executed serially in some order.    
# 
# 5) Durability: This property ensures that once the transaction has completed execution, the updates and modifications to the database are stored in and written to disk and they persist even if a system failure occurs. These updates now become permanent and are stored in non-volatile memory. The effects of the transaction, thus, are never lost. 

# In[ ]:





# Q3) Explain the concept of normalization.
# 
# 1) Normalization is the process of organizing data in a database. This includes creating tables and establishing relationships between those tables according to rules designed both to protect the data and to make the database more flexible by eliminating redundancy and inconsistent dependency.
# 

# In[ ]:





# Q4) Explain the many types of query languages used in relational databases. DQL, DML, DCL, and DDL are some examples.
# 
# 1) -->DDL (Data Definition Language): 
#     DDL or Data Definition Language actually consists of the SQL commands that can be used to define the database schema. It simply deals with descriptions of the database schema and is used to create and modify the structure of database objects in the database.DDL is a set of SQL commands used to create, modify, and delete database structures but not data. These commands are normally not used by a general user, who should be accessing the database via an application.
# 
#     List of DDL commands: 
# 
#     CREATE: This command is used to create the database or its objects (like table, index, function, views, store procedure,   and triggers).
#     DROP: This command is used to delete objects from the database.
#     ALTER: This is used to alter the structure of the database.
#     TRUNCATE: This is used to remove all records from a table, including all spaces allocated for the records are removed.
#     COMMENT: This is used to add comments to the data dictionary.
#     RENAME: This is used to rename an object existing in the database.
#     
# 2) -->DQL (Data Query Language):
#     DQL statements are used for performing queries on the data within schema objects. The purpose of the DQL Command is to get some schema relation based on the query passed to it. We can define DQL as follows it is a component of SQL statement that allows getting data from the database and imposing order upon it. It includes the SELECT statement. This command allows getting the data out of the database to perform operations with it. When a SELECT is fired against a table or tables the result is compiled into a further temporary table, which is displayed or perhaps received by the program i.e. a front-end.
#     List of DQL: 
#     SELECT: It is used to retrieve data from the database.
#     
# 3) -->DML(Data Manipulation Language): 
#     The SQL commands that deals with the manipulation of data present in the database belong to DML or Data Manipulation Language and this includes most of the SQL statements. It is the component of the SQL statement that controls access to data and to the database. Basically, DCL statements are grouped with DML statements.
# 
#     List of DML commands: 
# 
#     INSERT : It is used to insert data into a table.
#     UPDATE: It is used to update existing data within a table.
#     DELETE : It is used to delete records from a database table.
#     LOCK: Table control concurrency.
#     CALL: Call a PL/SQL or JAVA subprogram.
#     EXPLAIN PLAN: It describes the access path to data.
#     
# 4) -->DCL (Data Control Language): 
#     DCL includes commands such as GRANT and REVOKE which mainly deal with the rights, permissions, and other controls of the database system. 
#     List of  DCL commands: 
#     GRANT: This command gives users access privileges to the database.
#     REVOKE: This command withdraws the user’s access privileges given by using the GRANT command.
#     Though many resources claim there to be another category of SQL clauses TCL – Transaction Control Language. So we will see in detail about TCL as well. TCL commands deal with the transaction within the database. 
# 
#     List of TCL commands: 
#     COMMIT: Commits a Transaction.
#     ROLLBACK: Rollbacks a transaction in case of any error occurs.
#     SAVEPOINT:Sets a savepoint within a transaction.
#     SET TRANSACTION: Specify characteristics for the transaction.    

# In[ ]:





# Q5) What is the difference between the main key and a composite key? Give instances of how primary key and composite are used.
# 
# 1) Primary key is that column of the table whose every row data is uniquely identified. Every row in the table must have a primary key and no two rows can have the same primary key. Primary key value can never be null nor can be modified or updated.
# 2) Composite Key is a form of the candidate key where a set of columns will uniquely identify every row in the table.
#     Instances of primary key:
#     CREATE TABLE Persons (
#         ID int NOT NULL,
#         LastName varchar(255) NOT NULL,
#         FirstName varchar(255),
#         Age int,
#         PRIMARY KEY (ID) );
#         
#     Instances of composite key:
#         --Creating a database:
#         CREATE School;
#         --ing database:
#         USE School;
#         --Creating table with a composite key:
#         CREATE TABLE student
#         (rollNumber INT, 
#         name VARCHAR(30), 
#         class VARCHAR(30), 
#         section VARCHAR(1), 
#         mobile VARCHAR(10),
#         PRIMARY KEY (rollNumber, mobile));
#         --Inserting records in the table:
#         INSERT INTO student (rollNumber, name, class, section, mobile) 
#         VALUES (1, "AMAN","FOURTH", "B", "9988774455");
#         INSERT INTO student (rollNumber, name, class, section, mobile) 
#         VALUES (2, "JOHN","FIRST", "A", "9988112233");
#         INSERT INTO student (rollNumber, name, class, section, mobile) 
#         VALUES (3, "TOM","FOURTH", "B", "9988777755");
#         INSERT INTO student (rollNumber, name, class, section, mobile) 
#         VALUES (4, "RICHARD","SECOND", "C", "9955663322");
#         --Querying the records:
#         SELECT * FROM student;
# ![Screenshot%202022-09-01%20102039.png](attachment:Screenshot%202022-09-01%20102039.png)
# 
# 
# 
# 
#         
#         

# In[ ]:





# Q6) Create a table with a primary key, a column default value, and a column unique constraint in SQL.
# 
# 1)    CREATE TABLE Persons (
#         ID int NOT NULL UNIQUE,
#         LastName varchar(255) NOT NULL,
#         FirstName varchar(255),
#         Age int,
#         CONSTRAINT PK_Person PRIMARY KEY (ID,LastName) );
# 

# In[ ]:




