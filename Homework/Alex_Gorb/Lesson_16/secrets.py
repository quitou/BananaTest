import pymysql
import pymysql.cursors
from Homework.Alex_Gorb.Lesson_16 import creds
import os
import dotenv

dotenv.load_dotenv(override=True)

db = pymysql.connect(
    host=creds.host,
    port=creds.port,
    user=os.getenv('DB_USER'),
    password=os.getenv('DB_PASSW'),
    database=creds.database,  # ← именно эта база!
    charset=creds.charset
)

cursor = db.cursor(pymysql.cursors.DictCursor)
cursor.execute('SELECT * FROM students')
data = cursor.fetchall()