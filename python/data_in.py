import os


# Reads a given file and creates an array containing all of the lines in the file.
def read(path):
    if os.path.exists(path):
        with open(path) as file:
            try:
                return file.readlines()
            except IOError:
                print("Could not find file")
            finally:
                file.close()
    else:
        print('File does not exist')
        exit()


# Prints the data on a given line.
def data_toarray(line):

    values = list()
    data = line[10:]

    i = 0
    for value in data:
        if i % 2 == 0:
            values.append(value)
        i += 1

    return_string = "[";

    for number in values:
        return_string += (number + ";")
    return_string = return_string[:-1]
    return_string += "]"
    print(return_string)


# Finds the interval of entries containing the correct identity and dates.
def get_data(file, identity, open_date, close_date):
    data = read(file)
    entries = list()
    for line in data:
        entry = line.split(';')
        if entry[0] == identity:
            if open_date <= int(entry[2]) <= close_date:
                entries.append(entry)
    return entries


# Prompts a dialogue in the terminal asking user for correct parameters.
def dialogue():
    print('Hello and welcome to Samuel and Filips awesome Solar Cell Programme!\n')
    identity = input('What solar cell do you want to examine?\n')
    start = int(input('From what date? (YYYYMMDDhhmm)\n'))
    end = int(input('Until what date? (YYYYMMDDhhmm)\n'))
    return identity, start, end


def print_data(entries):
    for entry in entries:
        data_toarray(entry)


def main():
    identity, start, end = "734012530000024571", 201811290000, 201812220000
    entries = get_data('produktionsdata.csv', identity, start, end)
    print_data(entries)


if __name__ == '__main__':
    main()
