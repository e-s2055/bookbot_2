def get_num_words(x):
        """
        Accepts text from book as string and returns number of words in string
        """
        words = x.split()
        return len(words)

def get_chars_dict(x):
        """
        Takes text from book as a string, converts to lowercase, returns number of times characters appear; incl. symbols and spaces
        """
        lowercase = ""
        lowercase = x.lower()
        character_count = {}
        for char in lowercase:
            if char in character_count:
                   character_count[char] += 1
            else:
                   character_count[char] = 1
        return character_count

def chars_dict_to_sorted_list(x):
    """
    Creates 2 dictionaries with key-value for character and character count, sorts from greatest to least count
    """
    character_count_sorted = []
    for char in x:
          count = x[char] # Get the count that's there already
          char_dict = {"char": char, "num": count} # Create new formatting
          character_count_sorted.append(char_dict) # Adds it to the list as a pair
    character_count_sorted.sort(reverse=True, key=sort_on) # Sorts the list
    return character_count_sorted

def sort_on(x):
       return x["num"]