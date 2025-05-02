def count_words(text):
    word_list = text.split()
    word_count = len(word_list)

    return word_count

def count_chars(text):
    lower_txt = text.lower()
    char_dict = {}

    for c in lower_txt:
        if c in char_dict.keys():
            char_dict[c] += 1
        else:
            char_dict[c] = 1

    return char_dict
