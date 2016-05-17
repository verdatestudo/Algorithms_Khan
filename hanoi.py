'''
Algorithms from Khan Academy
https://www.khanacademy.org/computing/computer-science/algorithms

Last Updated: 2016-May-14
First Created: 2016-May-14
Python 2.7
Chris
'''

# this is a total copy. need to think more about this.

def hanoi(n, source, helper, target, second=False):
    if n > 0:
        # move tower of size n - 1 to helper:
        hanoi(n - 1, source, target, helper)
        # move disk from source peg to target peg
        if source[0]:
            disk = source[0].pop()
            target[0].append(disk)
        # move tower of size n-1 from helper to target
        hanoi(n - 1, helper, source, target, True)

source = ([x for x in range(3, 0, -1)], "source")
target = ([], "target")
helper = ([], "helper")
hanoi(len(source[0]),source,helper,target)


#print source, helper, target
