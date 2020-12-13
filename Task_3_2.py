def best_result(line):
    global_res = 1
    options = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for o in options:
        side_j, down_j = o
        wynik = 0
        pos = 0
        for i, item in enumerate(line):
            if i % down_j == 0:
                length = len(item)
                map_pos = pos % length
                if item[map_pos] == "#":
                    wynik += 1
                pos += side_j
        global_res *= wynik

    return global_res


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