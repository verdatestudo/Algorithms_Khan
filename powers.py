'''
Algorithms from Khan Academy
https://www.khanacademy.org/computing/computer-science/algorithms

Last Updated: 2016-May-11
First Created: 2016-May-11
Python 2.7
Chris
'''

def powers(x, n):
    '''
    Recursive function to calculate x to the power of n.
    '''

    if n < 0:
        return (1 / float(powers(x, -n)))

    if n == 0:
        return 1
    elif n % 2 == 0:
        return (x ** (n/2)) ** 2
    else:
        return powers(x, n-1) * x


print powers(2, 4), 16
print powers(2, 3), 8
print powers(3, 3), 27
print powers(2, 10), 1024
print powers(2, -3), 0.125
print powers(2, -4), 0.0625
