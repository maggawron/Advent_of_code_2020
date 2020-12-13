import string

def best_result(line):
    result = 0
    search = {"byr": [1920, 2002], "iyr": [2010, 2020],
              "eyr": [2020, 2030], "hgt": [150, 193, 59, 76], "ecl": ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"], "hcl":[], "pid":[]}
    for passport in line:
        search_map = set()
        for item in passport:
            it = item[0]
            value = item[1]
            if it == "byr" or it == "iyr" or it == "eyr" and search[it][0] <= int(value) <= search[it][1]:
                search_map.add(it)
            elif it == "hgt":
                if value[-1] == "m" and value[:3].isdigit():
                    if search[it][0] <= int(value[:3]) <= search[it][1]:
                        search_map.add(it)
                if value[-1] == "n" and value[:2].isdigit():
                    if search[it][2] <= int(value[:2]) <= search[it][3]:
                        search_map.add(it)
            elif it == "hcl":
                validate = 0
                for j, letter in enumerate(value):
                    if j == 0 and letter == "#":
                        validate += 1
                    if j >= 1 and letter.islower() or letter.isdigit():
                        if letter.islower():
                            letter_code = string.ascii_letters.index(letter)
                            if 0 <= letter_code <= 5:
                                validate += 1
                        if letter.isdigit():
                            validate += 1
                if len(value) == 7:
                    validate += 1
                if validate == 8:
                    search_map.add(it)
            elif it == "ecl":
                if value in set(search[it]):
                    search_map.add(it)
            elif it == "pid" and len(value) == 9:
                search_map.add(it)
        if len(search_map) == len(search):
            result += 1

    return result


def main():
    line = []
    memory = []
    try:
        while True:
            string = input()
            if string == "":
                line.append(memory)
                memory = []
            else:
                el = string.split(" ")
                for e in el:
                    n = e.split(":")
                    memory.append(n)
    except EOFError:
        pass
    result = best_result(line)
    print("Result is: {}".format(result))

if __name__ == "__main__":
    main()