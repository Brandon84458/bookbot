def num_words(book_text):
    words = book_text.split()
    count = 0

    for word in words:
        count += 1

    return count

def num_chars(book_text):
    words = book_text.split()
    character_dict = {}

    for word in words:
        for i in range(0,len(word)):
            if str(word[i]).lower() in character_dict:
                character_dict[str(word[i]).lower()] += 1
            else:
                character_dict[str(word[i]).lower()] = 1
    return character_dict

def sort_on(dict):
    return dict["num"]

def sorted_dict(input_dict):
    sort_list = []
    
    for key in input_dict:
        sort_list.append({"char": str(key), "num": input_dict[key]})

    sort_list.sort(reverse=True, key=sort_on)

    return sort_list

# test_string = "My name is Brandon Dickens"
# char_dict = num_chars(test_string)

# print(sorted_dict(char_dict))
