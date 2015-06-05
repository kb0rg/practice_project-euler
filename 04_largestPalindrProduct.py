"""
https://projecteuler.net/problem=4
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
"""
notes:
largest possible product of 2 3-digit numbers:
999 x 999 = 998001
smallest possible product of 2 3-digit numbers:
100 x 100 = 10000
largest palidrome will be within range(10000,998001)
iterate through this range backwards.

to test for palidrome: turn int into str and see if str.reversed() == str?
"""
def find_largest_palindrome_in_range(low, high):
    # print "low: ", low, "high: ", high

    for x in range(high, (low-1), -1):
        numstr = str(x)
        # print "numstr is: ", numstr
        if numstr == numstr[::-1]:
            return x

# #tests
# print find_largest_palindrome_in_range(1, 335)
# print find_largest_palindrome_in_range(9, 10)


# print find_largest_palindrome_in_range(10000,998001)
# returned 997799 -- incorrect

"""
test with example from instructions:
The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99.
notes:
largest possible product of 2 2-digit numbers:
99 x 99 = 9801
smallest possible product of 2 3-digit numbers:
10 x 10 = 100
largest palidrome will be within range(100,998001)
"""
print find_largest_palindrome_in_range(100, 9801)
# returned 9779 -- doesn't match instructions,
# what am I misunderstanding in instructions?!
"""
***!!!***
need to test whether num in range is actually a product 
of two n-digit numbers
maybe revisit not as range, but as iterating backwards
through n-digit numbers x and y, and testing product. arrrgh
"""
