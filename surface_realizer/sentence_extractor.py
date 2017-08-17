#prepare data
import os
import unicodedata
from bs4 import BeautifulSoup as bs

cwd = os.getcwd()

for filename in os.listdir(cwd):
	if filename.endswith('.xml'):
		with open(filename, "r+") as fp:
			fullname = os.path.join(cwd, filename)
			domain = filename.split("_")[1].strip(".xml")
			soup = bs(fp, "lxml")
    		for elem in soup.findAll('lex'):
				print domain
				with open(cwd+"/extracted_sentences/"+domain+".txt","a+") as output:
					sentence = elem.string.encode('utf-8')
					output.write(sentence+'\n')