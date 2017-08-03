#simplest script ever, to join files into a single xml
#not sure if will be needed

import os

cwd = os.getcwd()
print cwd

for root, subFolders, files in os.walk('.'):
	for file in files:
		if file.endswith(".xml") and file.startswith("clean"):
			if "allSolutions" in file:
				domain = str(file).split("_")[3]
			else:
				domain = str(file).split("_")[2]
			print file, domain
			with open(os.path.join(root, file), "r+") as f:
				with open(cwd+"/all_"+domain+".xml","a+") as outfile:
					outfile.write(f.read())

