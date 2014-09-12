# Christopher Pullen
# 12-09-2014
# Development exercise 1

import math

print(" Hello friend, today we will be seeing how many times y will divide into x and what the remainder is.")
first_number = int(input("Please enter your first number:"))
second_number = int(input("Please enter your second number:"))

number_of_divisions = first_number//second_number
remainder = first_number%second_number

print("The number of divisions posible are {0} and the remaining number is {1}" .format (number_of_divisions, remainder))
                    
