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
    if digits == 1
        return true
    high = get_digit(num, digits)
    low = get_digit(num, 1)
    if high == low
        return is_a_palindrome((num - high*10**digits - low)/10)
    return false

def main(num):
	maximum = math.sqrt(num)

	factors = []
	f = 2

	while num != 1:
		while num % f == 0:
			factors += [f]
			num /= f
		f += 1
	return max(factors)

if __name__ == "__main__":
	print "f(13195)=%s"%main(13195)	
	print "f(600851475143)=%s"%main(600851475143)	
	print "f(%s)=%s"%(sys.argv[1], main(int(sys.argv[1])))
