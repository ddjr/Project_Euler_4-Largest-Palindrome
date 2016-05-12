import math
import time
from sys import argv

def code_intro():
    print ""
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ---------------------------- Welcome to ----------------------------------'
    time.sleep(.1)
    print '  -------------------  Project Euler Problem 4  ----------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  ------------------ Created by: David Daly 2016 VA ------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  -- This project was done as part the https://projecteuler.net/ coding ----'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print "A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99. Find the largest palindrome made from the product of two 3-digit numbers."
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  -------- You can find me on Github at github.com/ddjr --------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    time.sleep(.1)
    print '  --------------------------------------------------------------------------'
    print ""
    time.sleep(.8)

def main():
    code_intro()
    palindrome_base = 997
    while check_palindrome(palindrome_base):
        palindrome_base -= 1

def check_palindrome(palindrome_base):
    palindrome, square_root = create_palindrome_and_sqr(palindrome_base)
    if is_palindrome_sum_of_two_numbers(palindrome, square_root):
        return False
    else:
        return True
def make_palindrome(palindrome_base):
    return int(str(palindrome_base) + reverse(palindrome_base))
def reverse(number):
    return str(number)[::-1]
 # [base 997 -> 997799 sqr = 998] [base 996 -> 996699 sqr = 998]
def create_palindrome_and_sqr(palindrome_base):
    palindrome = make_palindrome(palindrome_base)
    square_root = int(math.sqrt(palindrome))
    return palindrome, square_root
# Checks for whole number factors of a palindrome starting from 999 and going down by one until the palindrome's square root
def is_palindrome_sum_of_two_numbers(palindrome, square_root):
    factor = 999
    while factor >= square_root:
        if palindrome % factor == 0:
            print "%d * %d = %d" %(factor, palindrome/factor, palindrome)
            return True
        factor -= 1
    return False

main()
