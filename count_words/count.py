def count_words(sentence):
    words = sentence.split()
    words = [word.lower() for word in words]
    word_count = {}
    for word in words:
        if word_count.get(word):
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1
    return word_count


print(count_words("oh what a day What a lovely day"))
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
print(count_words("don't stop believing"))
# {"don't": 1, 'stop': 1, 'believing': 1}
# As a bonus, make sure your function works well with mixed case words:

# >>> count_words("Oh what a day what a lovely day")
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
# For even more of a bonus try to get your function to ignore punctuation outside of words:

# >>> count_words("Oh what a day, what a lovely day!")
# {'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}