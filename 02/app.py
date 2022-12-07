from dataclasses import dataclass


@dataclass
class Elf:
    food_calories: int


def get_calories(elves):
    total_calories = 0
    for elf in elves:
        total_calories += elf.food_calories

    return total_calories


def main():
    elves = []
    txt_file = open("elves.txt", "r")
    content = txt_file.readlines()

    elf_number = 0
    for index, line in enumerate(content):
        line = line.strip("\n")
        if index == 0:
            elves.append(Elf(food_calories=int(line)))
        if not line and index != 0:
            print(line)
            elves.append(Elf(food_calories=0))
            elf_number += 1
        else:
            elves[elf_number].food_calories += int(line)

    sorted_elves = sorted(elves, key=lambda x: x.food_calories, reverse=True)
    print("Part 1 Answer: " + str(sorted_elves[0].food_calories))
    print("Part 1 Answer: " + str(get_calories(sorted_elves[0:3])))


if __name__ == "__main__":
    main()
