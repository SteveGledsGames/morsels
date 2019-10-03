# def uniques_only(dupes):
#     uniques = list(set(dupes))
#     return uniques

# using generators. Note: not sure how to use this but it passes the test. Solution came from morsels.
def uniques_only(iterable):
    seen = set()
    for item in iterable:
        if item not in seen:
            yield item
            seen.add(item)
            print(item)


unique = uniques_only([1, 2, 2, 1, 1, 3, 2, 1])
print(unique)

# [1, 2, 3]
# >>> nums = [1, -3, 2, 3, -1]
# >>> squares = (n**2 for n in nums)
# >>> uniques_only(squares)
# [1, 9, 4]

# https://www.pythonmorsels.com/exercises/b684cd595ca745398131f2252ca13064/submit/