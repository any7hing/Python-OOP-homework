class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.rate = [].append(name)
    
    def __str__ (self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.count_grades(self.grades)}\nКурсы в процессе изучения: {" ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'
        return res
    
    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress:
            if course in lecturer.L_grades:
                lecturer.L_grades[course] += [grade]
            else:
                lecturer.L_grades[course] = [grade]
        else:
            return 'Ошибка'
        
    def count_grades(self,grades):
        result = 0
        for course,grade in grades.items():
            result += sum(grade)/len(grade)
        result = result/len(grades)
        return result
    
    def __lt__(self,other):
        if not isinstance(other,Student):
            print('Нельзя сравнивать разные классы')
            return
        return self.count_grades(self.grades) < other.count_grades(other.grades)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        self.L_grades = {}
        self.courses_attached = []

    def count_grades(self,L_grades):
        res = 0
        for courses,list_grades in L_grades.items():
            res += sum(list_grades)/len(list_grades)
        return (res/len(L_grades))
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.count_grades(self.L_grades)}'
        return res

    def __lt__(self,other):
        if not isinstance(other,Lecturer):
            print('Нельзя сравнивать разные классы')
            return
        return self.count_grades(self.L_grades) < other.count_grades(other.L_grades)

class Reviever(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
# Создаем экземпляры классов
Arthas = Student('Arthas','Menetil','man')
Terenas = Student('Terenas', "Menetil", 'man')
Sylvanas = Reviever('Sylvanas','Windrunner')
Trall = Reviever('Trall','Son_of_Durotan')
Lich = Lecturer('Lich','King')
Sindragosa = Lecturer('Sindragosa', 'Dragon')

# Операции с классами, Заполняем данные
Arthas.courses_in_progress += ['Python']
Arthas.finished_courses += ['Git']
Terenas.courses_in_progress += ['Python']
Terenas.finished_courses += ['Java']
Sylvanas.courses_attached += ['Python']
Trall.courses_attached += ['Python']
Lich.courses_attached += ['Python']
Sindragosa.courses_attached += ['Python']

# Ревьюеры ставят оценки студентам
Trall.rate_hw(Arthas,"Python", 9)
Trall.rate_hw(Arthas,"Python", 10)
Sylvanas.rate_hw(Terenas,"Python", 7)
Sylvanas.rate_hw(Terenas,"Python", 4)
# Сравниваем и выводим студентов
# print(Arthas)
# print(Terenas)
# print(Arthas < Terenas)

#Студенты оценивают Лекторов
Arthas.rate_hw(Lich,'Python', 7)
Arthas.rate_hw(Sindragosa,'Python', 10)
Terenas.rate_hw(Lich,'Python', 5)
Terenas.rate_hw(Sindragosa,'Python', 10)
# Сравниваем и выводим Лекторов
# print(Lich)
# print(Sindragosa)
# print(Lich<Sindragosa)

# Создаем и заполняем списки студентов и лекторов для 4 задания. Т.К. В лекции не обьясняли как ложить в список экземпляры при инициализации.
student_list = []
lekturer_list = []
student_list.append(Arthas)
student_list.append(Terenas)
lekturer_list.append(Lich)
lekturer_list.append(Sindragosa)

# 4 задание, 1 функция - считаем средний бал по курсу у студентов
def homework_grades(student_list, course_name):
    buff = 0
    for i in range(len(student_list)):
        for name,value in student_list[i].grades.items():
            if name == course_name:
                buff += sum(value)
            else:
                return ('Такого курса нет у студентов')
    buff = buff/len(student_list)
    res = f'Средний балл у студентов по курсу: {course_name}: {buff}'
    return  res
# print(homework_grades(student_list,'Python'))

# 4 задание, 2 функция - считаем средний балл у лекторов
def lekturer_grades(lekturer_list,course_name):
    buff = 0
    for i in range(len(lekturer_list)):
        for name,value in lekturer_list[i].L_grades.items():
            if name == course_name:
                buff +=sum(value)
            else:
                return('Такого курса нет')
    buff = buff/len(lekturer_list)
    res = f'Средний балл у лекторов по курсу: {course_name}: {buff}'
    return res
# print(lekturer_grades(lekturer_list,'Python'))
