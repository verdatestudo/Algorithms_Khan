
'''
Algorithms from Khan Academy
https://www.khanacademy.org/computing/computer-science/algorithms

Last Updated: 2016-May-11
First Created: 2016-May-11
Python 2.7
Chris
'''

def binary_search(target, target_range=False):
    '''
    Below is the pseudocode for binary search, modified for searching in an array.
    The inputs are the array, which we call array; the number n of elements in array;
    and target, the number being searched for. The output is the index in arrayoftarget:

    Let min = 0 and max = n - 1.
    Compute guess as the average of max and min, rounded down so that it is an integer.
    If array[guess] equals target, then stop. You found it! Return guess.
    If the guess was too low, that is, array[guess] < target, then set min=guess+1.
    Otherwise, the guess was too high. Set max = guess - 1.
    Go back to step two.

    '''

    if type(target) == int and target < 101:
        bin_min = 0
        bin_max = 100
        guess = (bin_max + bin_min) / 2
        count = 1

        while guess != target:
            print 'Guess No: %d ... guess is %d' %(count, guess)
            if guess > target:
                bin_max = guess - 1
            elif guess < target:
                bin_min = guess + 1
            guess = (bin_max + bin_min) / 2
            count += 1

        return 'Target was found in %d tries. Target was %d.' %(count, guess)

    elif type(target) == str:

        new_list = sorted(target_range)

        bin_min = 0
        bin_max = len(new_list)
        guess = (bin_max + bin_min) / 2
        count = 1

        while new_list[guess] != target:
            if bin_max == bin_min:
                return 'Target %s was not found.' %(target)

            if new_list[guess] > target:
                bin_max = guess - 1
            elif new_list[guess] < target:
                bin_min = guess + 1

            guess = (bin_max + bin_min) / 2
            count += 1

        return 'Target %s was found in %d tries at position %d' %(target, count, guess)

    else:
        print 'other'

def binary_search_recursive(target, bin_min=0, bin_max=100):
    '''
    Recursive guess a number
    '''
    if bin_min >= bin_max and bin_min != target:
        return -1
    elif bin_min >= bin_max and bin_min == target:
        return bin_min

    guess = (bin_min + bin_max) / 2

    if guess > target:
        bin_max = guess - 1
        return binary_search_recursive(target, bin_min, bin_max)
    elif guess < target:
        bin_min = guess + 1
        return binary_search_recursive(target, bin_min, bin_max)
    else:
        return guess

def binary_search_testing():
    '''
    Basic testing for binary search
    '''
    print binary_search(66)
    print binary_search('z', ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])
    print binary_search('oo', ['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'])

    print binary_search_recursive(66)

binary_search_testing()
