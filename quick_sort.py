'''
Algorithms from Khan Academy
https://www.khanacademy.org/computing/computer-science/algorithms

Last Updated: 2016-May-17
First Created: 2016-May-17
Python 2.7
Chris
'''

def quick_sort(my_list):

    if len(my_list) <= 1:
        return my_list

    pivot = my_list[-1]
    q = 0
    j = 0

    while j < len(my_list) - 1:
        if my_list[j] > pivot:
            j += 1
        else:
            my_list[j], my_list[q] = my_list[q], my_list[j]
            j += 1
            q += 1

    my_list[-1], my_list[q] = my_list[q], pivot

    return quick_sort(my_list[:q]) + quick_sort(my_list[q:])

print quick_sort([7, 4, 6, 2, 7, 12, 3])
print quick_sort([4, 65, 2, -31, 0, 99, 83, 782, 1])
