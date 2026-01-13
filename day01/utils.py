class Parser_1:
    def __init__(self, txt_path):
        self.in_text = []
        with open(txt_path, 'r') as file:
            self.in_text = [line.strip() for line in file.readlines()]

    def parse(self, inp):
        if inp[:1] == "R":
            return int(inp[1:])
        else:
            return -int(inp[1:])

    def __iter__(self):
        for line in self.in_text:
            yield self.parse(line)
