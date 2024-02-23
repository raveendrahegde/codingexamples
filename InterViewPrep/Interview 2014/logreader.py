filename='log.log'
f=open(filename, 'r')
logdict={}
import re
import sys

for line in f.readlines():
  time=line.split()[:3]
  mins= ":".join(time[2].split(":")[:2])
  date=" ".join(time[:2])
  date_mins = " ".join([date, mins])
  
  if date_mins in logdict:
    logdict[date_mins]['count'] += 1
  else:
    logdict[date_mins] = {'count':1}
  prog = line.split()[4]
  progname = prog.split('[')[0]
  
  if progname in logdict[date_mins]:
      logdict[date_mins][progname] +=1
  else:
      logdict[date_mins] = {progname:1}
       
keys=[]
for key, val in logdict.iteritems():
  keys += val.keys()
  
uniq_progs = list(set(keys))
print uniq_progs

for key, val in logdict.iteritems():
  sys.stdout.write(key)
  for progs in val:
    sys.stdout.write(progs)
  print ""
    
