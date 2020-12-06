import re

INPUT_FILE = "input02.txt"
line_regex = r'(\d+)-(\d+) ([a-z]): ([a-z]+)'
count = 0

def part_1():
    input = get_input(INPUT_FILE)
    test = re.compile(line_regex)
    for line in input:
        (min_num, max_num, letter, password) = test.match(line).groups()

def part_2():
    print("Part 2")

def get_input(input_file):
    with open(input_file) as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    part_1()
    # part_2()