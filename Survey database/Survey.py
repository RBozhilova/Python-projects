import sqlite3
import pandas as pd
import os

'''

This script creates survey form.  
The questions are asked on by one.
After a question is asked the program should wait for user input in the console.
After answer is provided, the user is presented with the second question.
This goes until all the questions are exhausted.
After all questions are answered, the result should be saved into the Survey table.
Тhe csv file output should be created. The output file contains information from the database. 
Release 1.0
'''

db = "QuestionsAnswers_DB.db"

# Check if the file exists, if it does not then create it
if not os.path.exists(db):
    conn = sqlite3.connect(db)
    print("Database was created")
elif os.path.exists(db):
    conn = sqlite3.connect('QuestionsAnswers_DB.db')
    print(f'Database exists. Successfully connected to {db}')

# Connect to database
cursor = conn.cursor()

# Create table Users
cursor.execute('''CREATE TABLE IF NOT EXISTS Users(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username varchar(255) NOT NULL,
                            password varchar(255) NOT NULL)''')


# Create method to insert values in table Users
def insert_user(user_name, user_password):
    cursor.execute('''INSERT INTO Users (username, password) VALUES(?, ?)''', (user_name, user_password))


# Create table Questions
cursor.execute('''CREATE TABLE IF NOT EXISTS Questions(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            question varchar(10000))''')


# Create method to insert new questions
def add_question(question):
    cursor.execute('''INSERT INTO Questions(question) VALUES(?)''', [question])


# Create table Survey
cursor.execute('''CREATE TABLE IF NOT EXISTS Survey(
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            user_id INTEGER,
                            question_id INTEGER,
                            answer varchar(1000),
                            FOREIGN KEY (user_id) REFERENCES Users(id)
                            FOREIGN KEY (question_id) REFERENCES Questions(id))''')

# Insert default questions in Questions table. Commit the changes.
cursor.execute('''INSERT INTO Questions(question) VALUES("What is your name?")''')
cursor.execute('''INSERT INTO Questions(question) VALUES("What is your email?")''')
cursor.execute('''INSERT INTO Questions(question) VALUES("What is your favorite movie?")''')
cursor.execute('''INSERT INTO Questions(question) VALUES("What is your favorite music band?")''')
cursor.execute('''INSERT INTO Questions(question) VALUES("What is your favorite food?")''')
conn.commit()

# Ask the user to choose one option
print("Enter 1 for admin; 2 for users; 3 exit")
command = input("Enter your command: ").strip()

# Start while loop. The loop will end when the command is 3 for exit.
while True:

    # When the command is 1, user could add extra questions.
    if command == "1":
        question = input("What is an extra question? ")
        add_question(question)
        conn.commit()
        print("Your question is added to survey form.")

    # When the command is 2, ask user to answer the question.
    elif command == "2":
        # Ask user for username and password in the console
        user_username = input("Enter username: ")
        user_password = input("Enter password: ")

        # Insert data in Users table
        insert_user(user_username, user_password)

        # Print to the console the question from table Questions to the user one by one
        cursor.execute("SELECT id, Question FROM Questions")
        questions = cursor.fetchall()

        for row in questions:
            question = str(row[1])
            answer = input(question + ' ')

            # Find current question's ID from table
            question_id = row[0]

            # Find current username ID from table Users
            cursor.execute('''SELECT id FROM Users WHERE username = ?''', [user_username])
            user_id = cursor.fetchall()[0][0]

            #  Insert values for answer, user_id and question_id if table Survey
            cursor.execute("""INSERT INTO Survey(answer, user_id, question_id) VALUES(?,?,?)""",(answer, user_id, question_id))

            # Save the changes for every question
            conn.commit()

    # When command is 3, exit the circle.
    elif command == "3":
        break

    command = input("If you want to enter new extra question, enter 1. If you want to enter the answers for new user, "
                    "enter 2. If you want to exit the survey form, please enter 3. \nEnter your command: ")


# Create csv file output.csv with information from database
data = pd.read_sql('''SELECT username, question, answer 
                    FROM Survey
                    INNER JOIN Questions ON Questions.id=Survey.question_id
                    INNER JOIN Users ON Users.id = Survey.user_id''', conn)

data.to_csv('output.csv')

#Close the database connection
conn.close()


