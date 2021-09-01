def print_upper_words(words, first_letter):
    """Prints array of words in uppercase."""

    for word in words :
        if word[0] in first_letter:
            print(word.upper())


print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], first_letter={"h", "y"})