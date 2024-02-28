def sum_is_zero(pnlist):
	plist = pnlist[0]
	nlist = pnlist[1]

	pdict = add_two_nums(plist)
	ndict = add_two_nums(nlist)

	for pnum in plist:
		for nkey, nval in ndict.items():
			if pnum + nval == 0:
				print(pnum, nkey)

	for nnum in nlist:
		for pkey, pval in pdict.items():
			if nnum + pval == 0:
				print(nnum, pkey)


def add_two_nums(anylist):
	mydict = {}
	for i in range(len(anylist)):
		j = i+1
		while j < len(anylist):
			key = str(anylist[i]) + "+" + str(anylist[j])
			mydict[key] = anylist[i] + anylist[j]
			j+=1
	return mydict

def separate_list(inputlist):
	nlist=[]
	plist=[]
	for i in range(len(inputlist)):
		if inputlist[i] < 0:
			nlist.append(inputlist[i])
		else:
			plist.append(inputlist[i])
	return [plist, nlist]

if __name__ == '__main__':
	'''Problem definition: Given a list of integers, output all subsets of size three, which sum to zero'''
	inputlist=[-1, 0, 1, 2, -1, -4]
	sum_is_zero(separate_list(inputlist))

