def main():
    print(find_passwords(108457, 562041))


def find_passwords(start, end):
    password_count = 0
    for i in range(start, end + 1):
        number = str(i)
        if is_increasing(number):
            for digit in number:
                count = number.count(digit)
                if count == 2:  # if count >= 2: for oppgave 1
                    password_count += 1
                    break
    return password_count


def is_increasing(number):
    return all(True if number[digit] <= number[digit + 1] else False for digit in range(len(number) - 1))


if __name__ == '__main__':
    main()
