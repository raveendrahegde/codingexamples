import os
def listfiles():
	pwd=os.getcwd()
	files=os.listdir(pwd)
	for f in files:
		if os.path.isdir(pwd+"/"+f):
			print f + "/"
			os.chdir(f)
			listfiles()
			os.chdir('..')
		else:
			print f

if __name__ == "__main__":
	listfiles()


