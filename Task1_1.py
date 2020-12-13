def best_result(line):
    line.sort()
    reverse_line = sorted(line, reverse=True)

    for i in line:
        if 2020 - i in reverse_line:
            return  i*(2020-i)

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