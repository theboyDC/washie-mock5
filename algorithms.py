def reverse_integer(n: int):
    converted_to_string = str(n)
    reversed_numbers = converted_to_string[::-1]
    lst = []
    
    for char in reversed_numbers:
        if char == "-":
            lst.insert(0, char)
        else:
            lst.append(char)
    joining = int("".join(lst))
    return joining
   
# print(reverse_integer(-456))


def first_non_repeating_char(text: str):
        print(first_non_repeating_char("aabbcdd"))
        pass






def two_sum(nums: list, target: int):
    for num in nums:
        print(num)
        for i in range(len(nums)):
            pass
    
print(two_sum([2, 7, 11, 15], 9))

# def is_palindrome(text: str) -> bool:
#     pass


# def max_consecutive_sum(nums: list, k: int) -> int:
#     pass


# def fibonacci(n: int, memo=None) -> int:
#     pass


# def remove_duplicates(items: list) -> list:
#     pass


# def balanced_brackets(text: str) -> bool:
#     pass


# def rotate_list(items: list, k: int) -> list:
#     pass


# def longest_common_prefix(words: list) -> str:
#     pass


# def find_missing_number(nums: list) -> int:
#     pass


# def are_anagrams(s1: str, s2: str) -> bool:
#     pass
