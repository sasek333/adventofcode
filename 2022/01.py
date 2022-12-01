#! /bin/env python3

def part1 (puzzle):
    max_calories = 0
    current_calories = 0

    for i in puzzle:
        if not i:
            max_calories = max_calories if (max_calories >= current_calories) else current_calories
            current_calories = 0
            continue
        else:
            current_calories += int(i)

    return max_calories


def part2 (puzzle):
    pass


if __name__ == "__main__":
    with open("2022/01.txt") as f:
        puzzle = []
        for line in f:
            puzzle.append(line.replace('\n', ''))
    
    print(part1(puzzle))

    # print(part2(puzzle))
