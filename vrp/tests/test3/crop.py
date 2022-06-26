
def parse_graph():
    try:
        f = open("vertex_weigths.csv")
        output = ""
        lines = f.readlines()
        for line in lines:
            print(line)
            elements = line.split(",")
            x = int(elements[0])
            y = int(elements[1])
            weight = float(elements[2])
            print("hjello")
            print(x, y)
            if (x <= 20 and y <= 20):
                output += f"{x},{y},{weight}\n"
                output += f"{y},{x},{weight}\n"
        f.close()

        f = open("output.csv", "w")
        f.seek(0)
        f.write(output)
        f.truncate()

        f.close()
    except:
        return None


parse_graph()
