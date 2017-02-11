#Hieu Dao-Tran 24353293 and Kelsey Lee 41441338. Lab Sec 5. Assignment 9

print('C1-----------------------')
print()

NUMBER_OF_STUDENTS = 200
NUMBER_OF_QUESTIONS = 20
NUMBER_OF_CHOICES = 4  # 3 choices is A/B/C, 4 choices is A/B/C/D, 5 is A/B/C/D/E

from random import randrange
from random import choice
from collections import namedtuple

def generate_answers()-> str:
    '''Returns a string form of the random answers to test'''
    choices = ['A', 'B', 'C', 'D']
    result = ''
    for answer in range(NUMBER_OF_QUESTIONS):
        result += choice(choices)
    return result
print(generate_answers())

ANSWERS = generate_answers()

print()
print('C2&C3-----------------------')
print()

Student = namedtuple('Student', 'name answers scores total')

def random_student_id() -> str:
    '''Returns an ID num in string form'''
    i_d = ''
    for num in range(7):
        i_d += str(randrange(0, 10))
    return i_d

def gather_scores(s: str)-> list:
    '''Returns a list of 1's and 0's'''
    scores = []
    for question in range(len(ANSWERS)):
        if s[question] == ANSWERS[question]:
            scores.append('1')
        else: scores.append('0')
    return scores

def gather_total(l: list) -> int:
    '''Returns number of 1's found in list'''
    return l.count('1')

def student_total(S: Student)-> int:
    '''Returns Student's total'''
    return S.total

def random_students(n: int) -> list:
    '''Returns list of Student namedtuple'''
    sclass = []
    average = 0
    for students in range(0, n):
        answers = generate_answers()
        scores = gather_scores(answers)
        sclass.append(Student(random_student_id(), answers, scores ,
                              gather_total(scores)))
        average += gather_total(scores)
    print('AVERAGE--------------------')
    print(average/n)
    print()
    sclass.sort(key=student_total, reverse=True)
    print('ID NUMS(TOP 10)----------------------')
    for id_num in sclass[:10]:
        print(id_num.name)
    print()
    return sclass
print(random_students(20))

print()
print('C4--------------------------')
print()

def generate_weighted_student_answer(s: str)-> str:
    '''Returns a student's answer'''
    choices = ['A', 'B', 'C', 'D']
    for amount in range(0, 8):
        choices.append(s)
    return choice(choices)
print(generate_weighted_student_answer('C'))
print()

def random_students2(n: int) -> list:
    '''Returns list of student namedtuple with better scores'''
    sclass = []
    average = 0
    for students in range(0,n):
        str_answer = ''
        for index in ANSWERS:
            studentanswers = generate_weighted_student_answer(index)
            str_answer += studentanswers
        scores = gather_scores(str_answer)
        sclass.append(Student(random_student_id(), str_answer, scores,
                                gather_total(scores)))
        average += gather_total(scores)
    print('Average Score-----------------')
    print(average/n)
    print()
    print('TOP 10 ID-NUMS------------------')
    sclass.sort(key=student_total, reverse=True)
    for num_id in sclass[:10]:
        print(num_id.name)
    return sclass
print(random_students2(25))

print()
print('C5------------------------')
print()

def question_weights(l: list) -> list:
    '''Returns a list with numbers showing incorrect answers'''
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for question in range(len(ANSWERS)):
        for Student in l:
            if Student.answers[question] != ANSWERS[question]:
                nums[question] = nums[question] + 1
    return nums
print('List of Incorrect answers for each question \n', question_weights(random_students2(10)))
weight_points = question_weights(random_students2(10))
student_constant = random_students2(10)

def Student_weighted_score(S: Student, l: list)-> Student:
    '''Returns new student record with changed score'''
    total_score = 0
    for question in range(len(ANSWERS)):
        if S.scores[question] == '1':
            total_score += l[question]
    return Student(S.name, S.answers, S.scores, total_score)

new_students = []
for student in student_constant:
    new_students.append(Student_weighted_score(student, weight_points))
new_students.sort(key=student_total, reverse=True)
for newstudent in new_students:
    print(newstudent)
    
print()
print('D1A-------------------------')
print()

