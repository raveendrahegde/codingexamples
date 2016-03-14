#__Author__ Raveendra Hegde (raveendra.h@gmail.com)

import threading
import time
import os
import re
import logging
import json

logging.basicConfig(filename='logparse.log', level=logging.DEBUG)
logger = logging.getLogger(__name__)

mydata = []


class MaxHeap(object):
	def __init__(self, items):
		self.heap = []

		for i in items:
			self.heap.append(i)
			self.__bubbleUp(len(self.heap) - 1)


	def __bubbleUp(self, index):
		if index == 0:
			return
		else:
			parentIndex = index/2
			if self.heap[parentIndex]["count"] < self.heap[index]["count"]:
				self.heap[parentIndex], self.heap[index] = self.heap[index], self.heap[parentIndex]
				self.__bubbleUp(parentIndex) #Need to bubble up recursively
			else:
				return
	
	def __bubbleDown(self, index):
		if index == len(self.heap) - 1:
			return
		else:
			leftChildIndex = 2*index
			rightChildIndex = 2*index + 1

			hasLeftChild = self.__hasLeftChild(leftChildIndex)
			hasRightChild = self.__hasRightChild(rightChildIndex)
			
			if hasLeftChild and hasRightChild:
				leftCount = self.heap[leftChildIndex]["count"]
				rightCount = self.heap[rightChildIndex]["count"]

				if leftCount >= rightCount:
					if self.heap[index]["count"] < self.heap[leftChildIndex]["count"]:
						self.heap[index], self.heap[leftChildIndex] = self.heap[leftChildIndex], self.heap[index]
						self.__bubbleDown(leftChildIndex)
				elif leftCount < rightCount:
					if self.heap[index]["count"] < self.heap[rightChildIndex]["count"]:
						self.heap[index], self.heap[rightChildIndex] = self.heap[rightChildIndex], self.heap[index]
						self.__bubbleDown(rightChildIndex)

			elif hasLeftChild and not hasRightChild:
				leftCount = self.heap[leftChildIndex]["count"]
				if self.heap[index]["count"] < self.heap[leftChildIndex]["count"]:
					self.heap[index], self.heap[leftChildIndex] = self.heap[leftChildIndex], self.heap[index]
			else:
				return

	def push(self, item):
		self.heap.append(item)
		self.__bubbleUp(len(self.heap) - 1)

	def popMax(self):
		"""Remove top value, move last child to top and bubble down"""
		if len(self.heap) == 1:
			maxv = self.heap.pop(0)
			return maxv
		elif len(self.heap) > 1:
			maxv = self.heap.pop(0) #Remove the first element
			last = self.heap.pop()
			self.heap.insert(0, last)
			self.__bubbleDown(0)
			return maxv
		else:
			return None

	def __hasLeftChild(self, leftChildIndex):
		hasLeftChild = True
		if leftChildIndex > (len(self.heap) -1):
			hasLeftChild = False

		return hasLeftChild

	def __hasRightChild(self, rightChildIndex):
		hasRightChild = True
		if rightChildIndex > (len(self.heap) -1):
			hasRightChild =  False

		return hasRightChild


class ReadFile(threading.Thread):
	"""Reads a given file to look for log lines based on regex. Runs on its own thread"""
	def __init__(self, filename):
		super(ReadFile, self).__init__()
		self.filename = filename
		self.data = {
			'filename' : self.filename,
			'INFO': [],
			'ERROR': [],
			'WARNING': [],
			'FATAL': [],
			'DEBUG': [],
			}

		self.loglevels = ["ERROR", "INFO", "WARNING", "FATAL", "DEBUG"]
		
	def run(self):
		self.readFile()

	def readFile(self):
		logger.info("Reading file - " + self.filename)
		fhandle = open(self.filename)
		
		for line in fhandle:
			try:
				line = line.strip('\n')
				if re.match('.+ - DEBUG -', line):
					splitline = line.split('- DEBUG -')
					content = splitline[1]
					self.addInfo('DEBUG', content)

				elif re.match('.+ - ERROR -', line):
					splitline = line.split('- ERROR -')
					content = splitline[1]
					self.addInfo('ERROR', content)

				elif re.match('.+ - WARNING -', line):
					splitline = line.split('- WARNING -')
					content = splitline[1]
					self.addInfo('WARNING', content)

				elif re.match('.+ - FATAL -', line):
					splitline = line.split('- FATAL -')
					content = splitline[1]
					self.addInfo('FATAL', content)

				elif re.match('.+ - INFO -', line):
					splitline = line.split('- INFO -')
					content = splitline[1]
					self.addInfo('INFO', content)
			except Exception as e:
				logger.error("Error processing log line " + str(line))

		self.heapify()

	def addInfo(self, level, info):
		"""Increase count or add count/logline to the data structure"""
		leveldata = self.data.get(level, None)
		if leveldata is None:
			return

		if len(leveldata) > 0:
			index = 0
			found = False
			
			for content in leveldata:
				existing = content.get("loginfo", None)
				if existing == info:
					self.data[level][index]["count"] = self.data[level][index]["count"] + 1
					found = True
				index += 1
			
			if not found:
				leveldata.append({"count":1, "loginfo": info})
				
		else:
			leveldata.append({"count":1, "loginfo": info})

	def heapify(self):
		for level in self.loglevels:
			mheap = MaxHeap(self.data[level])
			self.data[level] = mheap #Attach the heap object
		mydata.append(self.data) #Append to global list to retain data


