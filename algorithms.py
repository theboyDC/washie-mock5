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
    dict = {}
    for char in text:
        dict[char] = text.count(char)
        
    for key,value in dict.items():
        if value == 1:
            return key
    
def two_sum(nums: list, target: int):
    for num in nums:
        if nums[0] + num == target:
            return True
    else:
        return False


# def is_palindrome(text: str) -> bool:
#     list_of_texts = text.lower().replace(":","").strip(",").split()
#     print(list_of_texts)
#     reversed_list = list_of_texts[::-1]
#     reversed_string = " ".join(reversed_list)
    
#     if text == reversed_string:
#         return True
#     else:
#         return False
    
#     print(reversed_string)
# print(is_palindrome("A man, a plan, a canal: Panama"))

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
