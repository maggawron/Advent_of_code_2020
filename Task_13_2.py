def best_result(line):
    print(line)
    time_stamp = line[0][0]
    multiplier = line[0][0]
    checked = [1] + [0] * (len(line)-1)
    while True:
        for ind, it in enumerate(line):
            number, offset = it
            if (time_stamp + offset) % number == 0 and checked[ind] == 0:
                checked[ind] = 1
                multiplier *= line[ind][0]
        if sum(checked) == len(line):
            return time_stamp
        else:
            time_stamp += multiplier


def main():
    line = []
    time_stamp = int(input())
    buses = input().split(",")
    for ind, b in enumerate(buses):
        if b == "x":
            pass
        else:
            line.append((int(b), ind))
    result = best_result(line)
    print("Result is: {}".format(result))


if __name__ == "__main__":
    main()
