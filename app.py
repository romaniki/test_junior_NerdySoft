def find(string, character):
    """Function to find indexes of the searched character in the given word"""
    return [i for i, letter in enumerate(string) if letter == character]


class Vocabulary:
    """ An utility program for counting words that includes specific letters. """
    def __init__(self, words: list):
        self.words = words
        self.found_words = []
        self.counter = 0
    
    def add(self, word):
        self.words.append(word)
    
    def find_occurrences(self, searched_letters: str):
        """This method updates counter and adds all words which match user's query to the list"""

        for word in self.words:
            temp_check_indexes = []
            for letter in searched_letters:
                indexes = find(word, letter)
                for index in indexes:
                    if index not in temp_check_indexes:
                        temp_check_indexes.append(index)

            res = ''.join([word[index] for index in temp_check_indexes])
            if searched_letters in res:
                self.counter += 1
                self.found_words.append(word)
                
    def show(self):
        # For demonstration purposes we will show only 2 words at a time
        for i in range(0, len(self.found_words), 2):
            yield self.found_words[i:i+2]

def app():
    while True:  
        vocabulary = []  
        while True:

            """Load a vocabulary (append or replace)"""
        
            decision = input("Type 'c' to create a new vocabulary\
                \nType 'a' to append words to the existing vocabulary. For instance: \"book laptop car cat\"\nType 'pass' if you want to continue to work with created vocabulary\nType your command here: ")
            if decision == 'c':
                input_words = input("Enter a space separated list of words. /"
                                    "For instance: cat book python\nEnter your list here: ")
                list_words = input_words.split(' ')
                vocabulary = list_words
            elif decision == 'a':
                if vocabulary:
                    append_words = input("Enter words to append them to an existing vocabulary: ")
                    words_list_append = append_words.split(' ')
                    vocabulary.extend(words_list_append)
                else:
                    print("Vocabulary wasn't created!")
                    break
            elif decision == 'pass':
                if vocabulary:
                    pass
                else:
                    print("Vocabulary wasn't created!")
                    break
            else:
                print("Incorrect input! Please try again")
                break
            
            """Add a new word to vocabulary."""

            v = Vocabulary(vocabulary)
            add_word = input("You can add word here. Type 's' to skip: ")
            if add_word == 's':
                pass
            else:
                v.add(add_word)
            print(vocabulary)
            
            """Find exact number of words that contain provided letters (a word should contain all letters)"""

            search_query = input('Enter a query: ')
            v.find_occurrences(search_query)
            print(f"Input: {search_query}, Result: {v.counter}")
            
            """Show words that contain provided letters (think of how a user would want to see a list of words, e.g. don’t show 100500 words if he inputs just one letter."""

            gen = v.show()
            while True:
                show_words = input("You can display 2 words at a time.\
                    \nType 'show' to display words that match provided query.\
                    \nType 'exit' to finish the search.\nInput command here: ")
                if show_words == 'show':
                    try:
                        print(*next(gen))
                    except StopIteration:
                        print("There are no more items in the searched results!")
                        break
                elif show_words == 'exit':
                    break

if __name__ == "__main__":
    app()
