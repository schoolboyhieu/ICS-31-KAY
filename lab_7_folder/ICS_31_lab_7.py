# Hieu Dao-Tran 24353293 and Danny Nguyen 46002992 Lab Sec 5. Lab Assignment 7.

print('*'*7, 'C', '*'*7)
print()
from random import randrange

def random_names(n: int)-> list:
    infile = open('surnames.txt', 'r')
    surnames = infile.read()
    surnamelist = surnames.split()
    surnameNEW = []
    surname1 = []
    surname2 = []
    for c in range(1000):
        surnameNEW.append(surnamelist[c*4])
    for x in surnameNEW:
        x = x.lower()
        surname1.append(x)
    for q in surname1:
        p = q[0].upper() + q[1:]
        surname2.append(p)
    infile2 = open('malenames.txt', 'r')
    infile3 = open('femalenames.txt', 'r')
    malenames = infile2.read()
    femalenames = infile3.read()
    male = malenames.split()
    female = femalenames.split()
    bothgender = []
    realgender = []
    thisgender = []
    final = []
    for p in range(1000):
        bothgender.append(male[p*4])
        bothgender.append(female[p*4])
    for x in bothgender:
        x = x.lower()
        realgender.append(x)
    for x in realgender:
        c = x[0].upper() + x[1:]
        thisgender.append(c)
    for x in range(n):
        final.append((thisgender[randrange(0,2000)]+ ' '
                      + surname2[randrange(0, 1000)]))
    return final
print(random_names(5))
print()

print('*'*7, 'D', '*'*7)
print()

# d1
alpha = 'abcdefghijklmnopqrstuvwxyz'

def new_alphabet(n:int)-> str:
    new = alpha
    p = new[n:] + new[:n]
    return p

def Caesar_break(s: str) -> str:
    infile = open('wordlist.txt', 'r')
    dic = infile.read()
    dictionary = dic.lower().split()
    empty = []
    for x in range(0, 26):
        table = str.maketrans(alpha, new_alphabet(x))
        empty.append(s.lower().translate(table))
    new = ""
    for x in empty:
        for p in x.split():
            if p in dictionary:
                new += p + " "
    return new

# d2
print("Danny's message: 'smolkvv smolobq kckz occoxdskv'")
print()
print(Caesar_break('smolkvv smolobq kckz occoxdskv'))
print()
print("Hieu's message: 'jhyahu jhyal jhyaly jhyalzphu'")
print()
print(Caesar_break('jhyahu jhyal jhyaly jhyalzphu'))
print()

print('*'*7, 'E', '*'*7)
print()

# e1 & e2
def count_empty_lines(s: list):
   ''' Takes a list of string and returns a list of empty lines '''
   empty_line_list = [ ]
   for a in s:
       a = a.strip(" ")
       if a == "":
          empty_line_list.append(a)
   return empty_line_list

def list_nonempty_lines(s: list):
   ''' Takes a list of string and returns a list of non empty lines '''
   result = [ ]
   for i in s:
      if i.strip(" ") != "":
         result.append(i)
   return result

def stats(s: list):
    ''' Takes a list of string and returns the hashtag comments below '''
    z = ('{:7.0f} lines in the list'.format(len(s))) # Lines in the list
    b = ('{:7.0f} empty lines'.format(len(count_empty_lines(s)))) # Count number of empty lines
    result = [ ]
    for i in s:
        a = len(i)
        result.append(a)
    total = sum(result)/len(s)
    c = ('{:7.1f} average characters per line'.format(total)) # Average characters/line
    result2 = [ ]
    for q in list_nonempty_lines(s):
       result2.append(len(q))
    total_non_empty_lines = sum(result2)/(len(s)-len(count_empty_lines(s)))
    d = ('{:7.1f} average characters per non empty line'.format(total_non_empty_lines)) # Average characters/non-empty line
    final = [z, b, c, d]
    final2 = ''
    for m in final:
       m = (str(m) + '\n')
       final2 += m
    return final2

def copyfile(s: str):
    infile_name = input("Please enter the name of the file to copy: ")
    infile = open(infile_name, 'r', errors = 'ignore')
    outfile_name = input("Please enter the name of the new copy:  ")
    outfile = open(outfile_name, 'w', errors = 'ignore')
    file = infile.read()
    file2 = file.split('\n')
    if s == 'line numbers':
        for i in range(len(file2)):
            outfile.write('{:5d}: {}'.format(i+1, file2[i]))
    elif s == 'Gutenberg trim':
        start = file.find('*** START')
        end = file.find('***** This file')
        outfile.write(file[start+1:end])
    elif s == 'statistics':
        outfile.write(stats(file2))
    else:
        print(file)
    infile.close()
    outfile.close()
