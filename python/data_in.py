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


# Returns the line of a specific index in the data array.
def get_line(data, index):
    return data[index].split(';')


# Searches the data array for an entry with a specific identity.
def find_identity(data, identity):

    entries = list()

    for i in range(len(data)):
        line = get_line(data, i)
        if identity == line[0]:
            entries.append(line)
        else:
            i += 1

    return entries


# Returns all entries in the specified date interval.
def entries_by_date(entries, first_date, last_date):
    return [entry for entry in entries if first_date <= int(entry[2]) <= last_date]


# Prints the data on a given line.
def print_data(line):
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


def dialogue():
    print('Hello and welcome to Samuel and Filips awesome Solar Cell Programme!\n')
    identity = input('What solar cell do you want to examine?\n')
    start = int(input('From what date? (YYYYMMDDhhmm)\n'))
    end = int(input('Until what date? (YYYYMMDDhhmm)\n'))
    return identity, start, end


def main():
    data = read('produktionsdata.csv')
    identity, start, end = dialogue()
    entries = find_identity(data, identity)
    date_entries = entries_by_date(entries, start, end)
    print_data(date_entries[10])

    # id = 734012530000000438
    # start = 201701010000
    # end = 201702040000


if __name__ == '__main__':
    main()
