#! /bin/env python3

from collections import deque


def part1 (puzzle):
    buff = deque(puzzle[0][:4], maxlen=4)
    print(f"{buff}")
    for index, elem in enumerate(puzzle[0][4:]):
        print(f"{index=} {buff=} {elem=}")
        buff.append(elem)
        if ('0' not in buff) and (len(set(buff)) == 4):        
            return index+5


def part2 (puzzle):
    pass


if __name__ == "__main__":
    with open("2022/06.txt") as f:
        puzzle = []
        for line in f:
            puzzle.append(line.replace('\n', ''))
    
    print(part1(puzzle))

    # print(part2(puzzle))
