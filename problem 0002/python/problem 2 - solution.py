# -*- coding: utf-8 -*-
"""
Created on Sun May 26 19:02:15 2024

@author: k-nich
"""

from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r args:[%r, %r] took: %2.4f sec' % \
          (f.__name__, args, kw, te-ts))
        return result
    return wrap


@timing
def create_fibonacci_array(input_max_number):
    array = [1,2]
    small_component = 0
    large_component = 1
    next_value = array[small_component]+array[large_component]
    
    while next_value <= input_max_number:
        array.append(next_value)
        
        small_component += 1
        large_component += 1
                
        next_value = array[small_component]+array[large_component]
    return array


@timing
def recreate_array_without_odd_numbers(input_array):
    
    new_list = []
    for item in input_array:
        if item % 2 == 0:
            new_list.append(item)
    return new_list
    


print(sum(recreate_array_without_odd_numbers(create_fibonacci_array(4000000))))

#4613732         
        
    
