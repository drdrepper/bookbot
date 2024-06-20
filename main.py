def main():
    book_path = 'books/frankenstein.txt'
    text = read_book(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)

def read_book(book_path):
    with open(book_path) as f:
        return f.read()


main()
