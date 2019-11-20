import datetime
import mysql.connector
#INITIALIZING
db = mysql.connector.connect(
    host = "localhost",
    user = "root", 
    passwd= XXXXX,
    database = "testdatabase"
)


#CREATE DATABASE

mycursor = db.cursor()

mycursor.execute("CREATE DATABASE testdatabase")  # written first before adding into the "db"


#CREATE FIRST TABLE

mycursor.execute("CREATE TABLE Person(name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#used "smallint" instead of "int" to allow respresentation of smaller amount of bits. unsigned to remove any signs sice age isn't a negative number
        #VIEW DATABASE TABLE
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


#CREATE SECOND TABLE
mycursor.execute("CREATE TABLE Test(name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O') NOT NULL, id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
    #VIEW DATABASE TABLE
mycursor.execute("DESCRIBE Test")

for x in mycursor:
    print(x)

#INSERTING VALUES TO THE TABLE
mycursor.execute("INSERT INTO Test (name, created, gender) VALUES(%s,%s,%s)",
                 ("Tim", datetime.datetime.now(), "M"))
db.commit()
    #VIEW TABLE CONTENTS USING CONDITIONS
mycursor.execute("SELECT * FROM Test WHERE gender = 'M' ")
for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM Test WHERE gender = 'M' ORDER BY id DESC")
for x in mycursor:
    print(x)
    

mycursor.execute("SELECT id, name FROM Test WHERE gender = 'M' ORDER BY id ASC")
for x in mycursor:
    print(x)

#ALTER TABLE
mycursor.execute("ALTER TABLE Test ADD COLUMN city VARCHAR(50) NOT NULL")
    #DROP FROM TABLE
mycursor.execute("ALTER TABLE Test DROP city")   

mycursor.execute('DESCRIBE Test')
print(mycursor.fetchone) #only if you have one line of input

for x in mycursor:
    print(x)

    #CHANGE NAME OF OUR COLUMNS OR TABLE

mycursor.execute('ALTER TABLE Test CHANGE name first_name VARCHAR(50)') #change column name from "name" to "first_name"
mycursor.execute('DESCRIBE Test')

for x in mycursor:
    print(x)


#FOREIGN KEY
users = [("Martin", "mso123"), ("Joe", "joy123"), ("Joey", "joey123")]

user_scores = [(45,100), (30,200), (46,124)]

#CREATE TABLE  
Q1 = "CREATE TABLE User(id int PRIMARY KEY AUTO_INCREMENT NOT NULL ,name VARCHAR(50), passwd VARCHAR(50))" #PARENT TABLE

Q2 = "CREATE TABLE Score (userid int PRIMARY KEY, FOREIGN KEY(userId) REFERENCES User(Id),game1 int  DEFAULT 0, game2 int  DEFAULT 0)"

mycursor.execute(Q1)
mycursor.execute(Q2)

#DISPLAY ALL TABLES IN THE DATABASE
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

users = [("Martin", "mso123"), ("Joe", "joy123"), ("Joey", "joey123")]

user_scores = [(45, 100), (30, 200), (46, 124)]

#METHOD 1: quick way to add many data
#mycursor.executemany("INSERT INTO User(name, passwd) VALUES (%s, %s)", users)

#METHOD 2: same as exact output as method 1 but in loop form

Q3 = "INSERT INTO User(name, passwd) VALUES (%s, %s)"
Q4 = "INSERT INTO Score(userId, game1, game2) VALUES (%s, %s, %s)"
for x, user in enumerate(users):
    mycursor.execute(Q3, user)
    last_id = mycursor.lastrowid
    mycursor.execute(Q4, (last_id,) + user_scores[x])
    
db.commit()#saves the data

mycursor.execute("SELECT * FROM User")

for x in mycursor:
    print(x)

mycursor.execute("SELECT * FROM Score")

for x in mycursor:
    print(x)
