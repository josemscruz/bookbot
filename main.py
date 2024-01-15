def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    letters = {}
    for i in range(len(text)):
        char = ""
        if text[i].isalpha():
            char = text[i].lower()
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    print(letters)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()