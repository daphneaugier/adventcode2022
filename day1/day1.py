with open("./day1/input.txt", "r") as f:
    food_list = [[int(n) for n in elf.split("\n")] for elf in f.read().rstrip().split("\n\n")]

print("Part 1 : " + str(max([sum(top_elf) for top_elf in food_list])))
print("Part 2 : " + str(sum(sorted([sum(max_cal) for max_cal in food_list])[-3:])))