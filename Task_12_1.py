def best_result(line):
    general_direction = "E"
    coo_v = 0 #Coordinates south - north
    coo_h = 0 #Coordinates west - east
    move_d = {"N" : 0, "E": 1, "S": 2, "W": 3}
    move_de = {0: "N", 1: "E", 2: "S", 3: "W"}

    for move in line:
        m_h = 0  # Moves south - north
        m_v = 0  # Moves west - east
        d, number = move
        if d == "L":
            g_d_num = move_d[general_direction]
            g_d_num -= number // 90
            g_d_num = g_d_num % 4
            general_direction = move_de[g_d_num]
        if d == "R":
            g_d_num = move_d[general_direction]
            g_d_num += number // 90
            g_d_num = g_d_num % 4
            general_direction = move_de[g_d_num]
        if d == "F":
            d = general_direction
        if d == "W":
            m_h = -number
        if d == "E":
            m_h = number
        if d == "S":
            m_v = -number
        if d == "N":
            m_v = number
        coo_v += m_v
        coo_h += m_h

    print(coo_v, coo_h, general_direction)

    return abs(coo_h) + abs(coo_v)


def main():
    line = []
    try:
        while True:
            alles = input()
            line.append((alles[0], int(alles[1:])))
    except EOFError:
        pass
    result = best_result(line)
    print("Result is: {}".format(result))


if __name__ == "__main__":
    main()