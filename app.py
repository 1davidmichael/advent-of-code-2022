from dataclasses import dataclass


@dataclass
class Elf:
    food_calories: int


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
    print(sorted_elves[0].food_calories)


if __name__ == "__main__":
    main()
