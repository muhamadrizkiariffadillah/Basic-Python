def populate_file(filename: str):
    values_to_write = [x for x in range(1, 10)]
    with open(filename, "w") as file:
        for value_to_write in values_to_write:
            file.write(str(value_to_write))
            file.write("\n")


def read_from_file(filename: str):
    data: list = []
    with open(filename, "r") as file:
        for line in file:
            # data.append(line)
            yield line
    return data


file_name = "Generators.txt"
populate_file(file_name)
file = read_from_file(file_name)
for x in file:
    print(x)
 