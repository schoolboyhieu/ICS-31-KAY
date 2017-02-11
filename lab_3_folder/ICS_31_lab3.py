#Patrick Dumas 43391947 & Hieu Dao-Tran 24353293 Section 5, Assignment 3


#
#Part C.1
#
def abbreviate(a: str)->None:
    return a[:3]
   
 
assert abbreviate('January')=='Jan'
assert abbreviate('abril')=='abr'
print()

#C.2
def find_area_square(s: int)->int:
    return s**2
assert find_area_square(1) == 1
assert find_area_square(5) == 25
print()

#
#C.3
def find_area_circle(r: int)->int:
    return 3.14159*(r**2)
assert find_area_circle(1) == 3.14159
assert find_area_circle(5) == 78.53975
print()

#
#C.4
def print_even_numbers(e: list)->None:
   for number in e:
    if (number % 2) == 0:
        print(number)


print_even_numbers([2, 47, 31, 99, 20, 19, 23, 105, 710, 1004])       
print()

#
#c.5
def calculate_shipping(c: float)->None:
    if c<2: return(2.00)
    elif 2<=c and c<10: return(5.00)
    else: return(5+1.5*(c-10))
    
assert calculate_shipping(1.5) == 2.00
assert calculate_shipping(7) == 5.00
assert calculate_shipping(15) == 12.50
print()
'''
#
#Tkinter Time!!!!!
#c.6
import tkinter              # Load the library; do this just once per program

def create_square(x:int, y:int, l: int)-> None: 
    my_window = tkinter.Tk()    # Create the graphics window
    
    my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
    my_canvas.pack()            # Put the canvas into the window
    
    my_canvas.create_rectangle(x,y,x+l,y+l)
create_square(75, 75, 350)
   
#
#C.7
def create_circle(a:int, b:int, d: int)->None:
    my_window = tkinter.Tk()    # Create the graphics window
    
    my_canvas = tkinter.Canvas(my_window, width=500, height=500)  # Create a 500x500 canvas to draw on
    my_canvas.pack()            # Put the canvas into the window

    my_canvas.create_oval(a, b, a+d, b+d)
    
create_circle(50, 50, 300)
######
tkinter.mainloop()          # Combine all the elements and display the window
######
'''


#
# PART D

#D.1

from collections import namedtuple     # If this line is in your file already, you don't need it again
Restaurant = namedtuple('Restaurant', 'name cuisine phone dish price')
# Restaurant attributes: name, kind of food served, phone number, best dish, price of that dish
RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.55),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]




def restaurant_price(r: Restaurant)-> float:
    return r.price
assert restaurant_price(RC[0]) == 12.50
assert restaurant_price(RC[4]) == 5.55

#
#D.2

print()
print(RC) #To show the difference before and after sorting
RC.sort(key=restaurant_price)
print(RC)
print()


#
#D.3
#

def costliest(n: RC) -> str:
    n.sort(key=restaurant_price, reverse=True)
    return n[0].name
assert costliest(RC) == 'Noma'


#
#D.4
#


print(RC)
print(costliest(RC))

RC = [
    Restaurant("Thai Dishes", "Thai", "334-4433", "Mee Krob", 12.50),
    Restaurant("Nobu", "Japanese", "335-4433", "Natto Temaki", 5.50),
    Restaurant("Nonna", "Italian", "355-4433", "Stracotto", 25.50),
    Restaurant("Jitlada", "Thai", "324-4433", "Paht Woon Sen", 15.50),
    Restaurant("Nola", "New Orleans", "336-4433", "Jambalaya", 5.55),
    Restaurant("Noma", "Modern Danish", "337-4433", "Birch Sap", 35.50),
    Restaurant("Addis Ababa", "Ethiopian", "337-4453", "Yesiga Tibs", 10.50) ]
print('**************************')
def costliest2(n: RC) -> str:
    n = sorted(n, key=restaurant_price, reverse=True)
    return n[0].name
assert costliest2(RC) == 'Noma'
print(RC)
print()


#
#E.1
#
Book = namedtuple('Book', 'author title genre year price instock')

BSI = [
    Book('Alice', 'Curious George', 'Kids', 2001, 10.00, 50),
    Book('Tom', 'Fried Bung', 'Horror', 2014, 30.00, 100),
    Book('Larry', 'Ducks In A Row', 'Comedy', 2008, 25.00, 100),
    Book('Thomas', 'Attack On Birds', 'SciFi', 2005, 20.00, 75),
    Book('Aaron', 'Swing Low and Slap It!!', 'Adult Entertainment', 2002, 15.00, 20),
    Book('Bill', 'My Wife Is Hotter Than Yours', 'Maunal', 1950, 4.50, 1)]

for title in BSI:
    print(title[1])

#
#E.2
#
print('************************')

for i in range(len(BSI)):
    BSI[i] = Book(BSI[i].author,BSI[i].title,BSI[i].genre,BSI[i].year,BSI[i].price*2,BSI[i].instock)

print(BSI)
