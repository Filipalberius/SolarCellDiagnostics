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
def data_tostring(line):
    identity = line[0]
    date_format = line[1]
    date = line[2]
    q_code = line[3]
    period = line[4]
    unit = line[5]

    data = line[10:]

    print("Id: " + identity + ". Date: " + date)
    print("Production per hour:")

    i = 0
    a = 0
    for datum in data:
        if i % 2 == 0:
            print("Hour " + str(a) + ": " + datum + " " + unit)
            a += 1
        i += 1

def data_toarray(line):
    data_array = list()
    i = 0
    a = 0
    for value in line[10:]:
        if i % 2 == 0:
            list.append(value)
    return data_array


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


def main():
    identity, start, end = dialogue()
    entries = get_data('produktionsdata.csv', identity, start, end)
    data_tostring(entries[0])

    # id = 734012530000000438
    # start = 201701010000
    # end = 201702040000


if __name__ == '__main__':
    main()
