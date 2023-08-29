
# Task 1. There is a program that prints the numbers from 1 to 100. If the number is divisible of 3, print “Bin”
# If the number is divisible of 7, print “Go”. For numbers which are divisible of 3 and 7, print “BinGo”

def bin_go(n: int):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 7 == 0:
            print('BinGo')
        elif i % 3 == 0:
            print('Bin')
        elif i % 7 == 0:
            print('Go')
        else:
            print(i)

bin_go(100)

# Task 2. Compute the sum of digits in all numbers from 1 to n. When a function gets a number n,
# find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

def sum_of_nums_1_to_n(n: int):
    final_sum = 0
    for num in range(n + 1):
        final_sum = final_sum + num
    return final_sum

print(sum_of_nums_1_to_n(10))

# Level 2
# 1. Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124

def find_the_max_num(a: int, b: int, c: int):
    list_of_nums = [a, b, c]
    max_num = 0
    for n in list_of_nums:
        if n > max_num:
            max_num = n
    return max_num

print(find_the_max_num(1, -222, 3))

# 2. Leap year. When a function gets a year, the code detects if it is a leap year or not. How to approach this task
# A leap year is exactly divisible by 4
# If it’s a century year (divisible by 100), it is a leap year if it’s also divisible by 400.
# If it’s divisible by 100 and not divisible by 400, it’s not a leap year.
# Create a function that will return True if the given year is a leap year, else it will return False

def leap_year(n):
    if n % 100 == 0 and n % 400 == 0:
        return True
    elif n % 4 == 0 and not n % 100 == 0:
        return True
    else:
        return False

print(leap_year(2024))

# Level 3
# Fibonacci. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.
# Print out the Fibonacci sequence until the given n-th in the sequence.
# The task is to display all the numbers from start to n of the Fibonacci sequence.
# Follow the steps and complete the pre-code below.

def generate_fibonacci_sequence(n: int):
    fib_sequence = [0, 1]
    for i in range(2, n):
        result = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(result)
    print(fib_sequence)

generate_fibonacci_sequence(7)














