

def join_comma_word(line):
	incommaword=False
	joined=''
	newjoinedline=[]
	for word in line:
		if word.startswith('"'):
			incommaword=True
			joined=''
			joined = joined + word.split('"')[1]
			continue
		if word.endswith('"'):
			incommaword=False
			joined = joined + ',' + word.rstrip('"')
			newjoinedline.append(joined)
			continue
		if incommaword:
			joined = joined + ',' + word
		else:
			newjoinedline.append(word)
	return newjoinedline

def read_csv():
	csvfile='csvfile.csv'
	f=open(csvfile, 'r')
	final=[]
	for line in f:
		line_list=line.split(',')
		repaired=join_comma_word(line_list)
		final.append(repaired)
	print final

if __name__ == '__main__':
	read_csv()

