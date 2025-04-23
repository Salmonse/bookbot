from stats import num_words
from stats import char_count
from stats import sorted_char_count 
import sys

def get_book_text(Filepath):
    with open(Filepath) as f:
        book_text = f.read()
    return book_text

def main():
    if len(sys.argv) > 1:
        text = get_book_text(sys.argv[1])
        words = num_words(text)
        chars = char_count(text)
        sorted_chars = sorted_char_count(chars)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {words} total words")
        print("--------- Character Count -------")
        for i in sorted_chars:
            print(f"{i['char']}: {i['count']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
