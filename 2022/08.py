#! /bin/env python3
import numpy as np 


def part1 (puzzle):
    forest_map = np.array(puzzle)
    result = np.zeros(forest_map.shape)

    for (x, y), num in np.ndenumerate(forest_map):
        # print(f'{x=} {y=} {num=}')
        if num > max([*forest_map[:x, y], -1]) or \
           num > max([*forest_map[x+1:, y], -1]) or \
           num > max([*forest_map[x, :y], -1]) or \
           num > max([*forest_map[x, y+1:], -1]):
            result[x,y] = 1
    return int(result.sum())


def part2 (puzzle):
    def view_length(tree_height, trees):
        if all(tree_height > tree for tree in trees):
            return len(trees)
        for index, value in enumerate(trees):
            if value >= tree_height:
                return index + 1

    forest_map = np.array(puzzle)
    result = np.zeros(forest_map.shape)

    for (x, y), num in np.ndenumerate(forest_map):
        result[x,y] = view_length(num, np.flip(forest_map[:x, y]))
        result[x,y] *= view_length(num, forest_map[x+1:, y]) 
        result[x,y] *= view_length(num, np.flip(forest_map[x, :y])) 
        result[x,y] *= view_length(num, forest_map[x, y+1:]) 
    return int(np.amax(result))



if __name__ == "__main__":
    with open("08.txt") as f:
        puzzle = []
        for n, line in enumerate(f):
            puzzle.append([])
            for i in line:
                if i != '\n':
                    puzzle[n].append(int(i))
    
    # print(part1(puzzle))

    print(part2(puzzle))
