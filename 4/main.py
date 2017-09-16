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
    print "is_a_palindrome: %s"%num
    digits = num_digits(num)
    print "has %s digits"%digits
    if digits == 1:
        return True
    high = get_digit(num, digits)
    low = get_digit(num, 1)
    print "high=%s, low=%s"%(high,low)
    if high == low:
        if digits == 2:
            return True
        return is_a_palindrome((num - high*10**(digits-1) - low)/10)
    return False

if __name__ == "__main__":
	print "f(131)=%s"%is_a_palindrome(131)	
	print "f(123454321)=%s"%is_a_palindrome(123454321)	
	print "f(1221)=%s"%is_a_palindrome(1221)	
	print "f(%s)=%s"%(sys.argv[1], is_a_palindrome(int(sys.argv[1])))
