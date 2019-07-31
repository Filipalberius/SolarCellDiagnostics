import os
import plotly.graph_objects as go


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
def get_values(line):

    values = list()
    data = line[10:]

    i = 0
    for value in data:
        if i % 2 == 0:
            values.append(value)
        i += 1

    for i in range(len(values)):
        values[i] = float(values[i].replace(',', '.'))
    return values


# Finds the interval of entries containing the correct identity and dates.
def get_data(file, identity, start_date, end_date):
    data = read(file)
    entries = list()

    for line in data:
        entry = line.split(';')
        entry_id, date = entry[0], int(entry[2])

        if entry_id == identity and start_date <= date <= end_date:
            entries.append(entry)

    return entries


# Prompts a dialogue in the terminal asking user for correct parameters.
def dialogue():
    print('Hello and welcome to Samuel and Filips awesome Solar Cell Programme!\n')
    identity = input('What solar cell do you want to examine?\n')
    start = int(input('From what date? (YYYYMMDDhhmm)\n'))
    end = int(input('Until what date? (YYYYMMDDhhmm)\n'))
    return identity, start, end


def short_data(entries):
    values = list()
    for e in entries:
        values.append(get_values(e))
    return values


def make_graph_stacked(data):
    fig = go.Figure()
    i = 0
    for d in data:
        fig.add_trace(go.Scatter(y=d,
                                 mode='lines+markers',
                                 name='day' + str(i + 1)))
        i += 1

    fig.update_layout(title='Production per hour per day for the specified unit and date interval.',
                      xaxis_title='Hour',
                      yaxis_title='Production (KWH)')

    fig.write_html('data.html', auto_open=True)


def make_graph(data):
    fig = go.Figure()
    concat_data = list()
    for d in data:
        concat_data = concat_data + d

    fig.add_trace(go.Scatter(y=concat_data,
                             mode='lines+markers'))

    fig.update_layout(title='Production per hour per day for the specified unit and date interval.',
                      xaxis_title='Time',
                      yaxis_title='Production (KWH)')

    fig.write_html('data.html', auto_open=True)


def main():
    identity, start, end = '734012530000024571', 201811290000, 201812220000
    # identity, start, end = dialogue()
    entries = get_data('produktionsdata.csv', identity, start, end)

    make_graph(short_data(entries))


if __name__ == '__main__':
    main()
