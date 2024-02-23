def readall(): # read the file in a dictionary
	details={}
	f='access_log.2014.07.13'
	fo=open(f, "r")
	for line in fo.readlines():
		time=line.split()[3]
		stime=time.strip('[]')
		if stime in details:
			details[stime]['count'] += 1 #update count if the same timestamp again
		else:
			details[stime]={'count':1, 'line':line} #create key with timestamp
	return details

if __name__ == "__main__":
	details=readall()
	for key, val in details.iteritems():
		print ":".join(key.split(':')[1:]) + " = " + str(val['count']) #print timestamp and count
		print val['line']
