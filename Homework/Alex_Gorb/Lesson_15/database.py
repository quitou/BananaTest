import pymysql
import pymysql.cursors

db = pymysql.connect(
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    user='st4',
    password = "REPLACE_WITH_REAL_PASSWORD",
    database='st-onl',  # ← именно эта база!
    charset='utf8mb4'
)

cursor = db.cursor(pymysql.cursors.DictCursor)
cursor.execute('SELECT * FROM students')
data = cursor.fetchall()

# for student in data:
#     print(student['second_name'])

cursor.execute('SELECT * FROM students WHERE id = 53')
data2 = cursor.fetchone()
print(data2)

# query = f"SELECT * FROM students WHERE name = '{0}' and second_name = '{1}'"
# cursor.execute(query.format(input('name'), input('second_name')))
# print(cursor.fetchall())
# query = f"SELECT * FROM students WHERE name = %s and second_name = %s"
# cursor.execute(query, (input('name'), input('second_name')))
# print(cursor.fetchall())

# cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Azis', 'Derise','1')")
# cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Susi', 'Musi','1')")
# db.commit()

#cursor.execute("SELECT * FROM students WHERE group_id = 1") - проверил, что добавились новые сроки с Azis и Susi
#(cursor.fetchall())
# cursor.execute("INSERT INTO students (name, second_name, group_id) VALUES ('Ginger', 'Lusi','1')")
# student_id = cursor.lastrowid
# cursor.execute(f"SELECT name FROM students WHERE id = {student_id}")
# print(cursor.fetchone())
insert_query = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query, [
        ('Ging', 'Lusiner','1'),
        ('Ginger1', 'Lusi1','1')
    ]
)
select_query = '''
SELECT *
FROM students
WHERE name = 'George'
AND second_name = 'Washington'

'''
cursor.execute(select_query)
print(cursor.fetchall())

db.commit()
db.close()