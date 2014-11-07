import os
##wPath = "/home/cg/palantir/wTest/"
wPath = "/home/cg/palantir/w/"
def openImgFile(imgID):
	path = wPath + imgID[0] + '/' + imgID[1] + '/' + imgID[2] + '/' + imgID + ".imgInfo"
	if os.path.exists(path):	
		f = open(path, 'r+')
	else:
		f = open(path, 'w')
		os.chmod(path, 00777)
		createImgInfo(f, imgID)
		f = open(path, 'r+')
	return f

def createImgInfo(file, imgID):
	imgInfo_lines = []
	imgInfo_lines.append("ImgInfo " + imgID + "\n")
	imgInfo_lines.append("blank\n")
	for line in imgInfo_lines:
		file.write(line)
	file.close()

def updateImgFile(type, cameraID, newID, numItems):
	f = openImgFile(cameraID)
	img_lines = f.readlines()
	img_lines = checkForBlanks(img_lines)
	tile_found = False
	if type == 'c': ##assert: we are adding a corner
		ls = img_lines[1].split()
		if ls.count(newID) == 0:
			img_lines[1]= img_lines[1].rstrip()
			img_lines[1] += (' ' + newID + '\n')
	elif type == 'c_rem':
		ls = img_lines[1].split()
		popThis = 0
		for i in range(len(ls)):
			if ls[i] == newID:
				popThis = i
				ls.pop(popThis)
				break
		img_lines[1] = ""
		for j in range(len(ls)):
			img_lines[1]+=ls[j] + " "
		img_lines[1].rstrip()
		img_lines[1] +='\n'
	elif type == 't_inc': ##assert: we are adding a tile to increment or decrement fiber count
		for i in range(2,len(img_lines)):
			ls = img_lines[i].split()
			if ls[0] == newID:
				tile_found = True
				current = int(ls[1])
				new = current + numItems
				ls[1] = str(new)
				img_lines[i] = ""
				for item in ls:
					img_lines[i] += (item + ' ')
				img_lines[i] = img_lines[i].rstrip() + '\n'
		if not tile_found:
			img_lines.append(newID +' ' + str(numItems) +"\n")
	elif type == 't_dec': ##assert: we are adding a tile to increment or decrement fiber count
		for i in range(2,len(img_lines)):
			ls = img_lines[i].split()
			if ls[0] == newID:
				current = int(ls[1])
				new = current - numItems
				ls[1] = str(new)
				img_lines[i] = "" 
				for item in ls:
					img_lines[i] += (item + ' ')
				img_lines[i] = img_lines[i].rstrip() + '\n'	
			
	f.seek(0)
	f.truncate()
	for line in img_lines:
		line = line.replace("blank ", '')
		f.write(line)
	f.close()

def checkForBlanks(lines):
	for i in range(len(lines)):
		if lines[i] == '\n':
			lines[i] = "blank\n"
	return lines
