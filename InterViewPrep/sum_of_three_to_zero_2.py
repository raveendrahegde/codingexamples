# Q: Given a list of integers, output all subsets of size three, which sum to zero
# Algorithm: This program uses the two pointer approach after sorting the list. This is a simple and better approach compared to ../sum_of_three_to_zero.py

def find3sum(alist):
  triplets = []
  n = len(alist)
  alist.sort()

  for i in range(0, n-2):
    # Skip duplicates
    if i > 0 and alist[i] == alist[i - 1]:
        continue
        
    left = i + 1
    right = n - 1

    while left < right:
      sum = alist[left] + alist[i] + alist[right]

      if sum == 0:
        triplets.append([alist[left], alist[i], alist[right]])
        left += 1
        right -= 1
      elif sum < 0:
        left += 1
      else:
        right -= 1
      
  print(triplets)

if __name__ == '__main__':
	inputlist=[-1, 0, 1, 2, -1, -4]
	find3sum(inputlist)
