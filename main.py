import sys
from stats import get_num_words
from stats import get_num_char
from stats import get_count
from stats import sorted_dict

def get_book_text(pth):
    with open(pth) as f:
        contents = f.read()

    return contents

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    listed_dict = sorted_dict(path_to_book)

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(path_to_book)} total words")
    
    print("--------- Character Count -------")
    for item in listed_dict:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")



main()