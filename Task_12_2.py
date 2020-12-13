def best_result(line):
    way_point = (1, 10) #north - south, east - west
    coo_v = 0 #Coordinates south - north
    coo_h = 0 #Coordinates west - east

    for move in line:
        m_h = 0  # Moves south - north
        m_v = 0  # Moves west - east
        d, number = move
        if d == "L" or d == "R":
            if number == 0:
                pass
            if number == 270:
                d = "L" if d == "R" else "R"
                number = 90
            if number == 180:
                way_point = (-way_point[0], -way_point[1])
            if number == 90 and d == "L":
                way_point = (way_point[1], -way_point[0])
            if number == 90 and d == "R":
                way_point = (-way_point[1], way_point[0])
        if d == "F":
            m_h = number * way_point[0]
            m_v = number * way_point[1]
        if d == "W":
            way_point = (way_point[0], way_point[1] - number)
        if d == "E":
            way_point = (way_point[0], way_point[1] + number)
        if d == "S":
            way_point = (way_point[0] - number, way_point[1])
        if d == "N":
            way_point = (way_point[0] + number, way_point[1])
        coo_v += m_v
        coo_h += m_h

    print(coo_v, coo_h, way_point)

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