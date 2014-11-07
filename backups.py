import os
import shutil
import time

newRoot = ""
def copyFile(source,destination):
	##command = "cp "+source+" "+destination
	##os.system(command)
	if destination[-3:] == ".poly3":
		print destination
	file1 = open(source,'r')
	source_lines = file1.readlines()
	file1.close()
	file2 = open(destination, 'w')
	os.chmod(destination,00777)
	for line in source_lines:
		file2.write(line)
	file2.close()

def make_new_back_directory():
	global newRoot
	newDirectory  = "/home/cg/palantir/SharedDB-Server/BackupDB/" + time.strftime("%d.%m.%Y-%X")
	command = "cp -r /home/cg/palantir/SharedDB-Server/BackupDB/template "+newDirectory
	os.system(command)
	global newRoot
	newRoot = newDirectory
	print "newRoot is " + newRoot
	os.chmod(newDirectory,00777)
	return newDirectory
def recursiveChmod():
	global newRoot
	os.system("chmod 777 -R "+newRoot)
	

def db_backup(fileName,fileType):
	##newRoot = make_new_back_directory()
	##workingRoot = "home/cg/palantir/wTest"
	workingRoot = "/home/cg/palantir/w"
	path = ""
	newPath =""
	if fileType == 'c':
		path = workingRoot + '/c/' + fileName[0] + '/' + fileName[1] + '/' + fileName[2] + '/' + fileName
		newPath = newRoot + '/c/' + fileName[0] + '/' + fileName[1] + '/' + fileName[2] + '/' + fileName
	elif fileType == 't':
		path = workingRoot + '/t/' + fileName[0] + '/' + fileName[1] + '/' + fileName
		newPath = newRoot + '/t/' + fileName[0] + '/' + fileName[1] + '/' + fileName
	elif fileType == 'i':
		path = workingRoot + '/' + fileName[0] + '/' + fileName[1] + '/' + fileName[2] + '/' + fileName + '.imgInfo'
		newPath = newRoot + '/' + fileName[0] + '/' + fileName[1] + '/' + fileName[2] + '/' + fileName + '.imgInfo'
	elif fileType == 'p':
		path = workingRoot + '/t/' + fileName[0] + '/' + fileName[1] + '/' + fileName
		newPath = newRoot + '/t/' + fileName[0] + '/' + fileName[1] + '/' + fileName
	copyFile(path,newPath)

##newD = make_new_back_directory()
##print "new directory called " +newD+" made"
