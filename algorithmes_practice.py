# def swap_variables(a:int, b:int):
#     print(f'a = {a}, b = {b}')
#     a = a + b
#     b = a - b
#     a = a - b
#     print(f'a = {a}, b = {b}')
#
# test_a = 10
# test_b = -5
#
# swap_variables(test_a, test_b)
#
# def fizz_buzz(n):
#     for i in range(1, n + 1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('fizzbuzz')
#         elif i % 3 == 0:
#             print('fizz')
#         elif i % 5 == 0:
#             print('buzz')
#         else:
#             print(i)
#
# fizz_buzz(100)
#
# def factorial(n: int):
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     print(f'The factorial of {n} is {result}')
#
# factorial(5)
#
# def sum_of_3_digit_nums(n: int): # Is this a acceptable algorithm ?
#     n = str(n)
#     result = 0
#     for i in n:
#         result += int(i)
#     print(result)
#
# sum_of_3_digit_nums(291)
#
# def sum_of_three_digit_nums(n: int):
#     result = 0
#     for i in range(3):
#         current_num = n % 10
#         result += current_num
#         n //= 10
#     print(result)
#
# sum_of_three_digit_nums(291)
#
# # Build a algorithm that completes a song that makes you smile.
#
# def its_like(n):
#     its_like_list = []
#     for i in range(1, n +1):
#         if i not in its_like_list:
#             its_like_list.append(i)
#     print(f'Its like {its_like_list}. Its kinda dangerous to b a MC.'
#           f' \n They killed Tupac and Biggie.\n'
#           f'Its the alliance of Hip Hop, Y. O. ..')
# its_like(3)
#
#
# def reverse_number(n: int):
#     n = str(n)
#     if n[0] == '-':
#         return int('-' + n[ :0:-1])
#     else:
#         return int(n[ : :-1])
# print(reverse_number(-2131))
#
#
# def reverse_string(s: str):
#     return s[::-1]
# print(reverse_string('tacocat spelled backwards is tacocat.'))
#
#
# def they_are_a_anagram(n: str, n_1: str):
#     print(f'{n} and {n_1} are a anagram!')
#     return len(n) == len(n_1) \
#         and sorted(n.lower()) == sorted(n_1.lower())
# print(they_are_a_anagram('taco', 'Cato'))
#
#
# def it_is_a_palindrome(n:str):
#     print(f'{n} is a palindrome!')
#     return n.lower() == n[::-1].lower()
# print(it_is_a_palindrome('Tacocat'))
#
#
# def almost_a_palindrome(n: str):
#     for i in range(len(n)):
#         n_1 = n[:i] + n[i+1:]
#         if n_1.lower() == n_1[::-1].lower():
#             return f'{n} is almost a palindrome.: True'
#     return f'{n} is almost a palindrome.: False'
# print(almost_a_palindrome('Tackocat'))


# list_numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# list_numbers2 = [1, 3, 5, 7, 6, 0, 2, 4, 8]
# def missing_numbers(aray1: list, aray2:list):
#     list_numbers1.sort()
#     list_numbers2.sort()
#     print(list_numbers1)
#     print(list_numbers2)
#     for i in range(len(aray2)):
#         if aray1[i] != aray2[i]:
#             return f'{aray1[i]} is missing!'
#     return f'{aray1[-1]} is missing'
# print(missing_numbers(list_numbers1, list_numbers2))
#
#
#
#
# def largest_sum(aray: list):
#     curr_sum = max_sum = aray[0]
#
#     for num in aray[1:]:
#         curr_sum = max(curr_sum + num, num)
#         max_sum = max(max_sum, curr_sum)
#     return max_sum
#
# list_1 = [-4, 2, -1, 3, 4, 10, 10, -10, -1]
# print(largest_sum(list_1))
#
#
# def is_mountain_aray(aray: list):
#     i = 1
#     while aray[i - 1] < aray[i] and i < len(aray):
#         i += 1
#     if i == 1 or i == len(aray):
#         return False
#
#     while i < len(aray) and aray[i - 1] > aray[i]:
#         i += 1
#     if i == len(aray):
#         return True
#     else:
#         return False
#
# list = [1, 3, 5, 7, 3, 2]
#
# print(is_mountain_aray(list))


# def sum_and_multi(aray: list):
#     print(aray)
#     sum1 = 0
#     multi = 1
#     for n in aray:
#         sum1 += n
#         multi = multi * n
#     return sum1, multi
# num_l = [2, 5, 11, 19]
# print(sum_and_multi(num_l))
#
#
# def find_max_index_num(arr: list):
#     max_index = 0
#     max_num = arr[max_index]
#     for n in range(1, len(arr)):
#         if arr[n] > max_num:
#             max_index = n
#             max_num = arr[n]
#     return [max_index, max_num]
# num_list = [8, 2, 12, 3]
# print(find_max_index_num(num_list))


def sum_between_min_max(aray: list):
    max_i = 0
    min_i = 0
    for i in range(len(aray)):
        if aray[i] > aray[max_i]:
            max_i = i
        elif aray[i] < aray[min_i]:
            min_i = i
    return sum(aray[min(min_i, max_i) +1:max(min_i, max_i)])
num_1_list = [4, 1, 2, 9, 14, 10]
print(sum_between_min_max(num_1_list))

def buy_and_sell_stock(prices: list):
    curr_profit = 0
    max_profit =0
    for d in range(len(prices)-1):
        curr_profit = curr_profit + prices[d+1] - prices[d]
        if curr_profit > max_profit:
            max_profit = curr_profit
        elif curr_profit < 0:
            curr_profit = 0
    return max_profit
day_prices = [7, 1, 5, 3, 6, 14 ]
print(buy_and_sell_stock(day_prices))

def buy_and_sell_stock(prices: list):
    max_prof = 0
    for i in range(len(prices)-1):
        if prices[i+1] - prices[i] > 0:
            max_prof += prices[i+1] - prices[i]
    return max_prof
prices2 = [7, 1, 5, 3, 6, 4 ]
print(buy_and_sell_stock(prices2))






















