import re

INPUT_FILE = "input02.txt"
line_regex = r"(\d+)-(\d+) ([a-z]): ([a-z]+)"


def part_1():
    count = 0
    input = get_input(INPUT_FILE)
    regex = re.compile(line_regex)

    for line in input:
        (min_num, max_num, letter, password) = regex.match(line).groups()
        occurrence = password.count(letter)
        if occurrence >= int(min_num) and occurrence <= int(max_num):
            count += 1
    print(f"Number of valid passwords: {count}")


def part_2():
    count = 0
    input = get_input(INPUT_FILE)
    regex = re.compile(line_regex)

    for line in input:
        (position_1, position_2, letter, password) = regex.match(line).groups()


def get_input(input_file):
    with open(input_file) as f:
        return [line.strip() for line in f.readlines()]


if __name__ == '__main__':
    part_1()
    part_2()
