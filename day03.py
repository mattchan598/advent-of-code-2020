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
The answer is all the trees in each path multiplied together.
"""


def part_2():
    counts = [0, 0, 0, 0, 0]
    paths = [1, 3, 5, 7, 1]
    input = get_input(INPUT_FILE)
    line_length = len(input[0])
    places = [0, 0, 0, 0, 0]

    for index, line in enumerate(input):
        for i in range(len(places)):
            # check for the last path where you go down 2
            if i == 4 and (index % 2 != 0):
                continue
            if line[places[i]] is TREE:
                counts[i] += 1
            places[i] += paths[i]
            if places[i] > line_length - 1:
                places[i] -= line_length
    print(f"Number of trees in each path: {counts}")
    ans = 1
    for num in counts:
        ans *= num
    print(f"Final Answer: {ans}")


def get_input(input_file):
    with open(input_file) as f:
        return [line.strip() for line in f.readlines()]


if __name__ == '__main__':
    part_1()
    part_2()
