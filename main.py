def main():
    book_path = "books/frankenstein.txt"
    file_contents = get_text(book_path)
    word_count = get_word_count(file_contents)
    char_dict = get_char_dict(file_contents)
    char_list = get_char_list(char_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for li in char_list:
        print(f"The '{li["letter"]}' character was found {li["count"]} times")
    print("--- End report ---")

def get_word_count(text):
    return len(text.split())

def get_text(path):
    with open(path) as f:
        return f.read()

def get_char_dict(text):
    dict = {}
    lower_text = text.lower()
    char_set = set(lower_text)
    for char in char_set:
        char_count = lower_text.count(char)
        dict[char] = char_count
    return dict

def sort_on(dict):
    return dict["count"]

def get_char_list(dict):
    char_count_list = []
    for d in dict:
        if d.isalpha():
            new_dict = {}
            new_dict["letter"] = d
            new_dict["count"] = dict[d]
            char_count_list.append(new_dict)
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list


main()
