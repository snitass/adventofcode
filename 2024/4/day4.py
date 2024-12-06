def find_instance(arr, word, x, y, direction):
    if x < 0 or x > len(arr[0]) - 1 or y < 0 or y > len(arr) - 1:
        return False

    if arr[x][y] == word[0]:
        return True if len(word) == 1 else find_instance(arr, word[1:], x + direction[1], y + direction[0], direction)
    else:
        return False


arr, part1, part2, t = [], [], [], []
directions1 = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]
directions2 = [[-1, -1], [1, -1], [-1, 1], [1, 1]]
with open("day4.txt") as file:
    for line in file:
        arr.append(list(line.rstrip()))

for i in range(len(arr)):
    for j in range(len(arr[0])):
        for direction in directions1:
            if find_instance(arr, "XMAS", i, j, direction):
                part1.append([[i, j]])
        for direction in directions2:
            if find_instance(arr, "MAS", i, j, direction):
                t.append([i + direction[1], j + direction[0]])
for elm in t:
    if t.count(elm) == 2:
        part2.append(elm)

print(f"part1 = {len(part1)}")
print(f"part2 = {int(len(part2)/2)}")
