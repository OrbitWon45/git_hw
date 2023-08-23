def swap_variables(a:int, b:int):
    print(f'a = {a}, b = {b}')
    a = a + b
    b = a - b
    a = a - b
    print(f'a = {a}, b = {b}')

test_a = 10
test_b = -5

swap_variables(test_a, test_b)

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

fizz_buzz(100)

def factorial(n: int):
    result = 1
    for i in range(2, n + 1):
        result *= i
    print(f'The factorial of {n} is {result}')

factorial(5)

def sum_of_3_digit_nums(n: int): # Is this a acceptable algorithm ?
    n = str(n)
    result = 0
    for i in n:
        result += int(i)
    print(result)

sum_of_3_digit_nums(291)

def sum_of_three_digit_nums(n: int):
    result = 0
    for i in range(3):
        current_num = n % 10
        result += current_num
        n //= 10
    print(result)

sum_of_three_digit_nums(291)


