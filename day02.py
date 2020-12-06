INPUT_FILE = "input02.txt"

def part_1():
    print("Part 1")

def part_2():
    print("Part 2")

def get_input(input_file):
    with open(input_file) as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    part_1()
    part_2()