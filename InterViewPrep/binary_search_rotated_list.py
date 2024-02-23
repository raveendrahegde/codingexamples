def rotSearch(nums, needed):
	leastnumindex=0
	for i in range(len(nums)-1):
		if nums[i] > nums[i+1]:
			leastnumindex=i+1
			break
		elif nums[i] == needed:
			return True

	return BiSearch(nums[leastnumindex:]+nums[:leastnumindex], needed)

def BiSearch(nums, needed):
	if needed < nums[0] or needed > nums[-1]:
		print "Out of range"
		return False
	if len(nums) == 1:
		if nums[0] == needed:
			return True
		else: 
			return False
	elif len(nums) == 0:
		return None
	else:
		mid=len(nums)/2
		if nums[mid] == needed:
			return True
		elif nums[mid] > needed:
			return BiSearch(nums[:mid], needed)
		else:
			return BiSearch(nums[mid:], needed)	

if __name__ == '__main__':
	inputlist=input('Enter List:')
	find=input('Enter number to find:')

	print rotSearch(inputlist, find)