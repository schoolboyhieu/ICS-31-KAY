# Jonathan Gieg 77804954 and Hieu Dao-Tran 24353293 ICS 31 Lab Assignment 2
git add doc / lab_2_folder

print('How many hours?')
hours = float(input())
print('This many hours:', hours)
print('How many dollars per hour?')
rate = float(input())
print('This many dollars per hour:  ', rate)
print('Weekly salary:  ', hours * rate)

hours = int(input('How many hours?'))
print('This many hours:', hours)
rate = float(input('How many dollars per hour?'))
print('This many dollars per hour: $ ', rate)
print('Weekly salary: $ ', hours * rate)



print('Hello.  What is your name?')
name = input()
print("Hello,", name)
print("It's nice to meet you.")
print('How old are you?')
age = int(input())
print('Next year you will be', age + 1, 'years old.')
print('Good-bye!')

krone_per_euro = 7.46 
krone_per_pound = 10.33 
krone_per_dollar = 6.66 

print('What is your business name?')
business_name = input()
print('How many Euros do you have?')
number_of_euros = float(input())
print('How many pounds do you have?')
number_of_pounds = float(input())
print('How many dollars do you have?')
number_of_dollars = float(input())

print('Business name:', business_name)
print('Number of euros:', number_of_euros)
print('Number of pounds:', number_of_pounds)
print('Number of dollars:', number_of_dollars)

print('Copenhagen Chamber of Commerce')
print('Business name: Tycho Brahe Enterprises')
print(number_of_euros, 'euros is',number_of_euros * krone_per_euro,'krone')
print(number_of_pounds, 'pounds is', number_of_pounds * krone_per_pound,'krone')
print(number_of_dollars, 'dollars is', number_of_dollars * krone_per_dollar,'krone')
e = number_of_euros * krone_per_euro
p = number_of_pounds * krone_per_pound
d = number_of_dollars * krone_per_dollar
print('Total krone:', float(e + p + d))


from collections import namedtuple
Book = namedtuple('Book', 'title author year price')
favorite = Book('Adventures of Sherlock Holmes',
                'Arthur Conan Doyle', 1892, 21.50)
another = Book('Memoirs of Sherlock Holmes', 
               'Arthur Conan Doyle', 1894, 23.50)
still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 25.00)
print(still_another[0])
print(another[3])
print(float((favorite[3] + another[3] + still_another[3])/3))
print(favorite[2] < 1900)

still_another = Book('Return of Sherlock Holmes',
                     'Arthur Conan Doyle', 1905, 26.00)

print(still_another[3] * 1.20)

from collections import namedtuple
Animal = namedtuple('Animal', 'name species age_in_years weight_in_kg food')
animal1 = Animal('Jumbo', 'Elephant', 50 , 1000, 'peanuts')
animal2 = Animal('Perry', 'Platypus', 7 , 1.7 , 'shrimp')
print(animal1[3] < animal2[3])


booklist = [favorite, another, still_another]
print(booklist[0][3] < booklist[1][3])
print(booklist[0][2] > booklist[-1][2])

            






