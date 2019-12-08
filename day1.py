from math import floor


def main():
    print(get_fuel_requirement())


def get_fuel_requirement():
    total_fuel = 0
    file = open("input.txt")
    for line in file:
        module_fuel = floor(int(line) / 3) - 2
        total_fuel += fuel(module_fuel)
    return total_fuel


def fuel(module):
    total = module
    new_fuel = floor(module / 3) - 2
    while new_fuel > 0:
        total += new_fuel
        new_fuel = floor(new_fuel / 3) - 2
    return total


if __name__ == '__main__':
    main()
