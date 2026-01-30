import pytest
from algorithms import *


# 1. Reverse Integer
def test_reverse_integer():
    assert reverse_integer(123) == 321
    assert reverse_integer(-456) == -654
    assert reverse_integer(0) == 0


# 2. First Non-Repeating Character
def test_first_non_repeating():
    assert first_non_repeating_char("aabbcdd") == "c"
    assert first_non_repeating_char("aabb") is None
    assert first_non_repeating_char("") is None


# 3. Two Sum
def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9)
    assert not two_sum([1, 2, 3], 7)
    assert not two_sum([], 5)


# 4. Palindrome
def test_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert not is_palindrome("hello")
    assert is_palindrome("")


# 5. Maximum Consecutive Sum
def test_max_consecutive_sum():
    assert max_consecutive_sum([1, 2, 3, 4, 5], 2) == 9
    assert max_consecutive_sum([-1, -2, -3], 2) == -3
    with pytest.raises(ValueError):
        max_consecutive_sum([1], 2)


# 6. Fibonacci
def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55


# 7. Remove Duplicates
def test_remove_duplicates():
    assert remove_duplicates([1, 2, 2, 3, 1]) == [1, 2, 3]
    assert remove_duplicates([]) == []


# 8. Balanced Brackets
def test_balanced_brackets():
    assert balanced_brackets("{[()]}")
    assert not balanced_brackets("{[(])}")
    assert balanced_brackets("")


# 9. Rotate List
def test_rotate_list():
    assert rotate_list([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]
    assert rotate_list([], 3) == []


# 10. Longest Common Prefix
def test_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
    assert longest_common_prefix(["dog", "racecar"]) == ""
    assert longest_common_prefix([]) == ""


# 11. Missing Number
def test_missing_number():
    assert find_missing_number([3, 0, 1]) == 2
    assert find_missing_number([0, 1]) == 2


# 12. Anagram Checker
def test_anagrams():
    assert are_anagrams("listen", "silent")
    assert are_anagrams("Dormitory", "Dirty room")
    assert not are_anagrams("hello", "world")
