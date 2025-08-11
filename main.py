### imports function from stats.py 
from stats import get_num_words
from stats import character_count

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
    get_book = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(get_book)
    print(f"{num_words} words found in the document")
    char_count = character_count(get_book)
    print(f"{char_count}")

### Executes the program
main()
