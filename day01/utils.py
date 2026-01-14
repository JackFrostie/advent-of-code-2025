# This class is a generator to store and parse the input into negative or positive integer numbers
class Parser_1:
    def __init__(self, txt_path):
        # Initializes the storage of a list of strings
        self.in_text = []
        with open(txt_path, 'r') as file:
            self.in_text = [line.strip() for line in file.readlines()]

    def parse(self, inp):
        # This function parses the strings into either negative or positive integers
        if inp[:1] == "R":
            return int(inp[1:])
        else:
            return -int(inp[1:])

    def __iter__(self):
        # This is a generator function that returns the parsed value
        for line in self.in_text:
            yield self.parse(line)
