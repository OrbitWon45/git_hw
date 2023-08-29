
# Level 1
# Task 1. Reverse a negative integer and keep the negative sign at the beginning.

def reverse_negative_integer(n: int):
    n = str(n)
    n = "-" + n[:0:-1]
    return int(n)
print(reverse_negative_integer(-234))


# Task 2. Write a function that takes two strings as input and returns True if they are anagrams of each other, and False otherwise.
# The strings can contain uppercase and lowercase letters, and should be ignored during the comparison.

def are_anagrams(s1: str, s2: str):
    print(f'{s1} and {s2} are anagrams!')
    return sorted(s1.lower()) == sorted(s2.lower())
print(are_anagrams('Rat', 'Tar'))


# Level 2
# Task 3. Given a sentence, reverse the order of characters in each word

def reverse_words(sentence: str):
    sentence = sentence.split()
    sentence_list = []
    for w in sentence:
        word = w[::-1]
        sentence_list.append(word)
        result = ' '.join(sentence_list) + '.'
    return result
print(reverse_words('ehT taC sah caT'))


# Task 4. Given a string made of digits [0-9], return a string where each digit is repeated a number of times equals to its value

def repeat_digits(s: str):
    result = ''
    for char in s:
        char *= int(char)
        result += str(char) + ' '
    return result
print(repeat_digits('0123456789'))


# Task 5. Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u) in a given string.
# “y” is not considered a vowel for this task. The input string is always in lowercase.

def shortcut(s: str):
    s = s.lower()
    vowel = 'aeiou'
    result = ''
    for i in s:
        if i not in vowel:
            result += i
    return result
print(shortcut('I love Trap music!'))







