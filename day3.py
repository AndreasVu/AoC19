def main():
    print(intersect())


def intersect():
    with open('input3.txt', 'r') as f:
        lines = [path("".join(line).strip('\n').split(',')) for line in f]
    intersections = set(lines[0]).intersection(lines[1])
    return min(abs(x) + abs(y) for (x, y) in intersections)  # Finds the shortest intersection from center.
    # return 2 + min(sum(wire.index(intersect) for wire in wires) for intersect in intersections)


def path(line):
    pos = [0, 0]
    mapped_line = list()
    for element in line:
        for _ in range(int(element[1:])):
            pos[0 if element[0] in ('D', 'U') else 1] += 1 if element[0] in ('R', 'U') else -1
            mapped_line.append(tuple(pos.copy()))
    return mapped_line


if __name__ == '__main__':
    main()
