def get_line(index):
    file = open('produktionsdata.csv')

    return file.readlines()[index].split(';')


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
    line = get_line(0)
    print_data(line)


if __name__ == '__main__':
    main()