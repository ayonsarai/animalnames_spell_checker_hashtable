Animal Names Spell Checker

The hash table is used here to store the dictionary of words because it allows for efficient lookup of words. When `check_spelling` checks if a word is in the hash table, it can do so in constant time on average, regardless of the size of the dictionary. 
This makes the spell checker fast and scalable.

Class HashTable.__init__: This is the constructor of the `HashTable` class. It initializes an empty hash table as a dictionary.

Def .add_word: This method adds a word to the hash table. It converts the word to lowercase before adding it to ensure case-insensitivity.

Def check_word: This method checks if a word is in the hash table. It also converts the word to lowercase before checking to match the case used when adding words.

Def levenshtein_distance : This method calculates the Levenshtein distance between two words, which is the minimum number of single-character edits (insertions, deletions, or substitutions) required to change one word into the other. 
It's used to find similar words when a word is misspelled.

Def get_suggestions : This method generates suggestions for a misspelled word. It calculates the Levenshtein distance between the misspelled word and every word in the hash table, sorts the words by their distances, 
and returns the three words with the smallest distances.

Def check_spelling : This function checks the spelling of a text by splitting it into words and checking each word with `HashTable.check_word`. If a word is misspelled, it uses `get_suggestions` to generate 3 suggestions and asks the user if they meant one of the suggestions. If the user enters Yes, it returns `True`. If the user enters No, it asks the user to try inputting it again. If the user selects no again then it asks if they want to add the new word to the hash table.

DICTIONARY_FILE_PATH = is the path where the animals.txt file lives with the 20 animal names used for the dictionary.

Def load_dictionary: This function loads a dictionary of words from a file into a hash table. It reads each line from the file, strips any leading or trailing whitespace from the line to get a word, and adds the word to the hash table with `HashTable.add_word`.

Def main(): This function is the entry point of the program. It creates a hash table, loads the dictionary into the hash table, and then enters a loop to check the spelling of words.
If the user enters 'q', it ends the program. 
If the user enters a text, it checks the spelling of the text with `check_spelling`. 
After checking a text, it asks the user if they want to check another word. 
If the user says no, it ends the program(Goodbye!).
