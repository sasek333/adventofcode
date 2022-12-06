#! /bin/env python3

from collections import deque


def part1 (puzzle):
    buff = deque(puzzle[0][:4], maxlen=4)
    for index, elem in enumerate(puzzle[0][4:]):
        # print(f"{buff=} {index=} {elem=}")
        buff.append(elem)
        if ('0' not in buff) and (len(set(buff)) == 4):        
            return index+5

def part2 (puzzle):
    buff = deque(puzzle[0][:14], maxlen=14)
    for index, elem in enumerate(puzzle[0][14:]):
        print(f"{buff=} {index=} {elem=}")
        buff.append(elem)
        if ('0' not in buff) and (len(set(buff)) == 14):        
            return index+15


if __name__ == "__main__":
    with open("2022/06.txt") as f:
        puzzle = []
        for line in f:
            puzzle.append(line.replace('\n', ''))
    
    # print(part1(puzzle))

    print(part2(puzzle))
