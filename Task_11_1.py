from copy import deepcopy

def best_result(line):

    next_order = []
    prev_order = deepcopy(line)

    while prev_order != next_order:
        next_order = []
        for i, row in enumerate(line):
            new_row = ""
            for j, seat in enumerate(row):
                count_occupied = 0
                for hor in range(-1, 2):
                    for ver in range(-1, 2):
                        if hor != 0 or ver != 0:
                            if 0 <= i+hor < len(line) and 0 <= j+ver < len(row) and line[i+hor][j+ver] == "#":
                                count_occupied += 1
                assert 0 <= count_occupied < 9, count_occupied
                if seat == "L" and count_occupied == 0:
                    new_row = new_row + "#"
                elif seat == "#" and count_occupied >= 4:
                    new_row = new_row + "L"
                else:
                    new_row = new_row + seat
            next_order.append(new_row)
        prev_order = deepcopy(line)
        line = deepcopy(next_order)

    count_all = 0
    for p in line:
        for r in p:
            if r == "#":
                count_all += 1
    return count_all


def main():
    line = []
    try:
        while True:
            alles = input()
            line.append(alles)
    except EOFError:
        pass
    result = best_result(line)
    print("Result is: {}".format(result))


if __name__ == "__main__":
    main()