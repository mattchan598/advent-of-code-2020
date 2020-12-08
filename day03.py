INPUT_FILE = "input03.txt"
TREE = "#"

"""
Find the number of trees in your path.
Trees are denoted by a "#" in the input.
The path is right 3, down 1 starting at the top-left of the input.
"""
def part_1():
    count = 0
    input = get_input(INPUT_FILE) 
    line_length = len(input[0])
    place = 0

    for index, line in enumerate(input):
        if line[place] is TREE:
            count += 1
        place += 3
        if (place > line_length - 1):
            place -= line_length

    print(f"Number of trees hit: {count}")

def part_2():
    count = 0

def get_input(input_file):
    with open(input_file) as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    part_1()
    part_2()