from stats import (get_num_words, get_char_count, get_sorted_char_counts_pairs)
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()



def main():
    file_path = sys.argv[1]
    file_contents = get_book_text(file_path)
    char_counts = get_char_count(file_contents)
    sorted_char_counts = get_sorted_char_counts_pairs(char_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(file_contents)} total words")
    print("--------- Character Count -------")

    for pair in sorted_char_counts:
        if not pair["char"].isalpha():
            continue

        print(f"{pair["char"]}: {pair["num"]}")
    
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()
