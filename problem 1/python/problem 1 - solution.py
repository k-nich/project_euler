# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:23:43 2024

@author: k-nich
"""

def is_divisible_by_three_or_five(input_number):
    return input_number%3 == 0 or input_number%5 == 0

def total_up_divisible_numbers(input_number):
    total = 0
    for number in range(input_number):
        if is_divisible_by_three_or_five(number):
            total += number
    return total


print(total_up_divisible_numbers(1000))
#233168
