import re


def mul(x, y):
    return x * y


part1 = part2 = 0
with open("day3.txt") as file:
    _is_enable = 1
    for line in file:
        for elm in re.findall("mul\(\d+,\d+\)", line):
            part1 += eval(elm)

        for elm in re.findall("mul\(\d+,\d+\)|don't\(\)|do\(\)", line):
            if elm == "do()":
                _is_enable = 1
            elif elm == "don't()":
                _is_enable = 0
            else:
                if _is_enable:
                    part2 += eval(elm)

print(f"part1 = {part1}")
print(f"part2 = {part2}")
