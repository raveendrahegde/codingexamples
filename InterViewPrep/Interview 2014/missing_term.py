N=5
APS=['1', '11', '31', '41', '51']
AP=map(int,APS)

first=AP[1]-AP[0]
last=AP[-1]-AP[-2]
if first > last:
    print (AP[0]+AP[1])/2
    exit()
elif last > first:
    print (AP[-1]+AP[-2])/2
    exit()
else:
    diff=first
    
for i in range(N-1):
    if (AP[i+1]-AP[i] != diff):
        print (AP[i+1]+AP[i])/2
        exit()
    

