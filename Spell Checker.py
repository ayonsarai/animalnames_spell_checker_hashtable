# Sarai Ayon
# 5/8/24
# CS240 Data Structures and Algorithms
# Midterm - Spell Checker

import os # Import the os module

class HashTable: # Hash table class
    def __init__(self):
        self.table = {}

    def add_word(self, word): # Add word function
        self.table[word.lower()] = True

    def check_word(self, word): # Check word function
        return word.lower() in self.table

    def levenshtein_distance(self, word1, word2): # Levenshtein distance function
        size_x = len(word1) + 1 # Get the size of the words
        size_y = len(word2) + 1 
        matrix = [[0 for _ in range(size_y)] for _ in range(size_x)] # Create a matrix
        for x in range(size_x): # Fill the matrix
            matrix [x][0] = x
        for y in range(size_y): 
            matrix [0][y] = y

        for x in range(1, size_x): # Calculate the distance
            for y in range(1, size_y): 
                if word1[x-1] == word2[y-1]:
                    matrix [x][y] = min(
                        matrix[x-1][y] + 1,
                        matrix[x-1][y-1],
                        matrix[x][y-1] + 1
                    )
                else: 
                    matrix [x][y] = min(
                        matrix[x-1][y] + 1,
                        matrix[x-1][y-1] + 1,
                        matrix[x][y-1] + 1
                    ) 
        return matrix[size_x - 1][size_y - 1]

    def get_suggestions(self, word): # Get suggestions function
        distances = [(w, self.levenshtein_distance(word, w)) for w in self.table] # Calculate the distance between the word and the words in the dictionary
        suggestions = sorted(distances, key=lambda x: x[1])
        return [s[0] for s in suggestions[:3]]

def check_spelling(text, hash_table): # Check spelling function
    words = text.split()
    for word in words:
        if hash_table.check_word(word.lower()):
            print(f"Great Job! The word '{word}' is spelled correctly!")
            return True 
        else:
            print(f"'{word}' is misspelled.") # If the word is misspelled
            suggestions = hash_table.get_suggestions(word)
            if suggestions:
                print(f"Did you mean: {', '.join(suggestions)}?")
                while True:
                    correct_suggestion = input("Was this what you meant? (y/n): ").lower()
                    if correct_suggestion in ['yes', 'y']:
                        return True 
                        break
                    elif correct_suggestion in ['no', 'n']: # If the suggestion is not correct
                        word = input("Please input the word again: ")
                        if hash_table.check_word(word.lower()):
                            print(f"Great Job! The word '{word}' is spelled correctly!")
                            break
                        else:
                            print(f"'{word}' is misspelled.")
                    else:
                        print("Invalid input. Try again!")
            else: # If there are no suggestions
                print(f"We don't have any suggestions for '{word}'.")
                add_word = input(f"Hmm, we don't have '{word}' yet. Would you like to add it? (y/n): ").lower()
                if add_word in ['yes', 'y']:
                    confirm_add = input(f"Are you sure you want to add '{word}' to the dictionary? (y/n): ").lower()
                    if confirm_add in ['yes', 'y']:
                        hash_table.add_word(word)
                        print(f"'{word}' has been added to the dictionary.")

# Load the dictionary
DICTIONARY_FILE_PATH = r"C:\Users\Sarai Ayon\OneDrive - Whatcom Community College\Spring 2024\CS240 Database Structure & Algorithms\Midterm\animals.txt"
def load_dictionary(file_path, hash_table): 
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            hash_table.add_word(word)


def main(): # Main function
    hash_table = HashTable() # Create a hash table
    load_dictionary(DICTIONARY_FILE_PATH, hash_table) # Load the dictionary
    print("Welcome to the spell checker!")
    while True: # Loop to check spelling
        text = input("Enter text to check spelling or 'q' to quit: ")
        if text.lower() == 'q':
            print("Goodbye!")
            break
        check_spelling(text, hash_table) # Check spelling
        while True: # Loop to check another word
            continue_check = input("Do you want to check another word? (yes/no): ").lower()
            if continue_check in ['yes', 'y']:
                break
            elif continue_check in ['no', 'n']:
                print("Goodbye!")
                return
            else:
                print("Invalid input. Try again!")

if __name__ == "__main__": # Run the main function
    main()