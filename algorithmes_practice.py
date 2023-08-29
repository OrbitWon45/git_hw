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
def reverse_number(n: int):
    n = str(n)
    if n[0] == '-':
        return int('-' + n[ :0:-1])
    else:
        return int(n[ : :-1])
print(reverse_number(-2131))


def reverse_string(s: str):
    return s[::-1]
print(reverse_string('tacocat spelled backwards is tacocat.'))


def they_are_a_anagram(n: str, n_1: str):
    print(f'{n} and {n_1} are a anagram!')
    return len(n) == len(n_1) \
        and sorted(n.lower()) == sorted(n_1.lower())
print(they_are_a_anagram('taco', 'Cato'))


def it_is_a_palindrome(n:str):
    print(f'{n} is a palindrome!')
    return n.lower() == n[::-1].lower()
print(it_is_a_palindrome('Tacocat'))


def almost_a_palindrome(n: str):
    for i in range(len(n)):
        n_1 = n[:i] + n[i+1:]
        if n_1.lower() == n_1[::-1].lower():
            return f'{n} is almost a palindrome.: True'
    return f'{n} is almost a palindrome.: False'
print(almost_a_palindrome('Tackocat'))








