def best_result(line):
    all_ids = []

    for seat in line:
        min_row = 0
        max_row = 127
        row_options = 128
        min_col = 0
        max_col = 7
        col_options = 8
        row_letters = seat[:7]
        col_letters = seat[7:]
        for i in range(7):
            row_options /= 2
            if row_letters[i] == "F":
                max_row = max_row - row_options
            if row_letters[i] == "B":
                min_row = min_row + row_options
        assert min_row == max_row
        for i in range(3):
            col_options /= 2
            if col_letters[i] == "L":
                max_col = max_col - col_options
            if col_letters[i] == "R":
                min_col = min_col + col_options
        assert min_col == max_col
        all_ids.append(min_row*8+min_col)
    all_ids.sort()
    first = all_ids[0]
    for id in all_ids[1:]:
        if id - first != 1:
            return id-1
        first = id

def main():
    line = []
    try:
        while True:
            string = input()
            line.append(string)
    except EOFError:
        pass
    result = best_result(line)
    print("Result is: {}".format(result))

if __name__ == "__main__":
    main()