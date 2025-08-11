
def get_book_text(filepath):
    """
    Takes a file path as input, opens the file using a with block, reads all contents into a string, and returns it
    """
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def book_word_count(x):
        """
        Accepts text from book as string and returns number of words in string
        """
        words = x.split()
        return len(words)

def main():
    """
    Calls get_book_text() with the relative path "book/frankenstein.txt" and prints the result
    """
    get_book = get_book_text("books/frankenstein.txt")
    num_words = book_word_count(get_book)
    print(f"{num_words} words found in the document")

### Executes the program
main()
