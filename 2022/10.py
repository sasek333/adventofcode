#! /bin/env python3

def part1 (puzzle):
    x_register = 1
    cycle = 1
    interesting_ticks = [20, 60, 100, 140, 180, 220]
    result = 0

    for line in puzzle:
        if cycle in interesting_ticks:
            result += cycle * x_register
        
        cycle += 1

        if not line.startswith('noop'):
            if cycle in interesting_ticks:
                result += cycle * x_register
            x_register += int(line.split()[1])
            cycle += 1

    return result


def part2 (puzzle):
    pass


if __name__ == "__main__":
    with open("10.txt") as f:
        puzzle = []
        for line in f:
            puzzle.append(line.replace('\n', ''))
    
    print(part1(puzzle))

    # print(part2(puzzle))
