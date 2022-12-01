#! /bin/env python3

def part1 (puzzle):
    return puzzle


def part2 (puzzle):
    pass


if __name__ == "__main__":
    with open("2021/4.txt") as f:
        puzzle = []
        for line in f:
            puzzle.append(line.replace('\n', ''))
    
    print(part1(puzzle))

    # print(part2(puzzle))
