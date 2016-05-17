'''
Algorithms from Khan Academy
https://www.khanacademy.org/computing/computer-science/algorithms

Last Updated: 2016-May-16
First Created: 2016-May-16
Python 2.7
Chris
'''

def merge_sort(my_list):
    '''
    Merge Sort.
    '''
    if len(my_list) <= 1:
        return my_list
    else:
        mid_point = len(my_list) / 2
        left_list = merge_sort(my_list[:mid_point])
        right_list = merge_sort(my_list[mid_point:])
        return merge(left_list, right_list)

def merge(left_list, right_list):
    new_list = []
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] <= right_list[0]:
            new_list.append(left_list.pop(0))
        else:
            new_list.append(right_list.pop(0))

    if len(left_list) > 0:
        new_list.extend(left_list)

    if len(right_list) > 0:
        new_list.extend(right_list)


    return new_list

print merge_sort([2, 8, 4, 22, 20, 12, 14, 3])
print merge_sort([2, 8, 4, 22, 20, 12, -14])
