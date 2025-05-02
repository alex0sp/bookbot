from stats import count_words, count_chars

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    book_content = get_book_text("books/frankenstein.txt")
    count = count_words(book_content)
    print(f"{count} words found in the document", count)
    print(count_chars(book_content))

main()
