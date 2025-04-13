from stats import *
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])

    count_words = num_words(book_text)
    count_chars = num_chars(book_text)

    character_dict = sorted_dict(count_chars)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(character_dict)):
        if character_dict[i]["char"].isalpha():
            print(f"{character_dict[i]["char"]}: {character_dict[i]["num"]}")
    print("============= END ===============")


main()


