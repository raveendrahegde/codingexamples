import argparse
import re
import json

class Processor(object):
    def __init__(self, infile, outfile):
        self.infile = infile
        self.outfile = outfile
        self.entries = []
        self.errors = []

    def readinput(self):
        """
        Reads self.infile and tries to match each line using regex. If match found, process that line.
        Accuracy of the program is dependent on how well the regex can be tuned
        """
        try:
            print "Reading the input file {}".format(self.infile)

            with open(self.infile) as f:
                for linenum, line in enumerate(f):
                    if re.match(r'[A-Za-z.\s]+,\s[A-Za-z.\s]+,\s\(\d{3}\)-\d{3}-\d{4},\s\w+,\s\d{5}', line):
                        self.__processFormat1(line.strip())
                    elif re.match(r'[A-Za-z.\s]+\s[A-Za-z.\s]+,\s\w+,\s\d{5},\s\d{3}\s\d{3}\s\d{4}', line):
                        self.__processFormat2(line.strip())
                    elif re.match(r'[A-Za-z.\s]+,\s[A-Za-z.\s]+,\s\d{5},\s\d{3}\s\d{3}\s\d{4},\s\w+', line):
                        self.__processFormat3(line.strip())
                    else:
                        self.errors.append(linenum+1)
        except Exception as e:
            print "Failed to finish reading the file - err: " + str(e)

    def writeoutput(self):
        """Write the data structure to self.outfile after converting to JSON"""
        self.entries = sorted(self.entries, key=lambda x: (x['lastname'], x['firstname'])) #Entries needed to be sorted based on the name
        with open(self.outfile, 'w') as f:
            f.write(json.dumps({'entries':self.entries, 'errors':self.errors}, indent=2, separators=(',', ': ')))

        print "Output written to the file {}".format(self.outfile)

    def __processFormat1(self, line):
        """Line format: Lastname, Firstname, (703)-742-0996, Blue, 10013"""
        try:
            l = line.split(', ')
            d = {
                "lastname": l[0],
                "firstname": l[1],
                "phonenumber": l[2],
                "zipcode": l[4],
                "color": l[3],
                }
        except Exception as e:
            print "Failed to parse the line - {} - err:{}".format(line, e)
        
        self.entries.append(d)

    def __processFormat2(self, line):
        """Line format: Firstname Lastname, Red, 11237, 703 955 0373"""
        try:
            l = line.split(', ')
            name = l[0].split(' ')
            phone = l[3].split(' ')

            d = {
                "lastname": name[0],
                "firstname": name[1],
                "phonenumber": "({})-{}-{}".format(phone[0], phone[1], phone[2]),
                "zipcode": l[2],
                "color": l[1],
                }
        except Exception as e:
            print "Failed to parse the line - {} - err:{}".format(line, e)
        
        self.entries.append(d)

    def __processFormat3(self, line):
        """Line format: Firstname, Lastname, 10013, 646 111 0101, Green"""
        try:
            l = line.split(', ')
            phone = l[3].split(' ')

            d = {
                "lastname": l[1],
                "firstname": l[0],
                "phonenumber": "({})-{}-{}".format(phone[0], phone[1], phone[2]),
                "zipcode": l[2],
                "color": l[4],
                }
        except Exception as e:
            print "Failed to parse the line - {} - err:{}".format(line, e)

        self.entries.append(d)

if __name__ == '__main__':
    """Input and output files can be sent as command line argument. Brings flexibility"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--in', default='./data.in', type=str, dest='infile')
    parser.add_argument('--out', default='./result.out', type=str, dest='outfile')
    args = parser.parse_args()

    infile = args.infile
    outfile = args.outfile

    p = Processor(infile, outfile)
    p.readinput()
    p.writeoutput()




