# Hieu Dao-Tran 24353293 and Jose Gomez 47818875 Lab 4 assignment

#
#Part c
# 
def test_number(n: int, s: str) ->bool:
    '''Tells us if the argument is true or false'''
    if n %2 == 0 and s == 'even':
        return True
    if n %2 != 0 and s == 'odd':
        return True
    if n > 0 and s == 'positive':
        return True
    if n < 0 and s == 'negative':
        return True
    else: return False
    return True or False
assert test_number(14, 'even')
assert not test_number(100, 'odd')
assert test_number(33, 'positive')
assert not test_number(100, 'negative')
print()

#
# Part C.2
#
def display() -> None:
    '''Prints out every character in argument'''
    m= input('Enter a word:')
    for n in m:
        print(n)
    return None
display()
print()

#
# Part C.3
#

def square_list(n: list) -> None:
    '''Prints out each integer squared'''
    for j in n:
        print(j**2)
    return None
square_list([2,3,4,10])
print()

#
# Part C.4
#

def match_first_letter(y: str, k: list) -> None:
    '''Prints out the string with specificed character'''
    for x in k:
        if x[0] == y:
            print(x)
    return None
match_first_letter('I', ['Iron Man', 'Iron Man 2', 'The Avengers', 'Superman',
                         'I am Legend'])
print()

#
#Part C.5
#
def match_area_code(t: list, n: list) -> None:
    '''Prints phone numbers who's area code matches argument'''
    for x in n:
        for j in t:
            if x[1:4] == j:
                print(x)
match_area_code(['949', '714'], ['(714)824-1234',
                                 '(419)312-8732', '(949)555-1234'])
print()

#
#Part C.6
#
def match_area_codes(t: list, n: list) -> None:
    '''Returns list with matching numbers'''
    result = []
    for x in n:
        for j in t:

            if x[1:4] == j:
                result.append(x)
    return result
print(match_area_codes(['949', '714'], ['(714)824-1234',
                                 '(419)312-8732', '(949)555-1234']))
print()

#
#Part D.1
#
def is_vowel(x: str)-> None:
    '''Returns true or false if argument is a vowel'''
    l = ['a', 'e', 'i' ,'o','u','A','E','I','O','U']
    return x in l
assert is_vowel('a')
assert is_vowel('e')
print()

#
#Part D.2
#
def print_nonvowels(s: str) -> None:
    '''Prints nonvowels'''
    for x in s:
        if is_vowel(x) != True:
            print(x) 
    return
assert not print_nonvowels('cool')
assert not print_nonvowels('Hieu')
print_nonvowels('word')
print()

#
#Part D.3
#
def nonvowels(l: str) -> str:
    '''Returns string that contains all nonvowels'''
    result = ""
    for x in l:
        if is_vowel(x) != True:
            result+=x
    return result
assert nonvowels('word')
assert nonvowels('cool')
print(nonvowels('MynameisjosebecauseIamjose!@#@!$!$@'))
print()

#
#Part D.4
#
def consonants(c: str) -> str:
    '''Returns a string with only consonants'''
    result2 = ""
    long_string = ['q','z','w','s','x','d','c','r','f','v'
        ,'t','g','b','y','h','n','j','m','k','l','p']
    for x in c:
        if x in long_string:
            result2 += x
    return result2
print(consonants('hi1!'))
print()

#
#Part D.5
#
def select_letters(o:str, p: str) -> str:
    '''Returns strings with selective argument'''
    string_consonants = ""
    string_vowels = ""
    if o == 'v':
        for w in p:
            if is_vowel(w):
                string_vowels += w
        return string_vowels
    elif o == 'c':
        for x in p:
            if consonants(x):
                string_consonants += x
        return string_consonants
    else:
        return ''
print(select_letters('p', 'joseismiserable'))        
print()

#
#Part D.6
#
def hide_vowels(s: str) -> str:
    '''Replaces vowels with hyphens in the argument'''
    hyphen = ""
    for x in s:
        if consonants(x):
            hyphen += x
        elif is_vowel(x):
            hyphen += '-'
    return hyphen
print()

#
#Part E
#
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')

