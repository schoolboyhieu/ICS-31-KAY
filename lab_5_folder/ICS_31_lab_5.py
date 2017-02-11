# Hieu Dao-Tran 24353293 and Jerry He 49794121
# Lab assignment 5 Section 5


########### do doc strings********


#
#Part C.1
#
from collections import namedtuple

Dish = namedtuple('Dish', 'name price calorie')
d1 = Dish('Cheeseburger', 5.50, 400)
d2 = Dish('Hotdog', 3.50, 300)
d3 = Dish('Pizza', 1.50, 170)
d4 = Dish('Sushi', 9.00, 250)
d5 = Dish('Cat', 7.50, 420)
d6 = Dish('Dog', 12.50, 690)
d7 = Dish('Candy', 1.00, 100)
d8 = Dish('Dinosaur', 50.00, 1000)
d9 = Dish('Granola', .50, 50)
d10 = Dish('Ketchup', .10, 10)
DL = [d1, d2, d3, d4, d5, d6]
DL2 = [d7, d8, d9, d10]
print()

#
#Part C.2
#
def Dish_str(d: Dish) -> str:
    '''Returns a str with the provided order'''
    return d.name + " "+'($'+str(d.price)+'):'" "+ str(d.calorie)+ ' cal'
assert Dish_str(d1) == 'Cheeseburger ($5.5): 400 cal'

print(Dish_str(d1))
print()

#
#Part C.3
#

def Dish_same(d1: Dish, d2: Dish) -> bool:
    '''Returns True if names and  calories match in argument'''
    if d1.name == d2.name:
        if d1.calorie == d2.calorie:
            return True
    else:
        return False
assert Dish_same(d1, d3) == False

print(Dish_same(d1, d3))
print()

#
#Part C.4
#
def Dish_change_price(d: Dish, n:float) -> Dish:
    '''Returns a price increased/decreased by provided argument'''
    return d.price * (.01 * n) + d.price
assert Dish_change_price(d1, 100) == 11.0
print(Dish_change_price(d1, -25))
print()

#
#Part C.5
#
def Dish_is_cheap(d: Dish, n: float) -> bool:
    '''Returns True if number in argument is less than price of dish'''
    if d.price < n:
        return True
    else:
        return False
assert Dish_is_cheap(d1, 12) == True
print(Dish_is_cheap(d3, 1))
print()

#
#Part C.6
#
big_DL = []
big_DL.extend(DL + DL2)
print(big_DL)
print()
def Dishlist_display(l: list ) -> str:
    '''Returns a big str with all the str representation of each dish in a new line'''
    
    dishes = ""
    for n in l:
        dishes += Dish_str(n)+ '\n'
    return dishes
print(Dishlist_display(big_DL))
print()

#
#Part C.7
#
def Dishlist_all_cheap(l: list, n: float) -> bool:
    '''Returns True if the price of every dish on the list is less than the number provided'''
    for x in l:
        if not Dish_is_cheap(x, n):
            return False
    return True
print(Dishlist_all_cheap(big_DL, 100))
print()

#
#Part C.8
#

def Dishlist_change_price(l: list, n: float) -> list:
    '''Returns a list of dishes with the changed price provided by the number'''
    nl = []
    for x in l:
        new_dish = Dish( x.name, Dish_change_price(x,n), x.calorie) 
        nl.append(new_dish)
    return nl
print(Dishlist_change_price(big_DL, -25))
print()

#
#part C.9
#

def Dishlist_prices(l:list) -> float:
    '''Returns a list full of dish prices'''
    np = []
    for x in l:
        np.append(x.price)
    return np
print(Dishlist_prices(big_DL))
print()

#
#Part C.10
#

def Dishlist_average(l:list) -> float:
    '''Returns the average of the prices of the dishes in a list'''
    total = 0
    total = total + sum(Dishlist_prices(l)) 
    return total / len(l)
print(Dishlist_average(big_DL))
print()

#
#Part C.11
#

