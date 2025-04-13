def num_words(book):
    words_list = book.split()
    num_words = 0

    for word in words_list:
        num_words += 1
    return num_words

def num_chars(book):
    words_list = book.split()
    char_dict = {}

    for word in words_list:
        for i in range(0,len(word)):
            if str(word[i]).lower() in char_dict:
                char_dict[str(word[i]).lower()] += 1
            else:
                char_dict[str(word[i]).lower()] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sorted_dict(dict):
    sorted_list = []

    for key in dict:
        sorted_list.append({"char": str(key), "num": dict[key]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
