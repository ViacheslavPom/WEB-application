from app import db


class Users(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), index=True, unique=True)
    email = db.Column(db.String(20), index=True, unique=True)
    passwd = db.Column(db.String(20))

    def __repr__(self):
        return f'Пользователь {self.name}'


class Subjects(db.Model):
    subject_id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(30), index=True, unique=True)
    subject_name_eng = db.Column(db.String(30), index=True, unique=True)
    subj_min = db.Column(db.Integer)
    subj_max = db.Column(db.Integer)
    subj_value = db.Column(db.Integer)
    subj_general = db.Column(db.Boolean, default=True) # по умолчанию обязательный
    subj_10 = db.Column(db.Boolean, default=True)#по умолчанию для 10 класса

    def __repr__(self):
        return f'Предмет {self.subject_name}'


class Grades(db.Model):
    grade_id = db.Column(db.Integer, primary_key=True)
    grade_name = db.Column(db.String(3), index=True, unique=True)

    def __repr__(self):
        return f'Класс {self.subject_name}'


class Curriculum(db.Model):
    lesson_id = db.Column(db.Integer, primary_key=True)
    les_subject = db.Column(db.Integer, db.ForeignKey('subjects.subject_id'))
    les_grade = db.Column(db.Integer, db.ForeignKey('grades.grade_id'))
    les_number = db.Column(db.Integer)
    les_day = db.Column(db.Integer)

    def __repr__(self):
        return f'Урок {self.subject_name}'