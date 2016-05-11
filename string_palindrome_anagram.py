
'''
Algorithms from Khan Academy
https://www.khanacademy.org/computing/computer-science/algorithms

Last Updated: 2016-May-11
First Created: 2016-May-11
Python 2.7
Chris
'''

def check_palindrome(my_string):
    '''
    Recursive function to check if a string is a palindrome.
    '''
    if len(my_string) <= 1:
        return True

    if my_string[0] != my_string[-1]:
        return False
    else:
        return check_palindrome(my_string[1:-1])

def check_anagram(my_string, second_string):
    '''
    Recursive function to check if two strings are an anagram.
    '''
    if len(my_string) <= 1:
        return True

    if len(my_string) != len(second_string):
        return False

    for idx, letter in enumerate(second_string):
        if letter == my_string[0]:
            return check_anagram(my_string[1:], second_string[0:idx] + second_string[idx+1:])

    return False

print check_palindrome('racecar'), True
print check_palindrome('noon'), True
print check_palindrome('church'), False

print check_anagram('maro', 'ramo'), True
print check_anagram('mmmn', 'nnmm'), False
print check_anagram('church', 'church'), True