def calculate_GPA(l: list) -> int:
    '''Returns GPA calculated'''
    GPA = 0
    for grade in l:
        if grade == 'A':
            GPA += 4
        elif grade == 'B':
            GPA += 3
        elif grade == 'C':
            GPA += 2
        elif grade == 'D':
            GPA += 1
        elif grade == 'F':
            GPA += 0
    return GPA/ len(l)
assert calculate_GPA(['A', 'C', 'A', 'B', 'A', 'F', 'D']) == 2.5714285714285716
print(calculate_GPA(['A', 'B', 'F', 'A', 'C', 'A', 'F']))

print()
print('D1B---------------------------')
print()

def calculate_GPA2(l: list) -> int:
    '''Returns GPA calculated without if statements'''
    Grades ={
        'A+': 4.3,
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'D-': .7,
        'F+': .3,
        'F': 0
        }
    GPA = 0
    for num in l:
        GPA += (Grades[num])
    return GPA /len(l)
assert calculate_GPA2(['A', 'C', 'A', 'B', 'A', 'F', 'D']) == 2.5714285714285716
print(calculate_GPA2(['A', 'B', 'F', 'A', 'C', 'A', 'F']))

print()
print('D2-------------------------')
print()

def flatten_2D_list(l: list) -> list:
    '''Returns a new list that is not a 2D list'''
    new = []
    for lists in l:
        for thing in lists:
            new.append(thing)
    return new
assert flatten_2D_list([[1, 3, 2], [3, 5, 1], [7, 5, 1], [3, 2], [9, 4]]) == [1, 3, 2, 3, 5, 1, 7, 5, 1, 3, 2, 9, 4]

print()
print('D3A--------------------------')
print()

L = ['If', 'you', '432234', 'did', 'the', '9834234', 'exercise', 'correctly', '534523423', 
		 'this', 'should', '1044323', 'be', 'readable']

def skip_every_third_item(l: list):
    '''Prints items from list skipping every third item'''
    newL = list(l)
    del newL[2::3]
    for item in newL:
        print(item)
    return
skip_every_third_item(L)

print()
print('D3B--------------------------')
print()


def skip_every_nth_item(l: list, n: int):
    '''Prints a list with skipped n values'''
    newL = list(l)
    del newL[n-1:: n]
    for item in newL:
        print(item)
    return
skip_every_nth_item(L, 3)

print()
print('D4A---------------------------')
print()

work_week = ['Bob', 'Jane', 'Kyle', 'Larry', 'Brenda', 'Samantha', 'Bob', 
             'Kyle', 'Larry', 'Jane', 'Samantha', 'Jane', 'Jane', 'Kyle', 
             'Larry', 'Brenda', 'Samantha']

def tally_days_worked(l: list) -> dict:
    '''Turns list in a dictionary with worker and amount of times checked in'''
    workers = {}
    for worker in l:
        workers[worker] = workers.get(worker, 0) + 1
    return workers
workers = tally_days_worked(work_week)
print(workers)

print()
print('D4B-------------------------')
print()

hourly_wages = {'Kyle': 13.50, 'Brenda': 8.50, 'Jane': 15.50, 'Bob': 30.00, 'Samantha': 8.50, 'Larry': 8.50, 'Huey': 18.00}
def pay_employees(w: dict, h: dict):
    '''Prints out employees payment'''
    print('Kyle will be paid $', w['Kyle'] * 8 * h['Kyle'],
          'for 24 hours of work at $13.50 per hour.')
    print('Brenda will be paid $', w['Brenda'] * 8 * h['Brenda'],
          'for 16 hours of work at $8.50 per hour')
    print('Larry will be paid $', w['Larry'] * 8 * h['Larry'],
          'for 24 hours of work at $8.50 per hour.')
    print('Bob will be paid $', w['Bob'] * 8 * h['Bob'],
          'for 16 hours of work at $30.00 per hour.')
    print('Samantha will be paid $', w['Samantha'] * 8 * h['Samantha'],
          'for 24 hours of work at $8.50 per hour.')
    print('Jane will be paid $', w['Jane'] * 8 * h['Jane'],
          'for 32 hours of work at $15.50 per hour.')
pay_employees(workers, hourly_wages)

print()
print('D5-------------------------')
print()

def reverse_dict(d : dict) -> dict:
    '''Reverse dictionary values'''
    d = dict((v,k) for k, v in d.items())
    return d
print(reverse_dict({'a': 'one', 'b': 'two', 'c': 'three',
                    'd': 'four', 'e': 'five', 'f': 'six'}))
