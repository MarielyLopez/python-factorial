#coding:utf-8
import os
import sys

def insert_number():
    print "Welcome to factorial!"
    print " "
    valid = True
    while valid == True:
        number = raw_input("Insert a number: ")
        verific = verific_number(number)
        if verific == True:
            fact = factorial(number)
            print "The factorial of %s is %s" % (number,fact)
            question_y_n()
            valid = False
        else:
            print "Try again."

def verific_number(number):
    answer_u = True
    while answer_u == True:
        try:
            if True == number.isdigit():
                return True
            else:
                return False
        except ValueError:
            print "Try again"

def factorial(number):
    num = 1
    number = int(number)
    while number >= 1:
        num = num * number
        number = number - 1
    return num

def question_y_n():
    yesornot = True
    while yesornot == True:
        user_answer = raw_input("Do you want enter other number ? y / n: ")
        if user_answer == "y" or user_answer == "yes":
            insert_number()
        elif user_answer == "n" or user_answer == "not":
            print " Good bye."
            sys.exit(1)
        else:
            print "Insert yes or not."

if __name__ == '__main__':
    insert_number()
