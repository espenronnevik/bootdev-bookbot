def read(book):
    with open(book) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    letters = {}
    for c in text.lower():
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
