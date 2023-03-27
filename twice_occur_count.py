'''

Given an integer array data of size arr_size where the minimum size of array is 1. Each
integer appears once or twice. Write a function which will return an array of all the integers
that appear twice. Ignore the integer if it appears three or more number of times.
Example1:
data = [10, 12, 10, 11, 13, 17, 16, 15, 11]
output = [10, 11]
Example 2:
data = [7, 3, 8, 6, 4, 6, 7, 8, 9, 8, 7]
output = [6]

'''

def twice_occur_count(list):
    count_dict = {} #create an empty dict to keep count
    for i in range(0, len(list)):
        count_dict[list[i]] = list.count(list[i]) #filling the dict for each element
    print(count_dict)

    output_list = [] #create a blank list for output
    for key, value in count_dict.items(): #iterate over the dict
        if value == 2: #we need twice count
            output_list.append(key) #fill the list with key whose count is 2
    print(output_list)



if __name__ == '__main__':
    twice_occur_count( [7, 3, 8, 6, 4, 6, 7, 8, 9, 8, 7, -1, -2, 0, -1, 9, 2, 8, 15, 19, 154, 1872, 19, 0, 19])