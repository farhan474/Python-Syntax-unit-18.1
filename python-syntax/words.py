def print_upper_words(words,must_start_with={e}):
    for word in words:
        if word.startswith(tuple(must_start_with)):
            print(word.upper())

