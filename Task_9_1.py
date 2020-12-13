def best_result(line):

    for ind, number in enumerate(line[25:]):
        options = line[ind:ind+25]
        options.sort()
        assert len(options) == 25
        found = False
        while not found:
            for n in options:
                if number - n in options[::-1]:
                    print(number, ind)
                    found = True
        if not found:
            return number

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