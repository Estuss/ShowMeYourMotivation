import sqlite3

def create():
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
       userid INT PRIMARY KEY,
       fname TEXT,
       lname TEXT,
       gender TEXT);
    """)
    conn.commit()

def sqlrequest(request):
    cur.execute(request)
    conn.commit()

def clear():
    cur.execute("DROP TABLE IF EXISTS users;")

def sqlwrite():
    cur.execute("SELECT * FROM users;")
    all_results = cur.fetchall()
    print(all_results)

k=0
conn = sqlite3.connect('orders.db')
cur = conn.cursor()
clear() #убрать если не надо очищать бд
create()
print("Чтобы добавить человека в базу данных введите имя, фамилию и пол через запятую")
while True:
    txt = input("Добавить ")
    values = txt.split(",")
    sqlrequest("INSERT INTO users(userid, fname, lname, gender) VALUES('" + str(k) + "', '" + values[0] + "', '" + values[1] + "','" + values[2] + "');")
    k+=1
    sqlwrite()
