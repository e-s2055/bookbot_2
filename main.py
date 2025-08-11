### imports functions from stats.py 
from stats import get_num_words, character_count, chars_dict_to_sorted_list

def get_book_text(filepath):
    """
    Takes a file path as input, opens the file using a with block, reads all contents into a string, and returns it
    """
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def main():
    """
    Calls get_book_text() with the relative path "book/frankenstein.txt" and prints the result
    """
    print("============ BOOKBOT ============")
    
    book_path = "books/frankenstein.txt"
    get_book = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")

    print("----------- Word Count ----------")
    num_words = get_num_words(get_book)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")    
    char_count = character_count(get_book)
    char_sorted_list = chars_dict_to_sorted_list(char_count)
    for character in char_sorted_list:
        if not character["char"].isalpha():
            continue #Skips non-alpha chars when printing
        print(f"{character['char']}: {character['num']}")
    print("============= END ===============")

### Executes the program
main()
