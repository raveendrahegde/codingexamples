import csv
import re
import time
import os

oneday = re.compile(r'(\w{3}) (\d{1,2}:\d{1,2}).(am|pm) - (\d{1,2}:\d{1,2}).(am|pm)')
multiday = re.compile(r'(\w{3}-\w{3}) (\d{1,2}:\d{1,2}).(am|pm) - (\d{1,2}:\d{1,2}).(am|pm)')


def readFile(filename):
    """ Read the CSV file with raw dates """
    data = {}
    with open(filename) as f:
        reader = csv.reader(f)
        for row in reader:
            data[row[0]] = {'raw': row[1]}
    return data


def parseAvail(data):
    for k, v in data.items():
        v['proc'] = getAvail(v['raw'])


def getAvail(dateshit):
    """ Convert raw available days to time object using re. Single and multiple days are considered
        [(start, end), (start, end)] is structured format
    """
    structured = []
    for item in dateshit.split(','):
        item = item.strip()
        if oneday.match(item):
            groups = oneday.findall(item)[0]
            starts = "{} {} {}".format(groups[0], groups[1], groups[2])
            ends = "{} {} {}".format(groups[0], groups[3], groups[4])

            start = time.strptime(starts, "%a %I:%M %p")
            end = time.strptime(ends, "%a %I:%M %p")
            structured.append((start, end))
        elif multiday.match(item):
            weekdays = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            groups = multiday.findall(item)[0]

            availrange = groups[0].split('-')
            availdays = weekdays[weekdays.index(availrange[0].strip()):weekdays.index(availrange[-1].strip()) + 1]

            for day in availdays:
                starts = "{} {} {}".format(day, groups[1], groups[2])
                ends = "{} {} {}".format(day, groups[3], groups[4])

                start = time.strptime(starts, "%a %I:%M %p")
                end = time.strptime(ends, "%a %I:%M %p")
                structured.append((start, end))
    return structured


def getSlot(dateinput):
    """ Read the user input slot and convert to time objects """
    slot = []
    inputf = dateinput.split('-')
    slot.extend([inputf[0][:3], inputf[0][3:].strip(), inputf[1].strip()])

    starts = "{} {}".format(slot[0], slot[1])
    ends = "{} {}".format(slot[0], slot[2])

    start = time.strptime(starts, "%a %I:%M %p")
    end = time.strptime(ends, "%a %I:%M %p")

    return start, end


def findAavail(pdata, dateinput):
    """ Loop through each reps formatted availability and look for match """
    slot = getSlot(dateinput)
    avail = []
    for k, v in pdata.items():
        for proc in v['proc']:
            if slot[0] >= proc[0] and slot[1] <= proc[1]:
                avail.append(k)
    return avail


if __name__ == '__main__':
    file = os.getenv('HOME') + '/Downloads/sdr_availability.csv'
    data = readFile(file)
    parseAvail(data)
    dateinput = input("Enter Day and Time Range (Ex: Mon 9:00 am - 10:30 pm):")
    reps = findAavail(data, dateinput.strip())
    print('Available Reps:', ', '.join(reps))
