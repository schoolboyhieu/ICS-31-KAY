#Hieu Dao-Tran 24353293 and Jerry He 49794121
__author__ = 'dgk'

# RESTAURANT COLLECTION PROGRAM
# ICS 31, UCI, David G. Kay, Fall 2012

# Implement Restaurant as a namedtuple, collection as a list

##### MAIN PROGRAM (CONTROLLER)

def restaurants():  # nothing -> interaction
    """ Main program
    """
    print("Welcome to the restaurants program!")
    our_rests = Collection_new()
    our_rests = handle_commands(our_rests)
    print("\nThank you.  Good-bye.")

MENU = """
Restaurant Collection Program --- Choose one
 a:  Add a new restaurant to the collection
 c:  Change prices for the dishes served
 r:  Remove a restaurant from the collection
 s:  Search the collection for selected restaurants
 f:  Search by cuisine
 g:  Search by phrase
 p:  Print all the restaurants
 q:  Quit
"""

def handle_commands(C: list) -> list:
    """ Display menu, accept and process commands.
    """
    while True:
        response = input(MENU)
        if response=="q":
            return C
        elif response=='a':
            r = Restaurant_get_info()
            C = Collection_add(C, r)
        elif response=='r':
            n = input("Please enter the name of the restaurant to remove:  ")
            C = Collection_remove_by_name(C, n)
        elif response=='p':
            print(Collection_str(C))
        elif response=='s':
            n = input("Please enter the name of the restaurant to search for:  ")
            for r in Collection_search_by_name(C, n):
                print(Restaurant_str(r))
        elif response =='c':
            n = input("Please enter the percentage you want to increase the dishes by:  ")
            C = Collection_change_price(C, float(n))
        elif response == 'f':
            n = input("Please enter the cuisine you want to search by:")
            print(Collection_cuisine(C, n))
        elif response == 'g':
            n = input("Please insert phrase:")
            print(Collection_namekey(C, n ))

        else:
            invalid_command(response)

def invalid_command(response):  # string -> interaction
    """ Print message for invalid menu command.
    """
    print("Sorry; '" + response + "' isn't a valid command.  Please try again.")




##### Restaurant
from collections import namedtuple
Restaurant = namedtuple('Restaurant', 'name cuisine phone menu')
# Constructor:   r1 = Restaurant('Taillevent', 'French', '01-11-22-33-44', 'Escargots', 23.50)

def Restaurant_str(self: Restaurant) -> str:
    return ("Name:" + self.name + "\n" +
            "Cuisine:  " + self.cuisine + "\n" +
            "Phone:    " + self.phone + "\n" +
            "Menu:     " + display_menu(self.menu) + "\n"
            "Average price: " + str(Menu_price(self.menu)) + "\n"
            "Average calories:" + str(Menu_calories(self.menu))+ "\n")

def Restaurant_get_info() -> Restaurant:
    """ Prompt user for fields of Restaurant; create and return.
    """
    return Restaurant(
        input("Please enter the restaurant's name:  "),
        input("Please enter the kind of food served:  "),
        input("Please enter the phone number:  "),
        Menu_enter())

def Restaurant_cuisine(R: Restaurant)-> float:
    return Menu_price(R.menu)

def Cuisine_name(R: Restaurant) -> str:
    return R.cuisine


#### COLLECTION
# A collection is a list of restaurants

def Collection_new() -> list:
    ''' Return a new, empty collection
    '''
    return [ ]

def Collection_str(C: list) -> str:
    ''' Return a string representing the collection
    '''
    s = ""
    for r in C:
        s = s + Restaurant_str(r)
    return s

def Collection_search_by_name(C: list, name: str) -> list:
    """ Return list of Restaurants in input list whose name matches input string.
    """
    result = [ ]
    for r in C:
        if r.name == name:
            result.append(r)
    return result
    # alternative (using a list comprehension):
    # return [r for r in C if r.name == name]

def Collection_add(C: list, R: Restaurant) -> list:
    """ Return list of Restaurants with input Restaurant added at end.
    """
    C.append(R)
    return C

def Collection_remove_by_name(C: list, name: str) -> list:
    """ Given name, remove all Restaurants with that name from collection.
    """
    result = [ ]
    for r in C:
        if r.name != name:
            result.append(r)
    return result
    #    Alternative:
    #    return [r for r in self.rests if r.name != name]
def Collection_cuisine(c: list, s: str)-> list:
    nl = []
    total_rests = 0
    for x in c:
        if s == Cuisine_name(x):
            nl.append(x.name)
            total_rests += Restaurant_cuisine(x)
    nl.append(total_rests/len(c))
    return nl

def Collection_namekey(c: list, s: str) -> list:
    nl = []
    for x in c:
        a = Menu_name(x.menu)
        for p in a:
            if s in p:
                nl.append(x.name)
    return nl

### Dishes
Dish = namedtuple('Dish', 'name price calorie')

def Dish_str(d: Dish) -> str:
    return d.name + " "+'($'+str(d.price)+'):'" "+ str(d.calorie)+ ' cal'

def Dish_get_info() -> Dish:
    """ Prompt user for fields of Dish; create and return.
    """
    return Dish(
        input("Please enter the dish's name:  "),
        float(input("Please enter the price of that dish:  ")),
        int(input("Please enter the calories of dish  ")))
def Dish_get_price(d: Dish) -> float:
    return d.price

def Calorie_get(d: Dish) -> float:
    return d.calorie

def Dish_name(d: Dish) -> str:
    return d.name
    
### Menu
def Menu_enter() -> list:
    menu = []
    n = input('Do you want to add dish?')
    while n == 'yes':
        d = Dish_get_info()
        menu.append(d)
        n = input('Do you want to add another dish?')
    return menu

def display_menu(l: list) -> str:
    m =''
    for d in l:
        m = m + Dish_str(d) + '\n'
    return m
def Dish_change_price(d: Dish, n:float) -> Dish:
    nd = d._replace(price = d.price * (.01 * n) + d.price)
    return nd

def Menu_change_price(l: list, n:float) -> list:
    nm = []
    for d in l:
        D = Dish_change_price(d, n)
        nm.append(D)
    return nm


def Menu_price(l: list) -> float:
    price = []
    for x in l:
        price.append(Dish_get_price(x))
    return sum(price)/len(price)

def Menu_calories(l: list) -> float:
    calorie = []
    for c in l:
        calorie.append(Calorie_get(c))
    return sum(calorie)/len(calorie)

def Menu_name(l:list) -> list:
    result = []
    for x in l:
        result.append(Dish_name(x))
    return result
        

def Restaurant_change_price(r: Restaurant, n:float) -> Restaurant:
    new_price = r._replace(menu = Menu_change_price(r.menu, n))
    return new_price

def Collection_change_price(c: list, n:float) -> list:
    nc = []
    for r in c:
        r = Restaurant_change_price(r, n)
        nc.append(r)
    return nc


        
    



restaurants()
