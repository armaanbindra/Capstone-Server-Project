import os
#########Global Variables################
#########################################
all_versions = os.listdir("/home/cg/palantir/SharedDB-Server/BackupDB")
workingRoot = "/home/cg/palantir/w"
#workingRoot = "/home/cg/palantir/wTest"
#workingRoot = "/home/cg/palantir/SharedDB-Server/BackupDB/29.01.2014-14:56:21"
all_tiles = {} ## dictionary which will eventually contain all tiles and associated nFibers
all_corners = []

#########################################
####Functions To Use#####################
#########################################
def changeRoot(newRoot):
	workingRoot = newRoot

def run_old():
	print "Please Choose a Root Directory to Analyze:\n"
	for i in range(len(all_versions)):
		print str(i+1)+'\t'+all_versions[i]
	choice = raw_input("\nChoice:")
	
	workingRoot = "/home/cg/palantir/SharedDB-Server/BackupDB/"+all_versions[int(choice)-1]
	return workingRoot,all_versions[int(choice)-1]
	#analyze = True

def printCorner(corner):
  print '  ' + corner
  path = workingRoot + '/c/' + corner[0] + '/' + corner[1] + '/' + corner[2] + '/' + corner
  for line in open(path):
    print '    ' + line,

def printTile(tile):
  print '  ' + tile
  path = workingRoot + '/t/' + tile[0] + '/' + tile[1] + '/' + tile
  for line in open(path):
    print '    ' + line,

def printImgInfo(camName):
  print '  ' + camName
  path = workingRoot + '/' + camName[0] + '/' + camName[1] + '/' + camName[2] + '/' + camName + '.imgInfo'
  for line in open(path):
    print '    ' + line,

def countFibers(camName):
  path = workingRoot + '/' + camName[0] + '/' + camName[1] + '/' + camName[2] + '/' + camName + '.imgInfo'
  f = open(path,'r')
  img_lines = f.readlines()
  if not img_lines[1] == "blank\n":
          for corner in img_lines[1].split():
                  if not corner in all_corners: all_corners.append(corner)
  for i in range(2,len(img_lines)):
    if img_lines[i]== '\n' or img_lines[i]== "" or img_lines[i] == "blank":
      img_lines[i]= "blank"
      print "adding Blank"
    img_lines[i].rstrip()  
    ls = img_lines[i].split()
    ##print ls
    if not len(ls) < 2:
      tileID = ls[0]
      numFb = ls[1]
      if tileID in all_tiles:
        all_tiles[tileID]+= int(numFb)
      else:
        all_tiles[tileID] = int(numFb)
