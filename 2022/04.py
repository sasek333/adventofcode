#! /bin/env python3

def part1 (puzzle):
    result = 0
    for line in puzzle:
        first, second = line.split(',')
        first_start, first_stop = first.split('-')
        second_start, second_stop = second.split('-')


        if (int(first_start) <= int(second_start) and int(first_stop) >= int(second_stop)) or \
            (int(second_start) <= int(first_start) and int(second_stop) >= int(first_stop)):
            result += 1
            print(f"{line=} {first_start=} {first_stop=} {second_start=} {second_stop=}")

    return result


def part2 (puzzle):
    result = 0
    for line in puzzle:
        first, second = line.split(',')
        first_start, first_stop = first.split('-')
        second_start, second_stop = second.split('-')


        if (int(first_start) <= int(second_stop) and int(first_stop) >= int(second_start)) or \
         (int(second_start) <= int(first_stop) and int(second_stop) >= int(first_start)):
            result += 1
            print(f"Y {line=} {first_start=} {first_stop=} {second_start=} {second_stop=}")
        else:
            print(f"n {line=} {first_start=} {first_stop=} {second_start=} {second_stop=}")
    return result


if __name__ == "__main__":
    with open("2022/04.txt") as f:
        puzzle = []
        for line in f:
            puzzle.append(line.replace('\n', ''))
    
    # print(part1(puzzle))

    print(part2(puzzle))
