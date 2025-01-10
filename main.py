def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    list_of_char = convert_dict_to_list(char_count)
    list_of_char.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document\n")

    for c in list_of_char:
        if c["name"].isalpha():
            print(f"The \'{c["name"]}\' character was found {c["num"]} times")

    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_dict = {}
    for c in text:
        c = c.lower()
        if c in char_dict:
            char_dict[c] += 1
        else:
            char_dict[c] = 1
    return char_dict 

def convert_dict_to_list(d):
    new_list = []
    for key in d:
        new_list.append({"name": key, "num": d[key]})
    return new_list

def sort_on(dict):
    return dict["num"]

main()