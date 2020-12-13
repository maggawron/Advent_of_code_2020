def best_result(line):
    wynik = 0
    pos = 0
    for item in line:
        length = len(item)
        map_pos = pos % length
        if item[map_pos] == "#":
            wynik += 1
        pos += 3
    return wynik


def main():
    line = []
    try:
        while True:
            string = input()
            line.append(string)
    except EOFError:
        pass
    result = best_result(line)
    print("Result is: {}".format(result))

if __name__ == "__main__":
    main()