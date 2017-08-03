#simple script to obtain frequency of different prepositions and its collocators
import os
import nltk
import re
import sys
from nltk.chunk import tree2conlltags

reload(sys)
sys.setdefaultencoding('utf-8')

cwd = os.getcwd()

preps = dict()

for root, subFolders, files in os.walk('.'):
	for file in files:
		#check only original xml files, not the 'clean' ones
		if file.endswith(".xml") and "clean" not in file:
			print file
			with open(os.path.join(root, file), "r+") as readfile:
				lines = readfile.readlines()
				for line in lines:
					result = re.match(r'(\s*<lex\s.*?>)(.*?)(</lex>)', line)
					if result != None:
						sentence = result.group(2)
						text = nltk.word_tokenize(sentence)
						tags = nltk.pos_tag(text)
						ne_tree = nltk.ne_chunk(tags)
						iob_tagged = tree2conlltags(ne_tree)
						for idx,word in enumerate(iob_tagged):
							if idx+1 < len(iob_tagged):
								collo = iob_tagged[idx+1]
							if (word[1][0] == "V") and (collo[1] == "IN"):
								# print word, collo
								if word[0].lower() not in preps:
									preps[word[0].lower()] = {'count':1}
								else:
									preps[word[0].lower()]['count'] += 1

								if collo[0].lower() not in preps[word[0].lower()]:
									preps[word[0].lower()][collo[0].lower()] = 1
								else:
									preps[word[0].lower()][collo[0].lower()] += 1

while len(preps) > 0:
	bigger = 0
	b_elem = None
	for elem in preps:
		e = preps[elem]
		if e['count'] > bigger:
			b_elem = elem
			bigger = e['count']
	# print(str(b_elem)+str(preps[b_elem])+"\n")
	with open("ordered_verb-prep_freq.txt","a+") as o:
		o.write(str(b_elem)+str(preps[b_elem])+"\n")
	del preps[b_elem]