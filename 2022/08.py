#! /bin/env python3
import numpy as np 


def part1 (puzzle):
    forest_map = np.array(puzzle)
    result = np.zeros(forest_map.shape)

    for (x, y), num in np.ndenumerate(forest_map):
        # print(f'{x=} {y=} {num=}')
        if forest_map[x, y] > max([*forest_map[:x, y], -1]) or \
           forest_map[x, y] > max([*forest_map[x+1:, y], -1]) or \
           forest_map[x, y] > max([*forest_map[x, :y], -1]) or \
           forest_map[x, y] > max([*forest_map[x, y+1:], -1]):
            result[x,y] = 1
    return int(result.sum())


def part2 (puzzle):
    pass


if __name__ == "__main__":
    with open("08.txt") as f:
        puzzle = []
        for n, line in enumerate(f):
            puzzle.append([])
            for i in line:
                if i != '\n':
                    puzzle[n].append(int(i))
    
    print(part1(puzzle))

    # print(part2(puzzle))
