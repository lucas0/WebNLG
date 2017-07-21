#simplest script ever, to join files into a single xml
#not sure if will be needed

import os

cwd = os.getcwd()
print cwd
with open(cwd+"/all.xml","w+") as outfile:
	for root, subFolders, files in os.walk('.'):
		for file in files:
			if file.endswith(".xml"):
				print file
				with open(os.path.join(root, file), "r+") as f:
					outfile.write(f.read())

