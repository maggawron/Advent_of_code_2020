def best_result(line):
    wynik = 0
    for item in line:
        rang, letter, strin = item
        min_n, max_n = rang.split("-")
        letter = letter[0]
        count = 0
        for l in strin:
            if l == letter:
                count += 1
        if count >= int(min_n) and count <= int(max_n):
            wynik += 1
    return wynik


def main():
    line = []
    try:
        while True:
            all = input().split(" ")
            line.append(all)
    except EOFError:
        pass
    result = best_result(line)
    print("Result is: {}".format(result))

if __name__ == "__main__":
    main()