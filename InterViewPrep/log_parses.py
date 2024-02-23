logfile='access_log.2014.07.13'
import json

class LogFileRead():
	logDetails = {}
	def __init__(self, file):
		self.file = file

	def createDict(self):
		fh = open(self.file)

		for line in fh:
			lineparts = line.split()
			page = lineparts[6]
			ip = lineparts[0]
			datetime = lineparts[3]
			date = datetime.strip('[').split(':')[0]

			if self.logDetails.has_key(page):
				self.logDetails[page]['count'] += 1
				if ip not in self.logDetails[page]['ips']:
					self.logDetails[page]['ips'].append(ip)
				if date not in self.logDetails[page]['dates']:
					self.logDetails[page]['dates'].append(date)
			else:
				self.logDetails[page] = {'count': 1,
										'ips':[ip],
										'dates':[date]}


if __name__ == '__main__':
  	r = LogFileRead(logfile)
  	r.createDict()
  	r.logDetails

  	for page, details in r.logDetails.iteritems():
  		if 'api' in page:
	  		print "PAGE - " + page + " COUNT - " + str(details['count'])
	  		print "DATES - " + ",".join(details['dates']) + " IPs - " + ",".join(details['ips'])

