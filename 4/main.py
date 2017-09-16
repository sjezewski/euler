#!/usr/bin/env python

import math
import sys

def num_digits(num):
    power = 0
    while num/(10**power) != 0:
        power += 1
    return power

def get_digit(num, idx):
    return (num%10**idx - num%10**(idx-1))/10**(idx-1)

def is_a_palindrome(num):
    digits = num_digits(num)
    if digits == 1:
        return True
    if num == 0:
        return True

    offset = 0
    while offset <= digits/2-1:
        high = get_digit(num, digits-offset)
        low = get_digit(num, 1+offset)
        if high != low:
            return False
        offset += 1

    return True

def biggest_palindrome_from_factors_of_size(size):
    product = 123
    upper_bound = 10**(size)
    largest = 0
    for a in range(0, upper_bound - 1):
        for b in range(0, upper_bound - 1):
            product = (upper_bound-a) * (upper_bound -b)
            if is_a_palindrome(product):
                if product > largest:
                    largest = product
                # print "%s=%s*%s"%(product, upper_bound-a, upper_bound-b)
    return largest

if __name__ == "__main__":
	print "f(131)=%s"%is_a_palindrome(131)	
	print "f(123454321)=%s"%is_a_palindrome(123454321)	
	print "f(1221)=%s"%is_a_palindrome(1221)	
	print "f(%s)=%s"%(sys.argv[1], is_a_palindrome(int(sys.argv[1])))
        print "max palindrome w 1 digit:%s"%biggest_palindrome_from_factors_of_size(1)
        print "max palindrome w 2 digit:%s"%biggest_palindrome_from_factors_of_size(2)
        print "max palindrome w 3 digit:%s"%biggest_palindrome_from_factors_of_size(3)
