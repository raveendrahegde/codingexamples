# Q: Parse sample.log file and find the top 10 IPs (clients) for each hour of a particular day.

from collections import defaultdict
import re

structure = defaultdict(lambda: defaultdict(lambda: defaultdict(int)))

def parseLine(line):
  pattern = re.compile(r"(\d{1,2}/\d{1,2})\s(\d{1,2}:\d{1,2}:\d{1,2}).*\s(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})")
  result = pattern.search(line)
  # print(result)
  if result:
    (date, hour, IP) =  result.groups()
    hour = hour.split(':')[0]
    structure[date][hour][IP] += 1

def readFile(file):
  with open(file, 'r') as fh:
    for line in fh:
      parseLine(line)

def findTop(date, hour):
  sorted_ips = sorted(structure[date][hour].items(), key=lambda x: x[1], reverse=True)[:10]
  if sorted_ips:
    for ip, count in sorted_ips:
        print(f"{ip} - {count}")
  else:
    print("No calls during this time")

if __name__ == "__main__":
  file = "/Users/raveendrahegde/Projects/codingexamples/InterViewPrep/Interview2024/sample.log"
  readFile(file)
  findTop('03/22', '08')


