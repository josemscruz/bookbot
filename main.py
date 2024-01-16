def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters = {}
    for i in range(len(text)):
        char = ""
        if text[i].isalpha():
            char = text[i].lower()
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1

    sorted_letters = dict(sorted(letters.items(), key = lambda item: item[1], reverse=True))

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document\n")
    for l in sorted_letters:
        print(f"The '{l}' character was found {letters[l]} times")
    print("--- End report ---")
    
def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()