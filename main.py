def main():
    book_path = "books/frankenstein.txt"
    book_report(book_path)

def get_book_contents(path: str) -> str:
    with open(path) as f:
        return f.read()

def get_word_count(book_text: str) -> int:
    words = book_text.split()
    return len(words)

def get_character_count(book_text: str) -> dict:
    counts = {}
    for word in book_text:
        word = word.lower()
        for c in word:
            if c.isalpha():
                counts[c] = counts.get(c, 0) + 1
    counts = {k: v for k,v in sorted(counts.items(), reverse=True, key = lambda x: x[1])}
    return counts

def book_report(path: str) -> None:
    book_contents = get_book_contents(path)
    word_count = get_word_count(book_contents)
    character_count = get_character_count(book_contents)
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document")
    for k, v in character_count.items():
        print(f"The '{k}' character was found {v} times")
    print("-- End report --")

if __name__ == '__main__':
    main()
