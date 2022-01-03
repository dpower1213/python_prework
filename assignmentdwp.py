#question 1
#Write a function to print "hello_USERNAME!" USERNAME 
#is the input of the function. The first line of the 
#code has been defined as below.

def hello_name(user_name):
    print("Hello", user_name)

user_name=input("User name:")
hello_name(user_name)

#question 2
#Write a python function, first_odds that prints
#the odd numbers from 1-100 and returns nothing

def first_odds():
    odd_num=[]
    for n in range(1,100):
        if n%2==1:
            odd_num.append(n)
    print(odd_num)

print(first_odds())

#question 3
#Please write a Python function, max_num_in_list to return 
# the max number of a given list.
#The first line of the code has been defined as below.

def max_num_in_list(a_list):
    print(max(a_list))

a_list=[1,2,3,200,4,5,20,11,99]
max_num_in_list(a_list)

#Question 4
#Write a function to return if the given year
#is a leap year. A leap year is divisible by 4,
#but not divisible by 100, unless it is also divisible
#by 400. The return should be boolean Type (true/false).


def is_leap_year(a_year):
    
    a_year = int(a_year)
    if a_year % 4==0:
        if a_year % 100 == 0 and a_year % 400==0:
            print("true")
        
        elif a_year % 100 == 0 and a_year % 400 != 0:
            print("false")
        
        else: print("true")
    else: print("false")
a_year = input("what year to test?")    
is_leap_year(a_year)

#question 5
#Write a function to check to see if all numbers in list are
#consecutive numbers. For example, [2,3,4,5,6,7] are consecutive
#numbers, but [1,2,4,5] are not consecutive numbers. The return
#should be boolean Type.

def is_consecutive(a_list2):
    
    y = 0
    for y in [a_list2]:

        if y - y+1 != 1:
            print("false")
        else: y = y + 1

    print("true")
a_list2 = [1,2,3,4,5,6,10]
is_consecutive(a_list2)

