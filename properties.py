import datetime
import unittest

class Person:
    def __init__(self, name, lastname, birthday):
        self.name = name
        self.lastname = lastname
        self.birthday = birthday 

    def __repr__(self):
        items = list(self.__dict__.items())
        items.sort(key=lambda p: p[0])
        s = '{}('.format(self.__class__.__name__)
        for k,v in items:
            s += '{}={}, '.format(k,v)
        s = s[:-2] + ')'
        return s

class Student(Person):
    class _Descriptor:
        def __get__(self, instance, _):
            lst = list(map(lambda p: p[1], instance.grades.items()))
            return sum(lst)/len(lst)
    grade_average = _Descriptor()

    def __init__(self, name, lastname, birthday, grades={}):
        super(Student, self).__init__(name, lastname, birthday)
        self.grades = grades

    '''
    @property
    def grade_average(self):
        lst = list(map(lambda p: p[1], self.grades.items()))
        return sum(lst)/len(lst)
    '''

class Worker(Person):
    def __init__(self, name, lastname, birthday, pay_per_hour):
        super(Worker, self).__init__(name, lastname, birthday)
        self.pay_per_hour = pay_per_hour
    
        # Writing a custom metaclass instead?
        ps = [
            ('day_salary',8),
            ('week_salary', 8*5),
            ('month_salary', 8*5*4),
            ('year_salary', 8*5*4*12),
        ]

        for pname,ptimes in ps:
            def build_get_and_set(ptimes):
                '''
                def _get(self): return self.pay_per_hour*ptimes
                def _set(self,value): self.pay_per_hour=value/ptimes
                return _get, _set
                '''
            #setattr(self.__class__, pname, property(*build_get_and_set(ptimes)))
                class _Descriptor:
                    def __get__(self, instance, owner):
                        return instance.pay_per_hour*ptimes
                    def __set__(self, instance, value):
                        instance.pay_per_hour = value/ptimes
                return _Descriptor
            setattr(self.__class__, pname, build_get_and_set(ptimes)())

class Wizard(Person):
    '''
    ## Useless, to be fair ...
    def __init__(self, *args, **kwargs):
        super(Wizard, self).__init__(*args, **kwargs)
    '''

    '''
    @property
    def age(self):
        return (datetime.date.today()-self.birthday).days // 365
    @age.setter
    def age(self, value):
        self.birthday = datetime.date.today()-datetime.timedelta(days=value*365)
    '''

    class _Descriptor:
        def __get__(self, instance, owner):
            return (datetime.date.today()-instance.birthday).days // 365
        def __set__(self, instance, value):
            instance.birthday = datetime.date.today()-datetime.timedelta(days=value*365)

    age = _Descriptor()

class TestPerson(unittest.TestCase):
    def test___repr__(self):
        p = Person('Linus', 'Torvalds', datetime.date(2015,4,21))
        expected = 'Person(birthday=2015-04-21, lastname=Torvalds, name=Linus)'
        result = p.__repr__()
        self.assertEqual(expected, result)

class TestStudent(unittest.TestCase):
    def test_grade_average(self):
        gs = {'Math': 30, 'Kernels': 18, 'Computers': 22}
        s = Student('Linus', 'Torvalds', datetime.date(2015,4,21), gs)
        result = s.grade_average
        expected = 23.
        self.assertAlmostEqual(expected, result, places=0)

class TestWorker(unittest.TestCase):
    def test_get_day_salary(self):
        w = Worker('Linus', 'Torvalds', datetime.date(2015,4,21), pay_per_hour=300)
        self.assertEqual(w.day_salary, w.pay_per_hour*8)
    ## Very annoying to do. Anything better?
    '''
    def test_get_week_salary(self):
        w = Worker('Linus', 'Torvalds', datetime.date(2015,4,21), pay_per_hour=300)
        self.assertEqual(w.week_salary = w.pay_per_hour*8*5)
    def test_get_month_salary(self):
        w = Worker('Linus', 'Torvalds', datetime.date(2015,4,21), pay_per_hour=300)
        self.assertEqual(w.month_salary == w.pay_per_hour*8*5*4)
    def test_get_year_salary(self):
        w = Worker('Linus', 'Torvalds', datetime.date(2015,4,21), pay_per_hour=300)
        self.assertEqual(w.year_salary == w.pay_per_hour*8*5*4*12)

    def test_set_day_salary(self):
        w = Worker('Linus', 'Torvalds', datetime.date(2015,4,21), pay_per_hour=300)
        w.day_salary = 300
        self.assertAlmostEqual(w.pay_per_hour == w.day_salary/8, places=0)
    def test_set_week_salary(self):
        w = Worker('Linus', 'Torvalds', datetime.date(2015,4,21), pay_per_hour=300)
        w.week_salary = 300
        self.assertAlmostEqual(w.pay_per_hour == w.week_salary/5/8, places=0)
    def test_set_month_salary(self):
        w = Worker('Linus', 'Torvalds', datetime.date(2015,4,21), pay_per_hour=300)
        w.month_salary = 300
        self.assertAlmostEqual(w.pay_per_hour == w.month_salary/4/5/8, places=0)
    def test_set_year_salary(self):
        w = Worker('Linus', 'Torvalds', datetime.date(2015,4,21), pay_per_hour=300)
        w.year_salary = 300
        self.assertAlmostEqual(w.pay_per_hour == w.year_salary/12/4/5/8, places=0)
    '''

class TestWizard(unittest.TestCase):
    def test_aging(self):
        w = Wizard('Linus', 'Torvalds', datetime.date.today())
        self.assertEqual(w.age,0)
        w.age = 28
        self.assertEqual(w.birthday, datetime.date.today()-datetime.timedelta(days=28*365))
        w.age = 54
        self.assertEqual(w.birthday, datetime.date.today()-datetime.timedelta(days=54*365))

if __name__ == '__main__':
    unittest.main()
