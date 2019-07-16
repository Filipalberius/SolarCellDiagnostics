import os


# Reads a given file and creates an array containing all of the lines in the file.
from typing import List, Any


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
def find_identity_entries(data, identity):
    for i in range(len(data)):
        line = get_line(data, i)
        if identity == line[0]:
            return line
        else:
            i += 1

def return_data_with_dates(matrix, open_date, close_date):
    values = list()
    for x in matrix:
        if open_date <= x[2] <= close_date:
            values.append(x[2])
    return values


# prints the data on a given line
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


def main():
    data = read('produktionsdata.csv')
    #line = get_line(data, 26276)
    line = find_identity_entries(data, '734012530000043305')
    print_data(line)

    # identity = input("Enter cell's ID\n")
    # print(identity)


if __name__ == '__main__':
    main()
