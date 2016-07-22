#!/usr/bin/env python

import sys

def main(maximum):
	i = 1
	sum = 0
	while i < maximum:	
		if i % 5 == 0:
			sum += i
		elif i % 3 == 0:
			sum += i
		i += 1
	return sum

if __name__ == "__main__":
	#main(int(sys.argv[1]))
	print "f(10)=%s, should be 23"%main(10)
	print "f(30)=%s, should be 195"%main(30)
	print "f(1000)=%s, should be 23"%main(1000)
	print "f(10000)=%s, should be 23"%main(10000)

