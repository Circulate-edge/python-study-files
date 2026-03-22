with open("poem_libai.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line[0] == "#":
            continue
        print(line.strip())