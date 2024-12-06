def _is_positive(lst):
    for elm in lst:
        if elm < 0:
            return False
    return True


def _is_negative(lst):
    for elm in lst:
        if elm > 0:
            return False
    return True


def _is_in_range(lst, min, max):
    for elm in lst:
        if elm < min or elm > max:
            return False
    return True


def _is_safe(lst):
    df = []
    for id, elm in enumerate(lst[1:], start=1):
        df.append(int(elm) - int(lst[id - 1]))
    if (_is_positive(df) or _is_negative(df)) and (
        _is_in_range(df, 1, 3) or _is_in_range(df, -3, -1)
    ):
        return True


with open("day2.txt") as file:
    safe = dampener = 0
    for line in file:
        levels = line.split()
        if _is_safe(levels):
            safe += 1
        else:
            debug = 0
            for i in range(len(levels)):
                t = levels[:]
                t.pop(i)
                if _is_safe(t):
                    dampener += 1
                    break

    print(f"part1 = {safe}")
    print(f"part2 = {safe + dampener}")
