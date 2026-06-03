# Capstone 1: Smart Text & Anagram Analyzer (Complete Version)

import string

def clean_text(text):
    """Removes punctuation and converts text to lowercase."""
    text = text.lower()
    for char in string.punctuation:
        text = text.replace(char, "")
    return text

def count_words(text):
    """Returns the total number of words in the text."""
    words = text.split()
    return len(words)

def is_anagram(s1, s2):
    """Checks if two strings are anagrams."""
    s1_clean = s1.replace(" ", "").lower()
    s2_clean = s2.replace(" ", "").lower()
    
    if len(s1_clean) != len(s2_clean):
        return False
        
    return sorted(s1_clean) == sorted(s2_clean)

def recursive_anagram_guess(target_word, attempts_left):
    """A recursive mini-game to guess the anagram."""
    if attempts_left == 0:
        print(f"Game Over! The word was: {target_word}")
        return False
        
    guess = input(f"Guess an anagram for '{target_word}' ({attempts_left} attempts left): ")
    
    if guess.lower() != target_word.lower() and is_anagram(guess, target_word):
        print("🎉 Correct! You found an anagram!")
        return True
    else:
        print("❌ Incorrect or not an anagram.")
        return recursive_anagram_guess(target_word, attempts_left - 1)

def main_menu():
    """Main application loop."""
    print("=======================================")
    print("Welcome to the Smart Text Analyzer!")
    print("=======================================")
    
    while True:
        print("\nChoose an option:")
        print("1. Analyze Text (Word Count & Cleaning)")
        print("2. Check Anagrams")
        print("3. Play Anagram Guessing Game")
        print("4. Exit")
        
        choice = input("> ")
        
        if choice == '1':
            text = input("Enter text to analyze: ")
            cleaned = clean_text(text)
            count = count_words(cleaned)
            print(f"\nCleaned Text: {cleaned}")
            print(f"Word Count: {count}")
            
        elif choice == '2':
            s1 = input("Enter first phrase: ")
            s2 = input("Enter second phrase: ")
            if is_anagram(s1, s2):
                print("✅ They are anagrams!")
            else:
                print("❌ They are NOT anagrams.")
                
        elif choice == '3':
            recursive_anagram_guess("listen", 3)
            
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()
