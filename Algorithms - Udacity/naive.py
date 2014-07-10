# Udacity's Algorithms course
# Case Study - Different Algorithms for same task (naive and russian peasant algorithm for multiplying two numbers)

import time

def naive(a, b):
	x, y, z = a, b, 0
	while x > 0:
		z = z + y				# keeps on modifying z x-times
		x = x - 1
	return z

def russian(a, b):
    x = a
    y = b
    z = 0
    while x > 0:
        if x % 2 == 1:
            z = z + y
        y = y << 1
        x = x >> 1
    return z




