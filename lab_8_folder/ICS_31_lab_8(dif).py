# Karthik Jagadeesan 72796420 and Hieu Dao-Tran 24353293.  ICS 31 Lab sec 5.  Lab asst 8.

def read_menu_with_count(s : str)->str:
    infile1 = open(s, 'r')
    mlist = []
    print(infile1)
    for l in infile1:
        newline = l.replace('\n', '')
        mlist.append(newline.split('\t'))
    
       
                
            
        
        
    print(mlist[1:])
        
        
print(read_menu_with_count('menu1.txt'))



def read_menu(s:str)->str:
    infile1 = open(s, 'r')
    mlist = []
    print(infile1)
    for l in infile1:
        newline = l.replace('\n', '')
        mlist.append(newline.split('\t'))
    print(mlist)

from collections import namedtuple
Dish = namedtuple('Dish', 'name price calories')
Dish_list = [Dish('pizza', '98', '863'), Dish('bigmac ','87', '989'), Dish('bigk', '97' ,'0909') ]

def write_menu(Dish_list: list, s : str):
    final = []
    infile1 = open(s,'w')
    for Dish in Dish_list:
        
        final += Dish 
        infile1.write(str(Dish) + '\n')
    print(infile1)
print(write_menu(Dish_list, 'menu789.txt'))

print('------d--------')

print('d1---------------')
Course = namedtuple('Course', 'dept num title instr units')
# Each field is a string except the number of units
ics31 = Course('ICS', '31', 'Intro to Programming', 'Kay', 4.0)
ics32 = Course('ICS', '32', 'Programming with Libraries', 'Thornton', 4.0)
wr39a = Course('Writing', '39A', 'Intro Composition', 'Alexander', 4.0)
wr39b = Course('Writing', '39B', 'Intermediate Composition', 'Gross', 4.0)
bio97 = Course('Biology', '97', 'Genetics', 'Smith', 4.0)
mgt1  = Course('Management', '1', 'Intro to Management', 'Jones', 2.0)

Student = namedtuple('Student', 'ID name level major studylist')
# All are strings except studylist, which is a list of Courses.
sW = Student('11223344', 'Anteater, Peter', 'FR', 'PSB', [ics31, wr39a, bio97, mgt1])
sX = Student('21223344', 'Anteater, Andrea', 'SO', 'CS', [ics31, wr39b, bio97, mgt1])
sY = Student('31223344', 'Programmer, Paul', 'FR', 'COG SCI', [ics32, wr39a, bio97])
sZ = Student('41223344', 'Programmer, Patsy', 'SR', 'PSB', [ics32, mgt1])
  
StudentBody = [sW, sX, sY, sZ]
SL = ['ics31','ics32','wr39a']

print(sW.level)
def Students_at_level(l : list, level : str)->  list:
    slist = []
    for s in l:
        if s.level == level:
            slist.append(s)
    return slist
print(Students_at_level(StudentBody, 'SO'))



print('d2----------------')

clist = ['ICS', 'PSB']

def Students_in_majors(l : list, c : list)-> list:
    slist = []

    for s in l:
        if s.major in c:
            slist.append(s)

    return slist
    
print(Students_in_majors(StudentBody,clist))


print('d3-----------------')
def Course_equals(c1: Course, c2: Course) -> bool:
    ''' Return True if the department and number of c1 match the department and
	     number of c2 (and False otherwise)
    '''
    if c1.dept == c2.dept:
        if c1. num == c2.num:
            return True
    return False
assert Course_equals(ics31, ics31) == True
print(Course_equals(ics31, ics31))
print()

def Course_on_studylist(c: Course, SL: 'list of Course') -> bool:
    ''' Return True if the course c equals any course on the list SL (where equality
	     means matching department name and course number) and False otherwise.
    '''
    if c in SL:
        return True
    return False
assert Course_on_studylist(ics31, SL) == False
print(Course_on_studylist(ics32, SL))
print()

def Student_is_enrolled(S: Student, department: str, coursenum: str) -> bool:
    ''' Return True if the course (department and course number) is on the student's
	     studylist (and False otherwise)
    '''
    for x in S.studylist:
        if department == x.dept:
            if coursenum == x.num:
                return True
    return False
assert Student_is_enrolled(sW, 'ICS', '31') == True
print(Student_is_enrolled(sW, 'Writing', '39B'))
print()
def Students_in_class(l: list, dname: str, cnum: str) -> list:
    result = []
    for x in l:
        if Student_is_enrolled(x, dname, cnum) == True:
            result.append(x)
    return result
print(Students_in_class(StudentBody, 'ICS', '31'))



print('d5-----------------')

imajors = ['CS', 'CSE', 'BIM', 'INFX', 'CGS', 'SE', 'ICS']
print('\n')
#Bullet 1

def ics_students(l : list)->list:
    
    lst = []
    
    for s in l:
        if s.major in imajors:
            lst.append(s)
    return lst
print(ics_students(StudentBody))
#Bullet 2
print()
def ics_names(l : list)->list:
    lst1 = []
    for s in l:
        if s.major in imajors:
            lst1.append(s.name)
    return lst1
print(ics_names(StudentBody))
print()
#Bullet 3
def ics_students_num(l : list)->list:
    
    lst = 0
    
    for s in l:
        if s.major in imajors:
            lst += 1
    return lst
print(ics_students_num(StudentBody))
print()
#Bullet 4, 5, 6
def ics_senior(l : list)->list:
    
    lst = []
    num = 0
    
    for s in l:
        if s.level == 'SR' and  s.major in imajors:
            lst.append(s.name)
            num += 1
    print(num)
    print(num/len(imajors)*100)
    return lst
    
print(ics_senior(StudentBody))
print()
#Bullet 7

def ics_fresh(l : list)->list:
    
    num = 0
    for s in l:
        if s.level == 'FR' and s.major in imajors and ics31 in s.studylist:
            num += 1
    return num
print(ics_fresh(StudentBody))
print()
#Bullet 8
def get_fresh(l: list)-> float:
    num = 0
    for s in l:
        if s.level == 'FR' and ics31 in s.studylist:
            num += 1
    return num
def ics_fresh_units(l : list)->float:
    
    num = 0
    for s in l:
        for x in s.studylist:
            if s.level == 'FR' and ics31 in s.studylist:
                num += x.units
    return num/get_fresh(l)
print(ics_fresh_units(StudentBody))
print()
            
        
        
