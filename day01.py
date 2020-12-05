INPUT_FILE = "input01.txt"
SUM = 2020

def part_1():
    input = sorted(get_nums(INPUT_FILE), reverse=True)
    for num_1 in input:
        other_num = 2020 - num_1
        for num_2 in reversed(input):
            if num_2 > other_num:
              break
            elif num_2 == other_num:
                print(f'{num_1} + {num_2} = {SUM}')
                print(f'Answer is {num_1} * {num_2} = {num_1 * num_2}')
                return

def part_2():
    


def get_nums(input_file):
    with open(input_file) as f:
        return [int(line.strip()) for line in f.readlines()]

if __name__ == '__main__':
    part_1()