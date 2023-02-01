
import os


def l33t_code(word):
    if word.endswith("er"):
        word = word[:-2] + "xor"
    
    if "o" in word or "O" in word:
        word.replace("o","0").replace("O","0")
    if "e" in word or "E" in word:
        word.replace("e","3").replace("E","3")
    if "i" in word or "I" in word:
        word.replace("i","1").replace("I","1")
    return word

def copy_file(src_file, dst_file):
    with open(src_file, "r") as src:
        with open(dst_file, "w") as dst:
            lines = src.readlines()
            pages_to_copy = [lines[i:i+25] for i in range(0, len(lines), 25)]
            for page in pages_to_copy:
                page_text = "".join(page)
                page_text = l33t_code(page_text)
                dst.write(page_text)
    return dst_file

def report(dst_file):
    with open(dst_file, "r") as dst:
        text = dst.read()
        pages = len(text.split("\n\n"))
        lines = len(text.split("\n"))
        words = len(text.split(" "))
        alpha_chars = sum(c.isalpha() for c in text)
        num_chars = sum(c.isdigit() for c in text)
    
    final_dct = {   "pages": pages,
        "lines": lines,
        "words": words,
        "alpha_chars": alpha_chars,
        "num_chars": num_chars
                }
    
    return final_dct

if __name__ == "__main__":
    src_file = input("Enter source file path: ")
    dst_file = input("Enter destination file path: ")
#     pages = list(map(int, input("Enter page numbers to copy (e.g. 1 2): ").split()))
    dst_file = copy_file(src_file, dst_file)
    report = report(dst_file)
    
    print("Pages: ", report["pages"])
    print("Lines: ", report["lines"])
    print("Words: ", report["words"])
    print("Alphabetic Characters: ", report["alpha_chars"])
    print("Numeric Characters: ", report["num_chars"])