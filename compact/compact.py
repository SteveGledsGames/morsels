def compact(items):
    new_items = []
    for num, item in enumerate(items):
        if num == 0 or item != items[num-1]:
            new_items.append(item)
    return new_items



# >>> compact([1, 1, 1])
# [1]
# >>> compact([1, 1, 2, 2, 3, 2])
# [1, 2, 3, 2]
# >>> compact([])
# []