def best_result(line):
    count_ways = 1
    prev = 0
    line.sort()
    line.append(line[-1] + 3)
    diff = []

    for el in line:
        diff.append(el-prev)
        prev = el

    count_1 = 0
    for e in diff:
        if e == 1:
            count_1 += 1
        else:
            if count_1 == 2:
                count_ways *= 2
            if count_1 == 3:
                count_ways *= 4
            if count_1 == 4:
                count_ways *= 7
            count_1 = 0

    return count_ways


def main():
    line = []
    try:
        while True:
            alles = int(input())
            line.append(alles)
    except EOFError:
        pass
    result = best_result(line)
    print("Result is: {}".format(result))


if __name__ == "__main__":
    main()