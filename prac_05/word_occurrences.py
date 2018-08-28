words_dictionary = {}
user_text = input("Enter text: ")
words = user_text.split()
for word in words:
    number_of_occurrences = words_dictionary.get(word, 0)
    words_dictionary[word] = number_of_occurrences + 1
words = list(words_dictionary.keys())
words.sort()
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, words_dictionary[word]))
