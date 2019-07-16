import os


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


def get_line(data, index):
    if index > len(data):
        print('derp')
    return data[index].split(';')


def find_identity(data, identity):
    i = 0
    while True:
        line = get_line(data, i)
        if identity == line[0]:
            return line
        else:
            i += 1


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
    line = get_line(data, 26276)
    #line = find_identity(data, '734012530000043305')
    print_data(line)

    # identity = input("Enter cell's ID\n")
    # print(identity)


if __name__ == '__main__':
    main()
