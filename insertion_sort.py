'''
Algorithms from Khan Academy - insertion sort
https://www.khanacademy.org/computing/computer-science/algorithms

Last Updated: 2016-May-11
First Created: 2016-May-11
Python 2.7
Chris
'''

def insertion_sort(my_list):
    '''
    Now that you know how to insert a value into a sorted subarray, you can implement insertion sort:

    Call insert to insert the element that starts at index 1 into the sorted subarray in index 0.
    Call insert to insert the element that starts at index 2 into the sorted subarray in indices 0 through 1.
    Call insert to insert the element that starts at index 3 into the sorted subarray in indices 0 through 2.
    Finally, call insert to insert the element that starts at index n-1n-1n-1 into the sorted subarray in indices 0 through n-2n-2n-2.

    '''

    for item_idx in range(1, len(my_list)):
        sorted_idx = item_idx - 1
        key = my_list[item_idx]
        while my_list[sorted_idx] > key and sorted_idx >= 0:
            my_list[sorted_idx + 1] = my_list[sorted_idx]
            sorted_idx -= 1
        my_list[sorted_idx + 1] = key

    return my_list


print insertion_sort([1, 6, 55, 4, 22, -10, 6, -9, 2]), [-10, -9, 1, 2, 4, 6, 6, 22, 55]
