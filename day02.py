import re

INPUT_FILE = "input02.txt"
line_regex = r"(\d+)-(\d+) ([a-z]): ([a-z]+)"



'''
Find number of valid passwords in input.
Each line gives the password policy and then the password.
The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
i.e. "1-3 a: abcde"
'''
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


"""
Find number of valid passwords in input.
Each line gives the password policy and then the password.
The first and second numbers describe positions in the password (first letter is 1).
Exactly one of these poisitions must contain the given letter.
"""
def part_2():
    count = 0
    input = get_input(INPUT_FILE)
    regex = re.compile(line_regex)

    for line in input:
        (position_1, position_2, letter, password) = regex.match(line).groups()
        if (password[int(position_1)-1] is letter and password[int(position_2)-1] is not letter) or (password[int(position_2)-1] is letter and password[int(position_1)-1] is not letter):
            count += 1
    print(f"Number of valid passwords: {count}")

def get_input(input_file):
    with open(input_file) as f:
        return [line.strip() for line in f.readlines()]


if __name__ == '__main__':
    part_1()
    part_2()
