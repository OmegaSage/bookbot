import sys

from stats import character_count, get_num_words, sort_letter_count

num_words = None
num_letters = dict()
# global filepath
# filepath = ""


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    display_path = filepath.lstrip("/.")

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {display_path}...")
    file_contents = get_book_text(filepath)
    num_words = get_num_words(file_contents)
    num_letters = character_count(file_contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_letters = sort_letter_count(num_letters)
    for letter in sorted_letters:
        print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")


main()
