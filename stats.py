def get_num_words(x):
        """
        Accepts text from book as string and returns number of words in string
        """
        words = x.split()
        return len(words)

def character_count(x):
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
            