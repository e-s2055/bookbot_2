
# get_book_text(filepath): Takes a file path as input, opens the file using a with block, reads all contents into a string, and returns it
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents
    
#main(): Calls get_book_text() with the relative path "book/frankenstein.txt" and prints the result
def main():
    get_book = get_book_text("books/frankenstein.txt")
    print(get_book)

#main(): Executes the program
main()