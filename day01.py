INPUT_FILE = "input01.txt"
SUM = 2020

'''
Find two numbers that add up to 2020 and multiply them
'''
def part_1():
    input = sorted(get_nums(INPUT_FILE), reverse=True)
    for num_1 in input:
        other_num = 2020 - num_1
        for num_2 in reversed(input):
            if num_2 > other_num:
              break
            elif num_2 == other_num:
                print(f'{num_1} + {num_2} = {num_1 + num_2}')
                print(f'Part 1 answer: {num_1} * {num_2} = {num_1 * num_2}')
                return

'''
Find three numbers that add up to 2020 and multiply them
'''
def part_2():
    input = sorted(get_nums(INPUT_FILE), reverse=True)
    for num_1 in input:
        for num_2 in input:
            other_num = SUM - num_1 - num_2
            for num_3 in reversed(input):
                if num_3 > other_num:
                    break
                elif num_3 == other_num:
                    print(f'{num_1} + {num_2} + {num_3} = {num_1 + num_2 + num_3}')
                    print(f'Part 2 answer: {num_1} * {num_2} * {num_3}= {num_1 * num_2 * num_3}')
                    return


def get_nums(input_file):
    with open(input_file) as f:
        return [int(line.strip()) for line in f.readlines()]

if __name__ == '__main__':
    part_1()
    part_2()