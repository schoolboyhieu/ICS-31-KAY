#Ashley Victoria Chang #51682178 and Hieu Dao-Tran #24353293 Lab sec. 5

print()
print()
print('---------- (c) ----------')
print()
print()

#C1.

def contains(s: str, t: str) -> bool:
    '''Returns True if second string is in first string'''
    return t in s

assert contains('banana', 'ana')
assert not contains('racecar','ck')

#C2.

def blank_counter(s: str) -> str:
    '''Translates punctuation marks to blanks'''
    
    no_punct  = str.maketrans('.,:;?!"',
                       '       ')
    return s.translate(no_punct)

def sentence_stats(s: str) -> None: 
    '''Prints length of characters, length in words, average length of each word'''
    print('Characters: ', len(s))
    print('Words: ', len(s.split()))

    total_amount_of_letters = 0

    new_split_sentence = blank_counter(s).split()

    for word in new_split_sentence:
        total_amount_of_letters += len(word)
    
    
    print('Average word length: ', total_amount_of_letters/len(s.split()))

sentence_stats('I love UCI') 




#C3.

def initials(s: str) -> str:
    '''Returns initials of full name'''
    result = ''
    s.split()
    x = s.split()
    for s in x:
        result+= s[0].upper()
    return result

assert initials('Bill Crosby') == 'BC'
assert initials('Guido van Rossum') == 'GVR'
assert initials('alan turing') == 'AT'


print()
print()
print('---------- (d) ----------')
print()
print()


#D1.

from random import randrange

for x in range(0,50):
    print(randrange(0,11))

for c in range(0,50):
    print(randrange(1,7))
print()

#D2.

def roll2dice () -> int:
    x = randrange(1,7)
    c = randrange(1,7)
    return x + c

for p in range(0,50):
    print(roll2dice())
print()

#D3.

def distribution_of_rolls(n: int) -> None:
    num = []
    for x in range(0, n):
        num.append(roll2dice())
    print('Distribution of dice roll')
    print()
    for x in range(2,13):
        print('{}:  {}({:2.1f}%) {}'.format(x, num.count(x), (num.count(x)/ n)*100,
                                      num.count(x)* '*'))
    print('-------------------------------------')
    print('         ', n, 'rolls')
distribution_of_rolls(200)
distribution_of_rolls(500)
print()
print('------------------E-----------------')

#E.1
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
def rotated_alphabet(n: int) -> list:
    nl = ALPHABET
    x = nl[n:] + nl[:n]
    return x
print(rotated_alphabet(1))
print()    
def Caesar_encrypt(s: str, n: int) -> str:
    table = str.maketrans(ALPHABET, rotated_alphabet(n))
    return s.lower().translate(table)
print(Caesar_encrypt('ABCDEFGH', 1))
print(Caesar_encrypt('Cartan Carte Carter Cartesian', 7))
print()

def Caesar_decrypt(s: str, n: int) -> str:
    table = str.maketrans(rotated_alphabet(n), ALPHABET)
    return s.lower().translate(table)
print(Caesar_decrypt('ABDBDUCEN',1))
print()
#E.2
print(Caesar_encrypt('Hi my name is hieu how are you doing?', 5))

print('----------------F--------------')

#F.1
def print_line_numbers(l:list)-> None:
    line = 1
    for s in l:
        print('{}: {}'.format(line, s))
        line += 1
        
print_line_numbers([ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        " ])
print()

#F.2
def stats(l: list) -> None:
    nw = []
    for x in l:
        for c in x:
            nw.append(c)
    p = float(len(nw)/len(l))
    nl = []
    for x in l:
        if x != ' ':
            nl.append(x)
    n = float(len(nw)/len(nl))
    print('{str(:7.1f)} lines in the list'.format(len(l)))
    print('{str(:7.1f)} empty lines'.format(l.count(' ')))
    print('{str(:7.1f)} average characters per line'.format(p))
    print('{str(:7.1f)} average characters per non-empty line'.format(n))
    
stats([ "Four score and seven years ago, our fathers brought forth on",
 "this continent a new nation, conceived in liberty and dedicated",
        "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        "," "])
print()

#F.3
def list_of_words(l: list) -> list:
    result = []
    for x in l:
     table = x.maketrans(':;"!@#$%^&*()_\[].,/',
                         '                    ')
     result.append(x.translate(table).split())
    return result
print(list_of_words([ "Four score and seven years ago, our fathers brought forth on",
  "this continent a new nation, conceived in liberty and dedicated",
  "to the proposition that all men are created equal.  Now we are",
  "   engaged in a great 		civil war, testing whether that nation, or any",
  "nation so conceived and so dedicated, can long endure.        "," "]))


                                                            
