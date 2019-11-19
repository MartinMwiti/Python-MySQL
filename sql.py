import mysql.connector
#INITIALIZING
db = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    passwd="Themedici$7",
    database = "testdatabase"
)


#CREATE DATABASE

mycursor = db.cursor()
"""
mycursor.execute("CREATE DATABASE testdatabase")  # written first before adding into the "db"


#CREATE FIRST TABLE

mycursor.execute("CREATE TABLE Person(name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#used "smallint" instead of "int" to allow respresentation of smaller amount of bits. unsigned to remove any signs sice age isn't a negative number
        #VIEW DATABASE
mycursor.execute("DESCRIBE Person")

for x in mycursor: #get all output got from table "Person" and print line by line
    print(x)



#INSERTING VALUES TO THE TABLE
mycursor.execute("INSERT INTO Person(name, age) VALUES(%s, %s)", ("Joe", 22)) #%s to prevent hard coding. Best practice
db.commit()  # save input

        #VIEW TABLE CONTENTS
mycursor.execute("SELECT * FROM Person") # get all the items in the db

for x in mycursor:
    print(x)

"""

#CREATE SECOND TABLE
'''mycursor.execute("CREATE TABLE Test(name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")'''

