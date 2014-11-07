import os
import sys
workingRoot = "/home/cg/palantir/w"
ImgsDictC = {}
ImgsDictT = {}
def getDataFromCorner(corner):
	path = workingRoot + "/c/"+corner[0]+"/"+corner[1]+"/"+corner[2]+"/"+corner
	f = open(path,'r')
	corner_lines = f.readlines()
	for i in range(3,len(corner_lines)):
		ls = corner_lines[i].split()
		if ls[0] in ImgsDictC:
			ImgsDictC[ls[0]].append(corner)
		else:
			ImgsDictC[ls[0]]= [corner]
	f.close()

def getDataFromTile(tile):
	path = 	workingRoot + "/t/"+tile[0]+"/"+tile[1]+"/"+tile
	f = open(path,'r')
	tile_lines = f.readlines()
	for i in range(2,len(tile_lines)):
		ls = tile_lines[i].split()
		if ls[0] in ImgsDictT:
			ImgsDictT[ls[0]][tile]=len(ls)-1
		else:
			ImgsDictT[ls[0]]={}
			ImgsDictT[ls[0]][tile]=len(ls)-1
	f.close()
		
			

nCorners = 0
if os.path.exists(workingRoot + '/c'):
  # for digit0 in os.listdir(workingRoot + '/c'):
  for digit0 in ['1','2','3','4']:
    for digit1 in os.listdir(workingRoot + '/c/' + digit0):
      for digit2 in os.listdir(workingRoot + '/c/' + digit0 + '/' + digit1):
        path = workingRoot + '/c/' + digit0 + '/' + digit1 + '/' + digit2
        # print path
        #if len(os.listdir(path)) > 0:
          #print path, os.listdir(path)
        for corner in os.listdir(path):
          nCorners += 1
  	  getDataFromCorner(corner)

nTiles = 0
##Loop Through All Tile Files
if os.path.exists(workingRoot + '/t'):
  for digit0 in os.listdir(workingRoot + '/t'):
    for digit1 in os.listdir(workingRoot + '/t/' + digit0):
      path = workingRoot + '/t/' + digit0 + '/' + digit1
      # print path
      if len(os.listdir(path)) > 0:
        ##print path, os.listdir(path)
        a = 2
      	for tile in os.listdir(path):
	  if not tile.endswith('.poly3'):
            nTiles += 1
	    getDataFromTile(tile)

#print ImgsDictC["1130R"]
#print ImgsDictT["1130R"]
temp_ls=[]
for img in ImgsDictT:
	for tID in ImgsDictT[img]:
		if ImgsDictT[img][tID]==0:
			temp_ls.append(tID)
	for i in temp_ls:
		del ImgsDictT[img][i]
	temp_ls=[]
def createImgInfo(cameraID):
	path = workingRoot+"/"+cameraID[0]+"/"+cameraID[1]+"/"+cameraID[2]+"/"+cameraID+".imgInfo"
	img_lines = ["ImgInfo	"+cameraID]
	if cameraID in ImgsDictC:
		if ImgsDictC[cameraID]:
			temp = ""
			for i in ImgsDictC[cameraID]:
				temp+=" "+i
			temp = temp.lstrip()
			img_lines.append(temp)
		else:
			img_lines.append("blank")
	else:
		img_lines.append("blank")	
	for tID in ImgsDictT[cameraID]:
		img_lines.append(tID+" "+str(ImgsDictT[cameraID][tID]))
	final = open(path,"w")
	for line in img_lines:
		line+="\n"
		final.write(line)
	final.close()
for img in ImgsDictT:
	createImgInfo(img)

#print ImgsDictC["1130R"]
#print ImgsDictT["1130R"]
