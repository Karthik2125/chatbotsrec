import pymysql
import pandas as pd
import sys

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Harshini@2127',
    database='srec'
)

cursor = conn.cursor()

try:

    df = pd.read_excel('C:\\Users\\harsh\\OneDrive\\Desktop\\CHAT_BOT\\proj chatbot\\Book6.xlsx')

    
    df = df.where(pd.notnull(df), None)

    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS srec.srectable12 (
        id INT AUTO_INCREMENT PRIMARY KEY,
        QUESTIONS TEXT,
        ANSWERS TEXT
    )
    """)
    print(df['ANSWERS'])


    for _, row in df.iterrows():
        cursor.execute("""
            INSERT INTO srec.srectable12 (QUESTIONS, ANSWERS)
            VALUES (%s, %s)
        """, (row['QUESTIONS'], row['ANSWERS']))

    conn.commit()
    print("Data inserted successfully!")

except Exception as e:
    print("Error:", e)

finally:
    cursor.close()
    conn.close()

sys.exit()
