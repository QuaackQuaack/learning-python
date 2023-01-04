while True:
    line = input(">")
    if line == "done":
        break
    elif line[0] == "#":
        continue
    print(line)
print("!DONE")