class ReadDir(threading.Thread):
	"""Reads a given directory to look for log files on a thread. Filenames appened to a list"""
	def __init__(self, dirname):
		super(ReadDir, self).__init__()
		self.dirname = dirname
		self.logfiles = []

	def run(self):
		self.readDir()

	def readDir(self):
		try:
			files = os.listdir(self.dirname)
		except OSError as e:
			logger.error("Unable to read directory " + self.dirname)
			return

		for file in files:
			if file.endswith('.log'):
				logger.info("Logfile found - " + file)
				self.logfiles.append(self.dirname + "/" + file)


def printData():
	"""Prints the final data in required format"""
	for filedata in mydata:
		print "--For file %s --\n" %filedata["filename"]
		for level, heap in filedata.iteritems():
			if level == "filename":
				continue
			else:
				totalLines = getTotal(heap.heap)
				if totalLines:
					print level + " lines"
					print str(totalLines) + " Total lines"

					if len(heap.heap) <= 5:
						count = len(heap.heap)
					else:
						count = 5

					for count in range(0,count):
						top = heap.popMax()
						print "%d. %s - %d instance" %(count+1, top["loginfo"], top["count"])
					print "\n"

def getTotal(alist):
	count = 0
	if not alist:
		return 0

	for a in alist:
		count += a["count"]

	return count

if __name__ == '__main__':
	dirs = ['logdir', 'logdir2'] #To fecilitate multiple log directories
	logfiles = []
	threads_dir = []
	threads_file = []
	
	for d in dirs:
		read = ReadDir(d)
		logger.info("Thread %s started for %s" %(read, d))
		threads_dir.append(read)
		read.start()
		read.join()
		logfiles = logfiles + read.logfiles

	for f in logfiles:
		loginfo = ReadFile(f)
		logger.info("Thread %s started for %s" %(loginfo, f))
		threads_file.append(loginfo)
		loginfo.start()


	while threads_file: #Wait till all threads gather their data
		for fthread in threads_file:
			if not fthread.isAlive():
				threads_file.remove(fthread)

	printData()

"""
The program scans the directories given in the list `dirs` and looks for the files which end with `.log` assuming thats what we are looking for.
Reading directories is not necessarily run on different threads, but done so for future requirements if any. 
Reading of the files is usuful to run on threads because it's a time consuming operation. 
The files are read line by line and the regex matched lines are used to construct a data structure which is a dictionary with log levels as keys and list of dictionaries as values.
The maps inside the list contain any distinct log line, and how may times we have seen it. Then those list are converted to max heap(based on the count) and top 5 lines are printed using printData function.
It is possible to further improve the performance by constructing the max heap itself during log reading itself than converting to max heap after the log reading has been completed. 
I chose not to implement in that way because its log reading which is more time time intensive than converting the max heap.

It is assumed that log directories are present current directory.

The data structure, after converting to max heap looks like below:

{  
   "INFO":[  
      {  
         "count":83583,
         "loginfo":" Log line content A"
      },
      {  
         "count":5302,
         "loginfo":" Log line content Z"
      },
      {  
         "count":2442,
         "loginfo":" Log line content X"
      },
   ],
   "filename":"logdir/example1.log",
   "WARNING":[  
      {  
         "count":63052,
         "loginfo":" Log line content C"
      }
   ],
   "ERROR":[  
      {  
         "count":31174,
         "loginfo":" Log line content B"
      },
      {  
         "count":2651,
         "loginfo":" Log line content Z"
      }
   ],
   "DEBUG":[  

   ],
   "FATAL":[  
      {  
         "count":93863,
         "loginfo":" Log line content D"
      }
   ]
}
"""

"""
---Ways to test the script---
1. Create directories and logfiles and add directories to `dirs` list
2. Add empty log files to log directories
3. Add log files which has log line which are not in expected format
4. Add log lines which have no content after the log level
5. Add log files with same name in different log directories
6. Performance testing by adding multiple directories wich higher number of log files
7. Performance testing by adding log files with higher number of log lines
8. Remove log file/directory while its in processing
9. Add a non existing log directory to scan
10. Run the script and check for data mismatch
"""

