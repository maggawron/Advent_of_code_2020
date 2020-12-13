def best_result(line):
    print(line)
    result = 0
    for set_item in line:
        result += len(set_item)

    return result


def main():
    line = []
    memory = []
    try:
        while True:
            string = input()
            if string == "":
                memory = set(memory)
                line.append(memory)
                memory = []
            else:
                el = list(string)
                memory = memory + el
    except EOFError:
        pass
    result = best_result(line)
    print("Result is: {}".format(result))

if __name__ == "__main__":
    main()