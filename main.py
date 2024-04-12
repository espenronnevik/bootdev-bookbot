def read():
    with open("books/frankenstein.txt") as f:
        contents = f.read()
    return contents

def count_words(text):
    words = text.split()
    return len(words)

def main():
    contents = read()
    numwords = count_words(contents)
    print(f"The book contains {numwords} words")

main()
