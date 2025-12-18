from stats import character_count, dictionify, sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        split_file = file_contents.split()
        file_len = len(split_file)
        char_count = character_count(file_contents)
        return file_len, char_count

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    length, count = get_book_text(sys.argv[1])
    new_dict = dictionify(count)
    sort_dict(new_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {length} total words")
    print("--------- Character Count -------")
    for i in new_dict:
        print(f"{i['char']}: {i['num']}")

main()
