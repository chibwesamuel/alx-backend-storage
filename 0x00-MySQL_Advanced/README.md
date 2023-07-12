#MySQL Advanced

This repository contains a collection of SQL scripts and stored procedures that demonstrate advanced techniques and concepts in MySQL. The scripts cover various aspects of database management, query optimization, data manipulation, and more. Each script focuses on a specific task and provides a solution using MySQL features and functionalities.

The repository includes the following scripts:
```
###1. Creating a Unique Table: This script demonstrates how to create a table with unique attributes and enforce business rules within the table schema.

###2. Managing User Country: This script creates a table with an enumeration attribute for user country, allowing only specific country values. Default values and table existence checks are implemented.

###3. Ranking Bands by Fan Count: The script imports a database dump of metal bands and ranks them based on the number of fans they have. The bands are ordered in descending order of fan count.

###4. Listing Glam Rock Bands: This script lists bands that specialize in Glam rock as their main style. The bands are ranked by their longevity, calculated based on the "formed" and "split" attributes.

###5. Updating Item Quantities: A trigger is created to decrease the quantity of an item after adding a new order. This ensures that the item quantity is automatically updated without manual intervention.

###6. Validating Email Changes: Another trigger is implemented to reset the "valid_email" attribute only when the email address has been changed. This helps in email validation and avoids unnecessary resets.

###7. Adding Bonus Corrections: A stored procedure is created to add a new correction for a student. The procedure takes user ID, project name, and score as input, and adds the correction to the database.

###8. Computing Average Score: This stored procedure calculates and stores the average score for a student. The procedure takes the user ID as input and updates the "average_score" attribute accordingly.

###9. Indexing Names: The script creates an index on the "names" table based on the first letter of the name attribute. This index improves search performance when querying names starting with a specific letter.

###10. Safe Division Function: A function called "SafeDiv" is created to handle division operations safely. It takes two arguments and returns the result of division or 0 if the second argument is zero.

###11. Need for a Meeting: A view named "need_meeting" is created to list students who have a score below 80 and either no last meeting date or a date more than a month ago. This helps identify students who need a meeting.

###12. Computing Weighted Average Score: A stored procedure is implemented to calculate and store the average weighted score for a student. The procedure takes the user ID as input and calculates the weighted average based on project weights and scores.
```
The scripts are organized within the repository directory "0x00-MySQL_Advanced" and can be executed on any MySQL database. Each script is accompanied by example outputs and usage instructions to facilitate understanding and usage.
