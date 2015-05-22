"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

# look up sieve of Eratosthenes?
"""
import math

# create utility function to use later
def is_prime(n):
	if n == 2 or n == 3:
		return True
	elif n <= 1:
		return False
	elif type(n) != int:
		return False
	else:
		# reduce calcutation by running range only to square root of n
		# convert to int. range does not accept float
		for i in range(2, int(math.sqrt(n))):
			if n % i == 0:
				return False
	return True

def largestPrimeFactor(n):
	
	prime_factor_list = []
	# start range at square root of n, -1. convert to int.
	# test for 2 (lowest prime, only even case)
	if n % 2 == 0:
		prime_factor_list.append(2)
	for x in range(3, int(math.sqrt(n))):
		# skip even numbers
		if x % 2 != 0:
			if n % x == 0 and is_prime(x):
				prime_factor_list.append(x)
	return sorted(prime_factor_list)[-1]

print largestPrimeFactor(600851475143)