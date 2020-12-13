import re

def dfs(line, bags_to_search, multi, suma):
    """
    :param line: dictionary mapping bag color to its contents
    :param bags_to_search: list containing tuples (number of bags, color)
    :param multi: number of outer bags
    :return: number of inner bags
    """
    for bag in bags_to_search:
        num_bag = int(bag[0])
        col_bag = bag[1]
        if not line[col_bag]:
            suma += multi * num_bag
        else:
            print("Searching contents of:", col_bag, line[col_bag], "with multiplier of", multi*num_bag, "current sum is", multi * num_bag)
            suma += dfs(line, line[col_bag], multi * num_bag, multi * num_bag)
    return suma

def best_result(line):
    bags_to_search = [('1', 'shiny gold')]

    answer = dfs(line, bags_to_search, 1, 0) - 1

    return answer


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