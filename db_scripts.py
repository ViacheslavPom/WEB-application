import sqlite3


def data_1():
    # создаем подключение
    con = sqlite3.connect("mydb.db")
    # получаем курсор
    cursor = con.cursor()
    lessons = [

    ]
    cursor.executemany('''
                        INSERT INTO subjects
                        (subject_id, 
                        subject_name, 
                        subject_name_eng, 
                        subj_min,
                        subj_max,
                        subj_value,
                        subj_general)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''', lessons)

    query = con.execute("SELECT * FROM lessons")
    print(query.fetchall())
    con.commit()
    con.close()


def data_grades():
    # создаем подключение
    con = sqlite3.connect("mydb.db")
    # получаем курсор
    cursor = con.cursor()
    grades = [str(num)+letter for num in range(5,12) for letter in 'АБВГ']
    grades = [(i, x) for i, x in enumerate(grades)]

    cursor.executemany('''
                        INSERT INTO grades
                        (grade_id, 
                        grade_name)
                        VALUES (?, ?)''', grades)

    query = con.execute("SELECT * FROM grades")
    print(query.fetchall())
    con.commit()
    con.close()




def data_subjects():
    # создаем подключение
    con = sqlite3.connect("mydb.db")
    # получаем курсор
    cursor = con.cursor()
    subjects = [
        (1, 'Русский язык', 'russian', 1, 2, 1, True),
        (2, 'Математика', 'math', 3, 5, 5, True),
        (3, 'Английский язык', 'english', 6, 6, 6, True),
        (4, 'Второй иностранный', 'second_language', 1, 2, 1, False),
        (5, 'Информатика', 'IT', 2, 4, 4, False),
        (6, 'Физика', 'physics', 2, 5, 5, False),
        (7, 'Биология', 'biology', 2, 5, 5, False),
        (8, 'Химия', 'chemistry', 2, 4, 4, False),
        (9, 'Литература', 'literature', 3, 3, 3, True)
    ]
    cursor.executemany('''
                        INSERT INTO 
                        (subject_id, 
                        subject_name, 
                        subject_name_eng, 
                        subj_min,
                        subj_max,
                        subj_value,
                        subj_general)
                        VALUES (?, ?, ?, ?, ?, ?, ?)''', subjects)

    query = con.execute("SELECT * FROM subjects")
    print(query.fetchall())
    con.commit()
    con.close()

if __name__ == '__main__':
    data_grades()