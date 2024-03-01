# modify path_to_file to the path of the file you want to read relative to the main.py file
path_to_file = "books/frankenstein.txt"

with open(path_to_file) as f:
    file_contents = f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for letter in text:
        if letter.isalpha():
            letter = letter.lower()
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters

def sort_on(dict):
    return dict["num"]

def print_report():
    num_words = count_words(file_contents)
    num_letters = count_letters(file_contents)
    num_letters = sorted(num_letters.items(), key=lambda x: x[1], reverse=True)
    print(f"--- Report for {path_to_file} ---")
    print(f"{num_words} words found in the document")
    print()
    for letter, num in num_letters:
        print(f"The '{letter}' character was found {num} times")
    print("--- End of report ---")

print_report()