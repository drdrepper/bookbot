def main():
    book_path = 'books/frankenstein.txt'
    text = read_book(book_path)
    print(text)

def read_book(book_path):
    with open(book_path) as f:
        return f.read()

main()
