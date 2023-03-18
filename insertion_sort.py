'''
implementation of insertion sort ascending order
blog post: www.blinkingcursors.in/dsa/insertion_sort
'''

import random
from datetime import datetime



random_array = []
for i in range(1, 100001):
    random_array.append(random.randint(-100000000, 100000000))


start = datetime.now()

def insertion_sort_ascending(list):
    start = datetime.now()
    for j in range(1, len(list)):
        key = list[j]
        i = j-1
        while i >=0 and list[i] > key:
            list[i+1] = list[i]
            i = i-1
        list[i+1] = key
    return list

def insertion_sort_descending(list):
    start = datetime.now()
    for j in range(1, len(list)):
        key = list[j]
        i = j-1
        while i >=0 and list[i] < key:
            list[i+1] = list[i]
            i = i-1
        list[i+1] = key
    return list


if __name__ == '__main__':
    # list = [5, 2, 4, 6, 1, 3]
    print("Unsorted list:", random_array)
    print("Sorted list ascending:", insertion_sort_ascending(random_array))
    print("Sorted list descending:", insertion_sort_descending(random_array))
    print("Time taken:", datetime.now() - start)
    
'''
10^1 : 0:00:00.000961
10^2 : 0:00:00.003793
10^3 : 0:00:00.102799
10^4 : 0:00:09.767171
10^5 : 0:27:24.598726
'''