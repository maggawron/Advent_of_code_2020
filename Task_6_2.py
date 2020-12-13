import string

def best_result(line):
    result = 0
    for item in line:
        people_c, memory = item
        assert people_c != 0
        for i in memory:
            if i == people_c:
                result += 1

    return result


def main():
    people_count = 0
    line = []
    memory = [0] * 26
    try:
        while True:
            string_i = input()
            if string_i == "":
                line.append((people_count, memory))
                memory = [0] * 26
                people_count = 0
            else:
                people_count += 1
                el = list(string_i)
                for n in el:
                    i = string.ascii_lowercase.index(n)
                    memory[i] += 1
    except EOFError:
        pass
    result = best_result(line)
    print("Result is: {}".format(result))

if __name__ == "__main__":
    main()