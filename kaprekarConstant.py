#!/usr/bin/env Python3
"""
Filename: kaprekarConstant.py
Author: Fanoril
Date: 2025-02-28
Version: 0.1 
Description: Just a Script, that tries to calculate the Kaprekar Constant for a given Number.   
Licence: GPL-3.0
Dependencies: log10, ceil, floor from math 
"""  

# TODO: 
# 1) fix sorting algorithm
# 2) implement Kaprekars Zykel like: 71973 → 83952 → 74943 → 62964 → 71973 (with starting number 33363)
# 3) implement special case for 2-, 5- and 7-digit-numbers; there is no kapreka number  
# 4) implement algorithm for new kaprekar-constants (or new zykels) 
# --- question: how many "iterations of a zykel" are needed, to prove the existence of a zykel?  


""" 
Returns a tupel of
-the kaprekar constant of one given number and 
-the number of iterations to this number.

Parameters:
    number (int): Number

Returns: 
    kaprekar_tupel (int,int): Tupel of the Kaprekar constant 
                                and the Iterations, to got there
"""
def kaprekar_algorithm(number : int, *args)-> (int,int):
    #Output 1
    print("Kaprekar Number?")
    print("----------------") 
    print("Startnumber: " + str(number))
    print("----------------")

    kaprekar_constant_list = (
            0, 
            495, 
            6174, 
            549945, 
            631764, 
            63317664,
            97508421,
            554999445,
            864197532, 
            6333176664, 
            9753086421, 
            9975084201, 
            86431976532, 
            555499994445, 
            633331766664, 
            975330866421, 
            997530864201, 
            999750842001, 
            8643319766532, 
            63333317666664,
            )
    kaprekar_tupel = (0,0)
    kaprekar_number = -1 
    n = list(str(number))
    iterations = 1
    while (kaprekar_number not in kaprekar_constant_list): 
        # Get first ordered number (asc.) 
        n.sort()
        number_one = int(''.join(n))
        
        # Get second ordered number (desc.)
        n.sort(reverse = True)
        number_two = int(''.join(n))
        # Get difference of first and second number = potential Kaprekar Number
        kaprekar_number = number_two - number_one
        
        # Output 2
        print("Iteration: " + str(iterations))
        print("First Number: " + str(number_one))
        print("Second Number: " + str(number_two))
        print("Difference of 2 and 1: " + str(kaprekar_number))
        print("-------------------")

        # new Number = potential Kaprekar Number; Iteration + 1
        n = list(str(kaprekar_number))
        iterations += 1
    kaprekar_tupel = (kaprekar_number,iterations)
    return kaprekar_tupel


def main():
    number : str = input("Which number do you want to try?   ")
    kaprekar_tupel = kaprekar_algorithm(int(number))   
    if(kaprekar_tupel == (0,0)): 
        print("Numbers must be of the same Length!")
    else: 
        print("The kaprekar constant is: " + str(kaprekar_tupel[0]) + " with " + str(kaprekar_tupel[1]) + " Iterations.")

if __name__ == "__main__":
    main()


#TODO: Find a nice little Sorting algorithm. Split a given number in digits; reorder digits ascending oder descending. 
#For now this garbage is all i have. 

# Math fun
from math import log10, ceil, floor

"""
Returns a number sorted by digits. (Note: Just programming exercise to avoid using str.sort() functions. That's just all work and no play...) 
Parameters: 
    number (int): number, that should be sorted 
    desc (boolean): If True the number will be descending sorted
                    otherwise ascending sorted 
Returns: 
    sorted_number (int): sorted number
"""
def sort_numbers_by_digits(number: int, desc : bool) -> int: 
    #some variables
    sorted_number : int = 0 
    order_of_magnitude : int = 0
    number_of_digits : [int, ...] = [0,0,0,0,0,0,0,0,0,0]
    #digits : [int, ...] =  [] # just for debugging

    # Analyse Number 
    # Get the oder_of_magnitude by logarithmic magic
    order_of_magnitude = ceil(log10(number)) 
    
    # Get digits by dividing and rounding up and more important get the number/amount of EACH digit in the number 
    n : int = number # Just to be safe
    for current_power_of_ten in range(order_of_magnitude,0,-1):     
        digit = floor(n / (10**(current_power_of_ten-1))) # get the digit at the specifig point 
        number_of_digits[digit] += 1 # increment the amount of the specifig digit  
        n = n - digit*10**(current_power_of_ten-1) # new number to analyse



        #DEBUGGING - should be deleted anyways 
        #digits.append(digit) #just for debugging
        #print(current_power_of_ten) # debug
        #print(number_of_digits) # debug

    #Rearange number - sorted
    #VERY nasty sorting algorithm
    # 
    # shouldn't it be possible to merge the if- and else-Statement in a elegant way? It's nearly the same steps  
    #
    current_magnitude = order_of_magnitude
    if(desc): 
        current_digit = 9 # starting by digit 9 
        rate_of_change_digit = -1 # descending order
        while current_digit > 0: # For every 9,8,7, ... in the given number 
            if number_of_digits[current_digit] == 0: # if "none numbers" left
                current_digit += rate_of_change_digit # decrease the current_digit 
            else:
                sorted_number += current_digit*10**current_magnitude # reconstruct number 
                number_of_digits[current_digit] -= 1 # decrease amount of this specific digit
                current_magnitude -= 1 # decrease current magnitude
            print("AN:" + str(number_of_digits[current_digit])) #debug
            print("AZ:" + str(current_digit)) #debug

    else: # comments above
        current_digit = 0 
        rate_of_change_digit = +1 # ascending order
        while current_digit < 9: 
            if number_of_digits[current_digit] == 0: 
                current_digit += rate_of_change_digit
            else:
                sorted_number += current_digit*10**current_magnitude
                number_of_digits[current_digit] -= 1
                current_magnitude -= 1
            print("AN:" + str(number_of_digits[current_digit])) #debug
            print("AZ:" + str(current_digit)) #debug
    return sorted_number
