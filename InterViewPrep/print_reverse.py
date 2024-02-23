f='access_log.2014.07.15'
tells=[]
with open(f) as fh:
	while True:
		tells.append(fh.tell())
		line = fh.readline()
		if not line:
			break
	tells.reverse()

with open(f) as fh:
	for pos in tells:
		fh.seek(pos)
		line = fh.readline()
		print line,


