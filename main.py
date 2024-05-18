def read(book):
    with open(book) as f:
        return f.read()


def count_words(text):
    return len(text.split())


def count_letters(text):
    chars = {}
    charlist = []
    for c in text.lower():
        if c.isalpha():
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1
    for c in chars:
        charlist.append({"char": c, "count": chars[c]})
    charlist.sort(reverse=True, key=char_sort)
    return charlist


def char_sort(dict):
    return dict["count"]


def print_report(book, words, chars):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document")
    print("")
    for chardict in chars:
        print(f"The {chardict['char']} character was found {chardict['count']} times")
    print("--- End of report ---")


def main():
    current_book = "books/frankenstein.txt"
    contents = read(current_book)
    print_report(current_book, count_words(contents), count_letters(contents))


main()
