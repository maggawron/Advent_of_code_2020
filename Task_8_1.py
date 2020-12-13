import copy

def best_result(new_line):
    for index, j in enumerate(new_line):
        line = copy.deepcopy(new_line)
        if j[0] == "nop":
            line[index][0] = "jmp"
        if j[0] == "jmp":
            line[index][0] = "nop"

        i = 0
        current_sum = 0
        fine = True
        moves_log = [0] * len(line)

        while fine:
            if i >= len(line):
                fine = True
                break
            if moves_log[i] > 0:
                fine = False
                break
            instr = line[i][0]
            val = int(line[i][1])
            moves_log[i] = 1
            if instr == "jmp":
                i += val
            if instr == "nop":
                i += 1
            if instr == "acc":
                current_sum += val
                i += 1

        if fine is True:
            return current_sum

def main():
    line = []
    try:
        while True:
            strin = input()
            line.append(strin.split(" "))
    except EOFError:
        pass
    result = best_result(line)
    print("Result is: {}".format(result))

if __name__ == "__main__":
    main()