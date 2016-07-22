#!/usr/bin/env python

import math
import sys

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
