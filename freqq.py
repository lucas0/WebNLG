#generates the ordered_prep_freq.txt
from collections import defaultdict

mydict = list()
with open("prep_freq.txt") as fin:
    for line in fin:
    	k = eval("{"+line+"}")
    	mydict.append(k)

while len(mydict) > 0:
	print len(mydict)
	bigger = 0
	b_elem = None
	b_idx = 0
	for idx,elem in enumerate(mydict):
		e = elem.itervalues().next()
		print e
		if e['count'] > bigger:
			b_idx = idx
			b_elem = elem
			bigger = e['count']
	with open("ordered_prep_freq.txt","a+") as o:
		o.write(str(b_elem)+"\n")
	del mydict[b_idx]