R1 = Restaurant("Taillevent", "French", "343-3434", "Escargots", 24.50)
R2 = Restaurant("La Tour D'Argent", "French", "343-3344", "Ris de Veau", 48.50)
R3 = Restaurant("Pascal", "French", "333-4444", "Bouillabaisse", 32.00)
R4 = Restaurant("Thai Touch", "Thai", "444-3333", "Mee Krob", 10.95)
R5 = Restaurant("Thai Dishes", "Thai", "333-4433", "Paht Woon Sen",  8.50)
R6 = Restaurant("Thai Spoon", "Thai", "334-3344", "Mussamun", 9.00)
R7 = Restaurant("McDonald's", "Burgers", "333-4443", "Big Mac", 3.95)
R8 = Restaurant("Burger King", "Burgers", "444-3344", "Whopper", 3.75)
R9 = Restaurant("Wahoo's", "Fish Tacos", "443-4443", "Mahi Mahi Burrito", 7.50)
R10 = Restaurant("In-N-Out Burger", "Burgers", "434-3344", "Cheeseburger", 2.50)
R11 = Restaurant("The Shack", "Burgers", "333-3334", "Hot Link Burger", 4.50)
R12 = Restaurant("Gina's", "Pizza", "334-4433", "Combo Pizza", 12.95)
R13 = Restaurant("Peacock, Room", "Indian", "333-4443", "Rogan Josh", 12.50)
R14 = Restaurant("Gaylord", "Indian", "333-3433", "Tandoori Chicken", 13.50)
R15 = Restaurant("Mr. Chow", "Chinese", "222-3333", "Peking Duck", 24.50)
R16 = Restaurant("Chez Panisse", "California", "222-3322", "Grilled Duck Breast", 25.00)
R17 = Restaurant("Spago", "California", "333-2222", "Striped Bass", 24.50)
R18 = Restaurant("Sriped Bass", "Seafood", "333-2233", "Cedar Plank Salmon", 21.50)
R19 = Restaurant("Golden Pagoda", "Chinese", "232-3232", "Egg Foo Young", 8.50)
R20 = Restaurant("Langer's", "Delicatessen", "333-2223", "Pastrami Sandwich", 11.50)
R21 = Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50)
R22 = Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50)
R23 = Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50)
R24 = Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.50)
R25 = Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50)
R26 = Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) 


RL = [R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11, R12, R13, R14, R15, R16,
	R17, R18, R19, R20, R21, R22, R23, R24, R25, R26]
print()
#
#Part E
#
def Restaurant_change_price(o: object, n: float) -> object:
    '''Changes price of due to argument'''
    RL = o._replace(price= o.price + n)
    return RL
print()

#
#Part F.1
#
def alphabetical(L: list) -> list:
    '''Returns list in alphabetical order'''
    L.sort(key=None)
    return L
print()

#
#Part F.2
#
def alphabetical_names(L: list) -> list:
    '''Returns list of names in alphabetical order'''
    names = []
    L.sort(key=None)
    for x in L:
        names.append(x.name)
    return names
print()

#
#Part F.3
#
def all_Thai(L: list) -> list:
    '''Returns list of all thai restaurants'''
    thai = []
    for x in L:
        if x.cuisine == 'Thai':
            thai.append(x)
    return thai
print()

#
#Part F.4
#
def select_cuisine(L: list, c: str) -> list:
    '''Returns list of all restaurant with specified cuisine'''
    all_types = []
    for x in L:
        if x.cuisine == c:
            all_types.append(x)
    return all_types
print()

#
#Part F.5
#
def select_cheaper(L: list, n: float) -> list:
    '''Returns list of all restaurants with less than the given argument'''
    cheaper = []
    for x in L:
        if x.price < n:
            cheaper.append(x)
    return cheaper
print()

#
#Part F.6
#
def average_price(L: list) -> float:
    '''Returns the average price of list'''
    total = []
    for x in L:
        total.append(x.price)
    return sum(total)/len(L)
print()

#
#Part F.7
#
print(average_price(select_cuisine(RL, 'Indian')))
print()

#
#Part F.8
#
print(average_price(select_cuisine(RL, 'Chinese')+
                    select_cuisine(RL,'Thai')))
print()

#
#Part F.9
#
print(select_cheaper(RL, 15.00))
print()

#
#Part G
#
import tkinter
my_window=tkinter.Tk()
my_canvas=tkinter.Canvas(my_window,width=500,height=500)
my_canvas.pack()
def create_rectangle_from_center(x: int, y: int, h: int, w: int) -> None:
    '''Creates a rectangle from the center'''
    my_canvas.create_rectangle(x - w/2, y - h/2, x + w/2, y + h/2)
    return
create_rectangle_from_center(200, 200, 100, 100)
tkinter.mainloop()

    
