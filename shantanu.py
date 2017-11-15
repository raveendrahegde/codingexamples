import csv
import re
import time

oneday = re.compile(r'(\w{3}) (\d{1,2}:\d{1,2} am|pm) - (\d{1,2}:\d{1,2} am|pm)')
multiday = re.compile(r'(\w{3}-\w{3}) (\d{1,2}:\d{1,2} am|pm) - (\d{1,2}:\d{1,2} am|pm)')

def readFile(filename):
    data = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            data[row[0]] = {'raw': row[1]}
    return data


def parseAvail(data):
    for k, v in data.items():
        v['proc'] = getAvail(v['raw'])

    print(data)


def getAvail(dateshit):
    structured = []
    for item in dateshit.split(','):
        if oneday.match(item):
            groups = oneday.findall(item)[0]
            starts = "{} {}".format(groups[0], groups[1])
            ends = "{} {}".format(groups[0], groups[2])

            start = time.strptime(starts, "%a %I:%M %p")
            end = time.strptime(ends, "%a %I:%M %p")
            structured.append((start, end))
        elif multiday.match(item):
            groups = multiday.findall(item)[0]
            days = groups[0].split('-')

            starts = "{} {}".format(days[0], groups[1])
            ends = "{} {}".format(days[1], groups[2])

            start = time.strptime(starts, "%a %I:%M %p")
            end = time.strptime(ends, "%a %I:%M %p")
            structured.append((start, end))
    return structured


if __name__ == '__main__':
    file = '/Users/ravee/Downloads/sdr_availability.csv'
    data = readFile(file)
    pdata = parseAvail(data)
    # dateinput = input("Enter Day and Time:")
