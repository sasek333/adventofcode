#! /bin/env python3

def part1 (puzzle):
    result = 0
    for line in puzzle:
        half = int(len(line)/2)
        first = line[:half]
        second = line[half:]

        common = set(first).intersection(set(second)).pop()
        if common.isupper():
            result += 26
            common = common.lower()
        result += ord(common) - ord('a') + 1        

    return result


def part2 (puzzle):
    from itertools import islice, tee
    result = 0
    for i in range(int(len(puzzle)/3)):
        try:
            common = set(puzzle[3*i]).intersection(set(puzzle[3*i+1]), set(puzzle[3*i+2])).pop()
        except KeyError:
            continue

        if common.isupper():
           result += 26
           common = common.lower()

        result += ord(common) - ord('a') + 1        


    return result


if __name__ == "__main__":
    with open("2022/03.txt") as f:
        puzzle = []
        for line in f:
            puzzle.append(line.replace('\n', ''))
    
    # print(part1(puzzle))

    print(part2(puzzle))
