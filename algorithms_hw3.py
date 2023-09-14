# Task 1. Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.

def find_two_lowest(arr: list):
    arr.sort()
    return f'{arr[0]}, {arr[1]}'
list_of_num = [32, 40, 9, 66, 0, 10]
print(find_two_lowest(list_of_num))

# Task 2
# Given a list of numbers, return the inverse of each. Each positive becomes a negative, and the negatives become positives.

def invert_list(arr: list):
    for i in range(len(arr)):
        arr[i] = -arr[i]
    return arr
list1 = [1, -2, 3, -4, 5, -6, 0]
print(invert_list(list1))

# Task 3
# Implement a function that returns the difference between the largest and the smallest value in a given list.
# The list contains positive and negative numbers. All elements are unique.

def max_diff(arr: list):
    arr.sort()
    if len(arr) == 0:
        return 0
    else:
        result = arr[-1] - arr[0]
    return f'{arr[-1]} - {arr[0]} = {result}'
list_num = [10, -15, 5, 0, 2, 9]
print(max_diff(list_num))

# Task 4
# Write a function that counts the number of elements in a given list larger than their adjacent neighbors.

def count_larger_neighbors(arr: list):
    larger_nums = []
    count_var = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i+1]:
            count_var+=1
            larger_nums.append(arr[i])
    return f'{count_var}{tuple(larger_nums)}'
list_of_nums = [76, 82, 60, 2, 17, 4, 25, 24]
print(count_larger_neighbors(list_of_nums))

# Task 5
# Given an array. Find the minimum element in the list and subtract it from each element in the array

def subtract_min(arr: list):
    min_element = min(arr)
    for i in range(len(arr)):
        arr[i] = arr[i] - min_element
    return arr
list_num_1 =  [9, 2, 5, 4, 7, 6, 3, 1]
print(subtract_min(list_num_1))


















