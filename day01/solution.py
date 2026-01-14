from utils import Parser_1

if __name__ == "__main__":

#This is the solution for part 1
    counter = 0 # This is the counter that tracks how many times we end on zero
    ring = 100 # This represents the number of elements contained in the ring
    base = 50 # This represents the current element in the ring we are pointing to
    codes = Parser_1("input.txt")

    for code in codes:
        base = (base + code) % ring # This determines the new element that we are pointing to in the ring after the rotation
        if base == 0:
            counter += 1
    print(f"Solution for part 1: {counter}")

#This is the solution for part 2
    counter = 0
    ring = 100
    base = 50
    codes = Parser_1("input.txt")

    for code in codes:
        rotation = base + code # This is the sum of the current element and the rotation.
        if base == 0: # This is the case when our starting element is 0 and we can easily determine how many times it crosses zero from either the left or the right
            counter += abs(int((rotation)/ring))
        else: # This is the case we start at any element that is not 0
            if rotation <= 0: # This is the case that we are going left and have touched 0 at least once
                counter += 1 + abs(int((rotation)/ring))
            else: # This is the case where we are going left or right but have not crossed zero at least once as a result of going left
                counter += abs(int((rotation)/ring))
        base = (base + code) % ring # This updates the current element to the correct one
    print(f"Solution for part 2: {counter}")
