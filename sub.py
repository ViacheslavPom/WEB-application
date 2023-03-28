subject_list = ['Авторский стиль', 'Алгебра', 'Английский язык', 'Астрономия', 'Биология', 'Биосфера и человечество',
                'Введение в астрономию', 'Вводный курс химии', 'Видеоблогинг', 'Второй иностранный язык', 'География',
                'Геометрия', 'Дополнительные главы математики', 'Естествознание', 'Журналистика и медиа',
                'За страницами учебника истории', 'Зарубежная литература', 'ИЗО', 'Избранные вопросы математики',
                'Избранные вопросы химии', 'Индивидуальный проект', 'Информатика', 'Информационные технологии',
                'Информационные технологииПроектная и исследовательская деятельность', 'История', 'Китайский язык',
                'Классный час', 'Комплексный анализ текста',
                'Лабораторный практикум с элементами решения задач по физике', 'Литература', 'МХК', 'Математика',
                'Материальная история человеческой цивилизации ', 'Медийная информационная среда',
                'Метапредметные курсы: Техника. Искусство. Общество. Природа.',
                'Микробиология с элементами биотехнологий', 'Музыка', 'ОБЖ', 'ОДНКНР', 'Обществознание',
                'Ораторское мастерство', 'Основы мультипликации и Flash анимации',
                'Основы поэтики художественного слова', 'Основы предпринимательской деятельности',
                'Основы программирования на С++', 'Основы черчения', 'Основы экономики', 'Политическая сфера', 'Право',
                'Правовое регулирирование общественных отношений', 'Практикум по английскому языку',
                'Практикум по биологии', 'Практикум по информатике', 'Практикум по математике', 'Практикум по химии',
                'Приемы работы с общественным текстом', 'Программирование', 'Программирование на Python',
                'Проектная деятельность', 'Решение олимпиадных задач по математике',
                'Решение олимпиадных задач по русскому языку', 'Решение планиметрических задач', 'Родная литература',
                'Родной язык', 'Русский язык', 'Социология информационного общества', 'Социология медиапространства',
                'Спортивные игры', 'Теория вероятностей и статистика', 'Теория журнальных жанров', 'Технология',
                'Технология медиапроизводства', 'Физика', 'Физическая культура', 'Финансовая грамотность',
                'Функционнальная грамотность', 'Химия', 'Химия в задачах', 'Цифровая фото и видео студия',
                'Человек и его здоровье', 'Человек и его здоровьеИзбранные вопросы математики', 'Черчение',
                'Экология животных', 'Экология человека', 'Экономика']

import sqlite3
def data_subjects():
    # создаем подключение
    con = sqlite3.connect("mydb.db")
    # получаем курсор
    cursor = con.cursor()
    cursor.executemany('''
                            INSERT INTO subjects
                            (subject_id,
                            subject_name
                            )
                            VALUES (?, ?)
                            ''', Dsubject_list)
    con.commit()
    # query = con.execute("SELECT * FROM subjects")
    # print(query.fetchall())
    con.close()


if __name__ == '__main__':
    Dsubject_list = [(i + 1, item) for i, item in enumerate(subject_list)]
    data_subjects()