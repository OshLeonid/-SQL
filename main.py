import sqlite3
global data, columns
data = []
columns = ('participant ', 'grade', 'scores', 'status')

db = sqlite3.connect('participants.db')
cursor = db.cursor()

def read(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.split(';')
            line = (line[0], int(line[1]), float(line[2].replace('\n','')))
            data.append(line)
def create_database():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_7 
        (
            PARTICIPANT TEXT,
            SCORES FLOAT,
            STATUS TEXT
        )
    ''')
    db.commit()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student_8
        (
            PARTICIPANT TEXT,
            SCORES FLOAT,
            STATUS TEXT
        )
    ''')
    db.commit()
def add_to_database(data):
    for line in data:
        if line not in cursor.execute('SELECT * FROM student_'+str(line[1])):
            if line[2]>=18:
                place ="Победитель"
            elif line[2]>=15:
                place = "Призёр"
            else:
                place = "Участник"
            cursor.execute(f'INSERT INTO student_'+str(line[1])+' VALUES ("'+line[0]+'",'+str(line[2])+',"'+place+'")')
        else:
    db.commit()
create_database()
read('таблица 1.txt')
add_to_database(data)