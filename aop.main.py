from aop import *
pca = [('deduction',afterLog), ('deduction',beforeLog),
    ('salary',afterPostCondition), ('salary',afterLog),
    ('salary',beforeLog), ('add_exam', beforePreCondition),
    ('average', afterPostCondition)]

class Student:
    def __init__(self, name, age, cv):
        self.name = name
        self.age = age
        self.cv = cv
    def add_exam(self, name, mark):
        self.cv[name] = mark
    def average(self):
        return sum(self.cv.values())/len(self.cv)

class Worker:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.daily = salary
    def deduction(self, percentage):
        return self.daily*percentage/100
    def salary(self,percentage):
        return (self.daily-self.deduction(percentage))*365

Student = weaving(Student, pca)
Worker = weaving(Worker, pca)

if __name__ == '__main__':
    w = Worker('jane', 29, 30)
    s = Student('bob', 22, {'lp': 24, 'tsp':30})
    print(w.deduction(22))
    print(w.salary(35))
    print(s.average())
    s.add_exam('pa', 18)
    print(s.average())
