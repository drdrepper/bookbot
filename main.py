def main():
    book_path = 'books/frankenstein.txt'
    text = read_book(book_path)
    num_words = get_num_words(text)
    char_iterate = char_count(text)
    dict_list = get_dict_list(char_iterate)
    dict_list.sort(reverse=True, key=sort_on)
    print(f"{num_words} words found in the document")
    for i in range (0, len(dict_list)):
        for key in dict_list[i]:
            print(f"the letter {key} appears {dict_list[i][key]} times")
        

def get_num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    char_dict = {}
    text_low = text.lower()
    for k in text_low:
        char_dict[k] = 0
    for k in text_low:
        char_dict[k] += 1
    return char_dict

def get_dict_list(char_iterate):
    dict_list = []
    pair_dict = {}
    for k in char_iterate:
        if k.isalpha() == True :
            pair_dict[k] = char_iterate[k]
            dict_list.append(pair_dict)
            pair_dict = {}
    return dict_list

def sort_on(dict_list):
    for k in dict_list :
        return dict_list[k]
    
def read_book(book_path):
    with open(book_path) as f:
        return f.read()


main()
