def best_result(line, time_stamp):

    bus_found = False
    wait_time = 0
    while not bus_found:
        for b in line:
            if time_stamp % b == 0:
                print(wait_time, b)
                return wait_time * b
        wait_time += 1
        time_stamp += 1

def main():
    line = []
    time_stamp = int(input())
    buses = input().split(",")
    for b in buses:
        if b == "x":
            pass
        else:
            line.append(int(b))
    result = best_result(line, time_stamp)
    print("Result is: {}".format(result))


if __name__ == "__main__":
    main()