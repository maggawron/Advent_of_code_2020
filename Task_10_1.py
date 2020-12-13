def best_result(line):

    prev = 0
    count_1 = 0
    count_3 = 0
    line.sort()
    line.append(line[-1] + 3)

    
    for el in line:
        if el-prev == 1:
            count_1 += 1
        if el-prev == 3:
            count_3 += 1
        prev = el

    return count_1 * count_3


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