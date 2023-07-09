
import pyodbc

conn = pyodbc.connect('DRIVER=ODBC Driver 17 for SQL Server;SERVER=ISW-221130-1108\SQLEXPRESS;DATABASE=Training;Trusted_Connection=yes;')

class Db_students_database:
    def create_table(self):
        try:
            cur = conn.cursor()
            cur.execute('''
                CREATE TABLE TRAINING.dbo.Student_database(
                    Student_ID INT IDENTITY(1, 1) PRIMARY KEY,
                    Name VARCHAR(30),
                    Course_Code VARCHAR(10),
                    Mark INT,
                    Grade CHAR(1),
                    Employment_status VARCHAR(20)
                )
            ''')
            print('Table created successfully')
            conn.commit()
        except pyodbc.Error as e:
            if conn:
                conn.rollback()
            print(e)
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def insert_to_database(self):
        try:
            cur = conn.cursor()
            number = 1  # Number of student records to insert

            for i in range(number):
                Name = input('Enter student name: ')
                Course_Code = input('Enter course code: ')
                while True:
                    Mark = int(input('Enter student mark: '))
                    if Mark < 0 or Mark > 100:
                        print('Invalid Input. Please enter a mark between 0 and 100.')
                    else:
                     if Mark >= 75:
                         Grade ='A'
                         Employment_status='Automatic Employment'
                     elif Mark >= 65:
                         Grade ='B'
                         Employment_status='Open to Work'
                     elif Mark >= 55:
                         Grade ='C'
                         Employment_status='Open to Work'
                     else:
                         Grade ='F'
                         Employment_status='Probation'
                     break  # Break out of the while loop once a valid mark is entered

                cur.execute('INSERT into TRAINING.dbo.Student_database(Name, Course_Code, Mark, Grade, Employment_status) values (?, ?, ?,?,?)', (Name, Course_Code, Mark,Grade, Employment_status))
            conn.commit()
            print('Student records inserted successfully')
        except pyodbc.Error as e:
            if conn:
                conn.rollback()
            print(e)
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def show_students_on_probation(self):
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM TRAINING.dbo.Student_database WHERE Employment_status = 'Probation'")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            if conn:
                conn.rollback()
            print(e)
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
    def show_students_on_automatic_employment(self):
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM TRAINING.dbo.Student_database WHERE Employment_status = 'Automatic Employment'")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            if conn:
                conn.rollback()
            print(e)
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()
    def show_students_open_to_work(self):
        cur = None
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM TRAINING.dbo.Student_database WHERE Employment_status = 'Open to Work'")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except pyodbc.Error as e:
            if conn:
                conn.rollback()
            print(e)
        finally:
            if cur:
                cur.close()
            if conn:
                conn.close()

    def show_all_students(self):
        cur =conn.cursor()
        cur.execute('SELECT * FROM TRAINING.dbo.Student_database ORDER BY Employment_status')
        for row in cur:
            for value in row:
                print(value, end="-")
            print()

        conn.close()



# Create the table and update grades

if __name__ =='__main__':
    db = Db_students_database()
    # db.create_table()
    db.show_all_students()
    # db.insert_to_database()
    # db.update_grades()
    # Insert student records
    # db.show_students_on_automatic_employment()

# Show students on probation