def Dishlist_keep_cheap(l:list, n:float) -> list:
    '''Returns a list of dishes cheaper than the provided number'''
    lst = []
    for x in l:
        if x.price < n:
            lst.append(x)
    return lst
print(Dishlist_keep_cheap(big_DL, 10))

#
#Part C.12
#


d11 = Dish('Hot sauce', .15, 25)
d12 = Dish('Apple', .05, 5)
d13 = Dish('Wonton', 3.50, 40)
d14 = Dish('Taco', 4.50, 180)
d15 = Dish('Burrito', 8.90, 250)
d16 = Dish('Elephant', 99.00, 1500)
d17 = Dish('Squirtle', 199.00, 420)
d18 = Dish('Charmander', 199.00, 1200)
d19 = Dish('Bulbasaur', 199.00, 360)
d20 = Dish('AK47', 250, 1230)
d21 = Dish('Give us an A', 100, 100)
d22 = Dish('Passing grade', 100, 100)
d23 = Dish('CSE', 200, 200)
d24 = Dish('Mario Kart', 150, 150)
d25 = Dish('Smash Bros.', 300, 300)


biger_DL = [d11, d12, d13, d14, d15, d16, d17, d18, d19, d20, d21, d22, d23, d24, d25]
big_DL.extend(biger_DL)
print(big_DL)

def before_and_after() -> None:
    '''Changes price of dishes in the list by the inputted number'''
    p = input("Price increase by:")
    print(Dishlist_display(big_DL))
    new_big_DL = Dishlist_change_price(big_DL, float(p))
    print(Dishlist_display(new_big_DL))

before_and_after()
print()

#
#Part E.1
#

Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
r1 = Restaurant('Thai Dishes', 'Thai', '334-4433', [Dish('Mee Krob', 12.50, 500),
                                                    Dish('Larb Gai', 11.00, 450)])
r2 = Restaurant('Taillevent', 'French', '01-44-95-15-01', 
				[Dish('Homard Bleu', 45.00, 750),
				 Dish('Tournedos Rossini', 65.00, 950),
				 Dish("Selle d'Agneau", 60.00, 850)])

r3 = Restaurant('Pascal', 'French', '940-752-0107',
                [Dish('Escarsgots', 12.95, 250),
                 Dish('Poached Salmon', 18.50, 550),
                 Dish('Rack of Lamb', 24.00, 850),
                 Dish('Marjolaine Cake', 8.50, 950)])

print()

#
#Part E.2
#
def Restaurant_first_dish_name(R: Restaurant) -> str:
    '''Returns the name of the first dish in each menu of the restaurant'''
    return R.menu[0].name
assert Restaurant_first_dish_name(r1) == 'Mee Krob'
assert Restaurant_first_dish_name(r2) == 'Homard Bleu'
print(Restaurant_first_dish_name(r3))
print()

#
#Part E.3
#
def Restaurant_is_cheap(r: Restaurant, n:float) -> bool:
    '''Returns True if the average price of the menu is less than the number given'''
    return Dishlist_average(r.menu) < n
assert Restaurant_is_cheap(r1, 10) == False
assert Restaurant_is_cheap(r2, 11) == False
print(Restaurant_is_cheap(r1, 100))
print()

#
#Part E.4\
#

Collection = [r1, r2, r3]
def Menu_raise_prices(d: Dish) -> Dish:
    return d.price + 2.50
assert Menu_raise_prices(d1) == 8.00

def Restaurant_raise_price(r: Restaurant) -> Restaurant:
    nr = []
    for m in r.menu:
        nr.append(Menu_raise_prices(m))
    return nr
print(Restaurant_raise_price(r1))

def Collection_raise_price(c: Collection) -> Collection:
    nc = []
    for r in c:
        r = Restaurant_raise_price(r)
        nc. append(r)
    return nc
print(Collection_raise_price(Collection))
print(Collection)
def Collection_change_price(c: Collection, n: float) -> Collection:
    np = []
    for r in c:
        r = Restaurant_raise_price(r)
        r * n + r

print()

#
#Part E.5
#


