def read(book):
    with open(book) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_letters(text):
    valid_letters = "abcdefghijklmnopqrstuvwxyz"
    letters = {}
    for c in text.lower():
        if c in valid_letters:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1
    return letters

def main():
    current_book = "books/frankenstein.txt"
    contents = read(current_book)
    print(f"The book contains {count_words(contents)} words")
    print(count_letters(contents))

main()
