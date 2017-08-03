#simple script to 'clean' the xml files, 
#normalizing MWE and triple relations

import os
import re

cwd = os.getcwd()

for root, subFolders, files in os.walk('.'):
	for file in files:
		if file.endswith(".xml"):
			print file
			with open(os.path.join(root, file), "r+") as f:
				lines = f.readlines()
				# for line in lines:
				# 	print line
				# print "======================"
				for line in lines:
					#line for testing different possible formats
					# line = "<otriple>asdas | TestTestTest | adsasd</otriple>"

					#regex that captures only the line with the 'triples'
					result = re.match(r'(\s*<[om]triple>.*?\|\s)(.*?([A-Z]+?).*?)(\s\|.*?</[om]triple>)', line)

					#if result is not none, i.e., we captured the line we wanted, 
					#we gonna 'clean' the text
					if result != None:
						pre = result.group(1)
						rel = result.group(2)
						suf = result.group(4)
						newrel = re.sub(r'(?=[A-Z])',' ',rel).lower()
						newpre = re.sub(r'_',' ',pre)
						newsuf = re.sub(r'_',' ',suf)
						
						with open(os.path.join(root, "clean_"+file),"a+") as o:
							o.write(newpre+newrel+newsuf+"\n")
						#print instead of writting, for checking
						# print newpre+newrel+newsuf+"\n"
					else:
						with open(os.path.join(root, "clean_"+file),"a+") as o:
							o.write(line)
						#print instead of writting, for checking
						# print line