INPUT_FILE = "input01.txt"

def part_1():
    input = get_nums(INPUT_FILE)
    print(sorted(input))

def get_nums(input_file):
    with open(input_file) as f:
        return [int(line.strip()) for line in f.readlines()]

if __name__ == '__main__':
    part_1()