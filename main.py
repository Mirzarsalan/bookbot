def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = letter_dict(text)
    sorted_list = []
    for char,count in chars_dict.items():
        sorted_list.append({'char': char, 'count': count})
    sorted_list.sort(reverse=True, key=sorted_by)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} were found in this document")
    for i in sorted_list:
        char = i['char']
        count = i['count']
        line_to_print = f"The letter {char} was found {count} times"
        print(line_to_print)
    print("--- End of report---")

def sorted_by(char_dict):
    return char_dict["count"]

def letter_dict(text):
    letter_count = {}
    for char in text:
        lowered = char.lower()
        if lowered.isalpha():
            if lowered in letter_count:
                letter_count[lowered] += 1
            else:
                letter_count[lowered] = 1
    return letter_count

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open('./books/frankenstein.txt') as f:
        return f.read()

main()