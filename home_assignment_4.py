
#task 1
# Sum and multiplication of even and odd numbers.
# You are given an array of integers. Your task is to calculate two values:
# the sum of all even numbers and the product of all odd numbers in the array. Please return these two values as a list [sum_even, product_odd].


def sum_even_and_product_odd(arr: list):
    sum_even = 0
    product_odd = 1
    for i in arr:
        if i % 2 == 0:
            sum_even += i
        else:
            product_odd *= i
    return [sum_even, product_odd]
num_list = [1, 2, 3, 4]
print(sum_even_and_product_odd(num_list))

# task 2
# Sum between range values
# You are given an array of integers and two integer values, min and max.
# Your task is to write a function that finds the sum of all elements in the array that fall within the range [min, max], inclusive.


def sum_between_range(arr: list, min_val: int, max_val: int):
    arr.sort()
    result = 0
    r_list = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            result += arr[i]
            r_list.append(arr[i])
    return f'{result}, {tuple(r_list)}'
arr1 = [3, 2, 1, 4, 10, 8, 7, 6, 9, 5]
print(sum_between_range(arr1, 3, 7))




# task 3
# Stock price 2
# You are given an array of prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve.
# You may complete as many transactions as you like (buy one and sell one share of the stock multiple times).

def buy_and_sell_stock(prices: list):
    maximum = 0
    for i in range(len(prices)-1):
        if prices[i+1] - prices[i] > 0:
            maximum += prices[i+1] - prices[i]
    return maximum
prices_1 = [7, 1, 5, 3, 6, 4]
print(buy_and_sell_stock(prices_1))

# task 4
# Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the list to [1, 3, 0]

def plus_one(arr: list):
    arr[-1] += 1
    for i in reversed(range(1, len(arr))):
        if arr[i] != 10:
            break
        else:
            arr[i] = 0
            arr[i-1] += 1
            if arr[0] == 10:
                arr[0] = 1
                arr.append(0)
    return arr
n_list = [1, 2, 9,]
print(plus_one(n_list))



























