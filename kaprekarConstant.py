# !/usr/bin/env Python3


from math import log10, ceil, floor
import argparse

"""
Filename: kaprekarConstant.py
Author: Fanoril
Date: 2025-02-28
Version: 0.1
Description: Just a Script, that tries to calculate the
             Kaprekar Constant for a given Number.
Licence: GPL-3.0
Dependencies: log10, ceil, floor from math, argparser
"""

#
# TODO:
# 1) optimize sorting algorithm
# 2) implement special case for 2-, 5- and 7-digit-numbers;
#    there is no kapreka number
# 3) implement algorithm for new kaprekar-constants (or new zykels)
# --- question: how many "iterations of a zykel" are needed,
#               to prove the existence of a zykel?
# 4) optimize zykel algorithm
#
#
# Done:
# - fix sorting algorithm
# - optimize if-else-statement in sorting algorithm
# - implement special case for zykel
# - implement rough argparser
#


# Math fun

def sort_numbers_by_digits(number: int, desc: bool) -> int:
    """
    Returns a number sorted by digits. i
    (Note: Just programming exercise to avoid using str.sort() functions.
       That's just all work and no play...)
    Parameters:
    number (int): number, that should be sorted
    desc (boolean): If True the number will be descending sorted
                        otherwise ascending sorted
    Returns:
    sorted_number (int): sorted number
    """
    sorted_number: int = 0
    order_of_magnitude: int = 0
    number_of_digits: [int, ...] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Analyse Number
    # Get the oder_of_magnitude by logarithmic magic
    order_of_magnitude = ceil(log10(number))

    # Get digits by dividing and rounding up and
    # more important get the number/amount of EACH digit in the number
    n: int = number  # Just to be safe
    for current_power_of_ten in range(order_of_magnitude, 0, -1):
        # get the digit at the specifig point
        digit = floor(n / (10 ** (current_power_of_ten - 1)))
        # increment the amount of the specifig digit
        number_of_digits[digit] += 1
        # assign new number to analyse
        n = n - digit * 10 ** (current_power_of_ten - 1)

    #
    # Rearange number by digits
    # VERY nasty sorting algorithm
    #

    # initialise variables with uncommon value - debug
    current_magnitude = -1
    rate_of_change_magnitude = 0
    if desc:
        # if descending order: we start with max magnitude and decrease
        current_magnitude = order_of_magnitude - 1
        rate_of_change_magnitude = -1
    else:
        # if ascending order: we start with magnitude 0 and increase
        current_magnitude = 0
        rate_of_change_magnitude = +1

    #
    # iterate through all "number of digits"
    # if none left: decrease current_digit
    # else: rearange sorted number by power of 10s
    #       change current_magnitude and number_of_digits for specifig digit
    # Note: rate_of_change_magnitude and current_magnitude are initialised
    #       above. For descending order the digit 9 should be in the "highest
    #       magnitude", so we start at max magnitude and decrease. For
    #       ascending order the digit 9 should be in the "smallest magnitude",
    #       so we start a 0 and increase.
    #

    current_digit = 9
    while current_digit >= 0:
        if number_of_digits[current_digit] == 0:
            current_digit -= 1
        else:
            sorted_number += current_digit * 10 ** current_magnitude
            current_magnitude += rate_of_change_magnitude
            number_of_digits[current_digit] -= 1

    # return sorted number
    return sorted_number


def get_kaprekar_constant(number: int, *args):
    """
    Returns a tupel of
    -the kaprekar constant of one given number and
    -the number of iterations to this number.

    Parameters:
        number (int): Number

    Returns:
        kaprekar_tupel (int,int,bool): Tupel of the Kaprekar constant
                                and the Iterations, to got there; bool return
                                if there are any zykel
    """
    # Output 1
    print("Kaprekar Number?")
    print("----------------")
    print("Startnumber: " + str(number))
    print("----------------")

    kaprekar_constant_list = (0,
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
                              63333317666664)
    current_number = number
    kaprekar_tupel = (0, 0)
    kaprekar_number = -1
    iterations = 1

    #
    # For "Zykel" like 75933 → 63954 → 61974 → 82962 → 75933 (start: 33364):
    # Awkward Algorithm
    # just remember all potential kaprekar constants, if there is a duplicate
    # we have a zykel - not elegant nor effective just plain pragmatism
    #

    last_potential_kaprekar = [0]

    while (kaprekar_number not in kaprekar_constant_list):
        # Get first ordered number (asc.)
        number_one = sort_numbers_by_digits(current_number, False)

        # Get second ordered number (desc.)
        number_two = sort_numbers_by_digits(current_number, True)
        # Get difference of first and second number =
        # potential Kaprekar Number
        kaprekar_number = number_two - number_one

        # Output 2
        print("Iteration: " + str(iterations))
        print("First Number: " + str(number_one))
        print("Second Number: " + str(number_two))
        print("Difference of 2 and 1: " + str(kaprekar_number))
        print("-------------------")

        # new Number = potential Kaprekar Number; Iteration + 1
        current_number = kaprekar_number
        iterations += 1

        # for zykels
        if current_number in last_potential_kaprekar:
            index_of_zykel = last_potential_kaprekar.index(current_number)
            last_potential_kaprekar.append(current_number)
            kaprekar_tupel = (
                last_potential_kaprekar[index_of_zykel:], iterations, True)
            return kaprekar_tupel
        last_potential_kaprekar.append(current_number)

    # form and return kaprekar_tupel
    kaprekar_tupel = (kaprekar_number, iterations - 1, False)
    return kaprekar_tupel


def main():
    #
    # Parser things:
    # -h, --help; help
    # -g, --get-constant; get a kaprekar constant by a given number
    # -f, --find-constant; find new kaprekar constant by given digitnumber
    #
    parser = argparse.ArgumentParser(
        prog='Kaprekar Constant Fun',
        description='Simple Script to get and find kaprekar constants. ',
        epilog='Everywhere is this number ... 6174')

    parser.add_argument(
        '-g',
        '--get',
        action="store_true",
        help='Get-Mode: Get a kaprekar constant by a given number.')

    parser.add_argument(
        '-f',
        '--find',
        action="store_true",
        help='Find-Mode: Find a kaprekar constant by given number of digits')

    parser.add_argument(
        "NUMBER",
        type=int,
        help="""In Get-Mode you get the kaprekar constant for the given NUMBER.
        In Find-Mode the program tries to find a kaprekar constant for the
        given NUMBER of digits.""")

    args = parser.parse_args()

    # Get kaprekar mode

    if args.find:
        print("Find-Mode")
        pass
    elif args.get:
        print("Get-Mode")
        kaprekar_tupel = get_kaprekar_constant(int(args.NUMBER))
        if kaprekar_tupel == (0, 0, ...):
            print("Error!")
        else:
            if kaprekar_tupel[2]:  # if there is a zykel
                print("There is a zykel with " + str(kaprekar_tupel[0]) +
                      " after " + str(kaprekar_tupel[1]) + " iterations.")
            else:
                print("The kaprekar constant is: " + str(kaprekar_tupel[0]) +
                      " with " + str(kaprekar_tupel[1]) + " iterations.")
    else:
        print("ERROR - pray and hope for the best!")


if __name__ == "__main__":
    main()
