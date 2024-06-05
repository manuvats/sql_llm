import sqlite3

# Connect to sqlite
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table, retireve records
cursor = connection.cursor()

## create the table
table_info="""
    CREATE TABLE IF NOT EXISTS student(
        NAME VARCHAR(25),
        CLASS VARCHAR(25),
        SECTION VARCHAR(25),
        MARKS INT
    );
    """

cursor.execute(table_info)

## Insert some more records
cursor.execute('''Insert Into STUDENT values('Manu','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('John','BI','B',100)''')
cursor.execute('''Insert Into STUDENT values('Ashok','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Divyesh','BI','A',50)''')
cursor.execute('''Insert Into STUDENT values('Jack','Big Data','A',35)''')
cursor.execute('''Insert Into STUDENT values('Nancy','Data Science','A',95)''')

# Display all the records
print("The inserted records are \n")

data = cursor.execute('''Select * from STUDENT ''')

for row in data:
    print(row)

## Close the connection
connection.commit()
connection.close()