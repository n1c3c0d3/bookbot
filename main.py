import sys

from stats import get_num_words, get_chars_dict, get_sorted_chars


def main():
    # Check for a command-line argument
    if len(sys.argv) < 2:
        print("Error: Please provide a path to the book file.")
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)  # Exit the program early

    print("============ BOOKBOT ============")
    book_path = (sys.argv[1])
    print(f"Analyzing book found at {book_path}...")

    text = get_book_text(book_path)

    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    chars_dict = get_chars_dict(text)
    sorted_chars = get_sorted_chars(chars_dict)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

def get_book_text(path): 
    with open(path) as f: 
        return f.read()

main()

