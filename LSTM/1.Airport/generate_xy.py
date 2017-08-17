#prepare data
import os
from bs4 import BeautifulSoup as bs

cwd = os.getcwd()

for filename in os.listdir(cwd):
	if filename.endswith('.xml'):
		fullname = os.path.join(cwd, filename)
		tree = bs(fullname)
		for elem in tree.findAll('')
		print tree