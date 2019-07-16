def initialize():
    return open('produktionsdata.csv').readlines()


def get_line(data, index):
    return data[index].split(';')


def find_identity(data, identity):



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
    data = initialize()
    test_line = get_line(data, 0)
    print_data(test_line)
    identity = input("Enter cell's ID\n")
    print(identity)


if __name__ == '__main__':
    main()