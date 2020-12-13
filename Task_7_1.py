import re

def best_result(line):
    target = "shiny gold"
    reversed_map = {}

    for key, val in line.items():
        for v in val:
            reversed_map.setdefault(v[1], []).append(key)

    new = set(reversed_map[target])
    solution = set(reversed_map[target])

    while len(new) != 0:
        new_new = set()
        for j in new:
            if j in reversed_map:
                potential = reversed_map[j]
                for it in potential:
                    if it not in solution:
                        new_new.add(it)
                        solution.add(it)
        new = new_new


    return len(solution)


def main():
    line = {}
    try:
        while True:
            strin = input()
            tupl = strin.split(" bags contain ")
            tupl[1] = re.findall("(\d+) (\D+) bag[s]{0,1}", tupl[1])
            line[tupl[0]] = tupl[1]
    except EOFError:
        pass
        result = best_result(line)
    print("Result is: {}".format(result))

if __name__ == "__main__":
    main()