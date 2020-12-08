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

    for line in input:
        if line[place] is TREE:
            count += 1
        place += 3
        if (place > line_length - 1):
            place -= line_length

    print(f"Number of trees hit: {count}")

"""
Find the number of trees in each path.
Trees are denoted by a "#" in the input.
The paths are: 
    -right 1, down 1
    -right 3, down 1
    -right 5, down 1
    -right 7, down 1
    -right 1, down 2
starting at the top-left of the input.
"""
def part_2():
    count = 0

def get_input(input_file):
    with open(input_file) as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    part_1()
    part_2()