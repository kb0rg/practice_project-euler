"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

# don't run the code below. it crashes my machine.
"""
def largestPrimeFactor(n):

	primeFactorL = list()

	for x in range(n):
		if n % x == 0:
			primeFactorL.append(x)

	return primeFactorL[:1]

print largestPrimeFactor(600851475143)

"""

# forgot to test if prime
# look up sieve of Eratosthenes


def largestPrimeFactor(n):

# find factors first, or test whether is prime first?

	# make function to test if prime? 
	# reduce calcutation by running range backward
	# start at half? third? square root?

	# start range backwards from square root of n
	# convert to int. range does not accept float
	rangeStart = int(math.sqrt(n))

	# start range at square root of n, -1. convert to int.
	for x in range(rangeStart, 1, -1):
		# skip even numbers
		while x % 2 != 0:
			if n % x == 0:
				return x



print largestPrimeFactor(600851475143)


"""
or. create an isprime function first.
start a for loop, running the range backwards, beginning from n % 2 
??? not sure if logic is correct, but 2 is the first potentional prime it's divisible by, so half n is the largest possible factor???
check to see if loop iterator is prime -- if not, skip.
if iterator is prime, then check whether dividing n by x is an integer. then check to see if n%x is prime?
"""

