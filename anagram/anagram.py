def is_anagram(first, second):
    if len(first) != len(second):
        return False
    first, second = sorted(first.lower()), sorted(second.lower())
    if first != second:
        return False
    return True

# I want you to write a function that accepts two strings and returns True if the two strings are anagrams of each other.

# Your function should work like this:

print(is_anagram("tea", "eat"))
# True
print(is_anagram("tea", "treat"))
# False
print(is_anagram("sinks", "skin"))
# False
print(is_anagram("Listen", "silent"))
# True
# Make sure your function works with mixed case.

# Before you try to solve any bonuses, I recommend you try to find at least two ways to solve this problem.