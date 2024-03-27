def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open('./books/frankenstein.txt') as f:
        return f.read()

main()   

    
    
'''     
    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()
        count = 0
        words = file_contents.split()
        for word in words:
            count += 1
        print(count)

main()
'''