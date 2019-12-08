intcode = [1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 1, 19, 9, 23, 1, 23, 13, 27, 1, 10, 27, 31, 2,
           31, 13, 35, 1, 10, 35, 39, 2, 9, 39, 43, 2, 43, 9, 47, 1, 6, 47, 51, 1, 10, 51, 55, 2, 55, 13, 59, 1, 59, 10,
           63, 2, 63, 13, 67, 2, 67, 9, 71, 1, 6, 71, 75, 2, 75, 9, 79, 1, 79, 5, 83, 2, 83, 13, 87, 1, 9, 87, 91, 1,
           13, 91, 95, 1, 2, 95, 99, 1, 99, 6, 0, 99, 2, 14, 0, 0]


def main():
    find_pair(intcode.copy())


def run_intcode(code, noun, verb):
    code[1] = noun
    code[2] = verb
    i = 0
    while code[i] != 99:
        if code[i] == 1:
            code[code[i + 3]] = code[code[i + 1]] + code[code[i + 2]]
            i += 4
        elif code[i] == 2:
            code[code[i + 3]] = code[code[i + 1]] * code[code[i + 2]]
            i += 4
    return code


def find_pair(code):
    noun = 0
    verb = 0

    while run_intcode(code.copy(), noun, verb)[0] != 19690720:
        if noun <= 106:
            noun += 1
        else:
            verb += 1
            noun = 0
    print(noun * 100 + verb)


if __name__ == '__main__':
    main()