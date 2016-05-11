'''
Algorithms from Khan Academy - selection sort
https://www.khanacademy.org/computing/computer-science/algorithms

Last Updated: 2016-May-11
First Created: 2016-May-11
Python 2.7
Chris
'''

def selection_sort(my_list):
    '''
    There are many different ways to sort the cards.
    Here's a simple one, called selection sort, possibly similar to how you sorted the cards above:

    Find the smallest card. Swap it with the first card.
    Find the second-smallest card. Swap it with the second card.
    Find the third-smallest card. Swap it with the third card.
    Repeat finding the next-smallest card, and swapping it into the correct position until the array is sorted.
    '''
    if len(my_list) == 1:
        return my_list

    small = float('inf')

    for idx, item in enumerate(my_list):
        if item < small:
            small = item
            small_idx = idx

    my_list[small_idx] = my_list[0]
    my_list[0] = small

    return [my_list[0]] + selection_sort(my_list[1:])


print selection_sort([1, 4, 21, 3, 8, 12, 99, 2, 2, -1]), [-1, 1, 2, 2, 3, 4, 8, 12, 21, 99]
