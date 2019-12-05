#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: December 2019
# This program goes to a certain decimal place


def greatestNumber(choice):
    # This function calculates the biggest number
    # empty list
    numbers = []
    # empty variable
    biggest = None
    # process
    for insert in range(choice):
        number_as_string = input("Enter your number: ")
        number_as_int = int(number_as_string)
        biggest = number_as_int
        numbers.append(number_as_int)
    for digit in numbers:
        if digit >= biggest:
            biggest = digit
    # returns number to main function
    return biggest


def main():
    # This function takes the user choice of input
    # this helps ask again
    while True:
        # input
        choice_as_string = input("How many numbers do you wish to enter: ")
        print()
        try:
            # converts string to int
            choice_as_int = int(choice_as_string)
            # enters greatestNumber function
            greatest = greatestNumber(choice_as_int)
            print()
            # output
            print("The biggest number is", greatest)
        # prevents crashes and asks again
        except ValueError:
            print("Invalid Input")
            print()
            continue
        # break out of loop
        else:
            break


if __name__ == "__main__":
    main()
