#! /bin/env python3

def part1 (puzzle):
    from collections import defaultdict

    filepath = []
    sizes = defaultdict(int)
    total = 0
    max_size = 100000

    # parse input commands
    for line in puzzle:
        # change directories
        if (line.startswith('$ cd')):
            directory = line.split()[-1]
            # go to previous directory
            if(directory == '..'):
                filepath.pop()
                continue
            # add directory to filepath
            else:
                filepath.append(directory)
                continue

        # list contents
        elif (line.startswith('$ ls')):
            continue
        
        # parse ls output for sizes
        else:
            size, _ = line.split()
            if (size.isdigit()):
                size = int(size)
                for i in range(len(filepath)):
                    sizes['/'.join(filepath[:i+1])] += size

    # calculate sum of directories with size at most 100k
    for key, value in sizes.items():
        if (value <= 100_000):
            total += value    
    
    return total


def part2 (puzzle):
    from collections import defaultdict

    filepath = []
    sizes = defaultdict(int)

    # parse terminal output
    for line in puzzle:
        # change directories
        if (line.startswith('$ cd')):
            directory = line.split()[-1]
            # go to previous directory
            if (directory == '..'):
                filepath.pop()
            # add directory to filepath
            else:
               filepath.append(directory)

        # list contents
        elif (line.startswith('$ ls')):
            continue
    
        # parse ls output for sizes
        else:
           size, _ = line.split()
           if(size.isdigit()):
               size = int(size)
               for i in range(len(filepath)):
                  sizes['/'.join(filepath[:i+1])] += size

    total_space = 70000000
    update_size = 30000000
    used_space = sizes['/']
    free_space = total_space - used_space
    space_needed = update_size - free_space

    # find eligible directories to delete
    options = []
    for _,value in sizes.items():
        if(value > space_needed):
            options.append(value)

    print(options)
    # print answer
    return (min(options))


if __name__ == "__main__":
    with open("07.txt") as f:
        puzzle = []
        for line in f:
            puzzle.append(line.replace('\n', ''))
    
    print(part1(puzzle))

    print(part2(puzzle))
