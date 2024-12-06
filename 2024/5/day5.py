def _is_right_order(rules, update):
    for i in range(len(update)):
        if i == len(update)-1:
            return True
        if [update[i], update[i+1]] not in rules:
            return False


def update_order(rules, update):
    for i in range(len(update)):
        if i == len(update)-1:
            return update
        if [update[i], update[i+1]] not in rules:
            return update_order(rules, update[:i] + [update[i+1], update[i]] + update[i+2:])


def middle_page_number(update):
    return int(update[len(update)//2])


rules, updates = [[] for _ in range(2)]
part1 = part2 = 0
with open("day5.txt") as file:
    for line in file:
        if "|" in line:
            rules.append(line.rstrip().split("|"))
        elif "," in line:
            updates.append(line.strip().split(","))

for update in updates:
    if _is_right_order(rules, update):
        part1 += middle_page_number(update)
    else:
        part2 += middle_page_number(update_order(rules, update))

print(f"\npart1 = {part1}")
print(f"part2 = {part2}")