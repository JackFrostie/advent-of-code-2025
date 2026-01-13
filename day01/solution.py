from utils import Parser_1

if __name__ == "__main__":
    counter = 0
    ring = 100
    base = 50
    codes = Parser_1("input.txt")

    for code in codes:
        base = (base + code) % ring
        if base == 0:
            counter += 1
print(counter)
