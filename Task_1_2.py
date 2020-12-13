def best_result(line):
    line.sort()

    for a_i, number in enumerate(line):
        b_i = a_i + 1
        while line[a_i] + line[b_i] < 2020 and b_i < 200:
            if 2020 - line[a_i] - line[b_i] in line:
                return (2020 - line[a_i] - line[b_i]) * line[a_i] * line[b_i]
            else:
                b_i += 1

def main():
    line = []
    try:
        while True:
            number = int(input()) #number
            line.append(number)
    except EOFError:
        pass
    result = best_result(line)
    print("Result is: {}".format(result))

if __name__ == "__main__":
    main()