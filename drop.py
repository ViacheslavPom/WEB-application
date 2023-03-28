import sqlite3
def droptable():
    # создаем подключение
    con = sqlite3.connect("mydb.db")
    # получаем курсор
    cursor = con.cursor()
    cursor.execute("DELETE FROM curriculum")
    con.commit()
    con.close()
droptable()