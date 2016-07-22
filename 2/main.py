#!/usr/bin/env python

def main(maximum):
	two_previous = 1
	previous = 2
	sum = 2

	while True:
		value = two_previous + previous
		two_previous = previous
		previous = value
		if value >= maximum:
			return sum
		if value % 2 == 0:
			sum += value
		print value


if __name__ == "__main__":
	print "f(4000000)=%s"%main(4000000)	

