from collections import deque

def best_result(line):

    target = 15690279
    num_list = deque()

    for nu in line:
        if sum(num_list) == target:
            return min(num_list) + max(num_list)
        if sum(num_list) < target:
            num_list.append(nu)
        while sum(num_list) > target:
            num_list.popleft()

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