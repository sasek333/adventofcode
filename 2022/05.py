#! /bin/env python3
import re

def part1 (puzzle):
    stacks = [[], [], [], [], [], [], [], [], []]
    for line in puzzle:
        if not line or line[0] == ' ':
            continue
        elif line[0] == '[':
            for idx in range(len(line)//4+1):
                item = line[idx*4+1]
                if item != ' ':
                    stacks[idx] += item
        else:
            _, num, _, from_stack, _, to_stack = line.split()
            num = int(num)
            from_stack = int(from_stack)-1
            to_stack = int(to_stack)-1
            # print(f"{num=} {from_stack=} {to_stack=}")

            for n in range(num):
                item = stacks[from_stack].pop(0)
                stacks[to_stack].insert(0, item)
    return ''.join([stack[0] for stack in stacks])


def part2 (puzzle):
    pass


if __name__ == "__main__":
    with open("2022/05.txt") as f:
        puzzle = []
        for line in f:
            puzzle.append(line.replace('\n', ''))
    
    print(part1(puzzle))

    # print(part2(puzzle))
