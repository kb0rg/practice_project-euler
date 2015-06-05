"""
2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of 
the numbers from 1 to 20?
"""

"""
range to search: higher num through product of all num in range.
for each num (x) in search range, iterate through orig range to test 
	if divisible by each num in orig range
as soon as num % x !=0, iterate up search range
make recursive?  
"""

def find_max_search_num(numLo, numHi):
	product = 1
	for num in range(numLo, (numHi+1)):
		product = num * product
	print "max search num: ", product
	return product

def smallestMultiple(numLo, numHi):

	iter = 0
	maxNum = (find_max_search_num(numLo, numHi)+1)

	def recur_search(iter, maxNum):
		while iter < maxNum:
			print "iter: ", iter

			for num in range(numLo, (numHi+1)):
				iter = iter + numHi

				print "num is now: ", num
				print "is ", iter, "divisible by ", num, "?"
				if iter % num != 0:
					print "no -- moving on"
					iter += numHi
					recur_search(iter, maxNum)
				else:
					print "yes.....next!"

		print "smallest positive number is: ", iter
		return iter

	recur_search(iter, maxNum)

"""
test1
print smallestMultiple(1, 5)
# smallest positive number is:  145
"""

"""
test2
print smallestMultiple(1, 10)
#RuntimeError: maximum recursion depth exceeded
"""

#print smallestMultiple(1, 20)