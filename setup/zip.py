import os
import zipfile
import shutil
import random

def zipdir(path, ziph):
	for root, dirs, files in os.walk(path):
		for file in files:
			ziph.write(os.path.join(root, file))

count=0
for folderName in os.listdir('Images/'):
	randDel = random.randint(0,2)
	if randDel == 0 and count < 35:
		shutil.rmtree('Images/'+folderName)
		count+=1



for folderName in os.listdir('Images/'):
	temp = folderName.split('-',1)
	print(temp[1])
	count = 1
	for filename in os.listdir('Images/'+folderName+'/'):
		count+=1
		if count > 11:
			os.remove('Images/'+folderName+'/'+filename)
	shutil.make_archive('Images/'+temp[1], 'zip', 'Images/'+folderName)

#temp = 'n02094433-Yorkshire_terrier'.split('-',1)
#print(temp[1]+'.zip')
#shutil.make_archive(temp[1], 'zip', 'n02094433-Yorkshire_terrier')
