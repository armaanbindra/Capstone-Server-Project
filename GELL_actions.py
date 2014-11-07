## This file defines the actions to me taken based on each action reported by the client
## argument 'action' should be of list form with the command at index 0

import os, ImgFile_Ops
#wPath = "/home/cg/palantir/wTest/"#Test Directory
wPath = "/home/cg/palantir/w/"
def execute(action):
	if len(action) == 0:
		print("empty line")
		##skip
	elif action[0] == "addFiber": ##[addFiber, tileID, cameraID, SuperPixel IDs]		
		num_new_pixels = 0		
		tileID =  action[1]
		cameraID = action[2]
		f,tile_lines = tileOpen(tileID)
		cameraID_found = False
		for i in range(2,len(tile_lines)):
			local_ls = tile_lines[i].split()
			##print("Local ls is: " + str(local_ls))
			if local_ls[0] == cameraID:
				cameraID_found = True
				tile_lines[i] = tile_lines[i].rstrip()
				for j in range(3, len(action)):
					if not local_ls.count(action[j]):
						tile_lines[i] += (" " + action[j])
						num_new_pixels += 1
				tile_lines[i] += "\n"
		if not cameraID_found:
			new_ID_line = cameraID
			for j in range(3, len(action)):
					new_ID_line += (' ' + action[j])
					num_new_pixels += 1
			new_ID_line += '\n'
			tile_lines.append(new_ID_line)
		deleteContent(f)
		writeFile(f, tile_lines) ##output edited file
		##print "Num new pixels: " + str(num_new_pixels)
		ImgFile_Ops.updateImgFile("t_inc", cameraID, tileID, num_new_pixels)

	elif action[0] == "removeFiber": ##[removeFiber, tileID, cameraID, SuperPixel IDs]
		tileID = action[1]
		cameraID = action[2]
		f,lines = tileOpen(tileID)
		deleteThesePixels = []      ##blank list, to hold pixel ids 
		for i in range(3, len(action)):
			deleteThesePixels.append(action[i]) ##loop adds all pixels to be deleted 
		for i in range(2,len(lines)):
			ls = lines[i].split() #split string by spaces, sve as a list in ls
			if ls[0] == action[2]: ## check for cameraID we want - stored as first item in list
				for pixel in deleteThesePixels:  ##we are on the right line
					if ls.count(pixel):	
						ls.remove(pixel)         ##cycle pixels to delete and remove from line
				lines[i] = "" ##empty the line
				for item in ls:
					lines[i] += item ##rewrite the line  without the deleted pixels
					lines[i] += " "
				lines[i] = lines[i].rstrip()
				lines[i] += "\n"
		deleteContent(f) #delete old contents of tile file
		writeFile(f, lines) #output edited file
		ImgFile_Ops.updateImgFile("t_dec", cameraID, tileID, (len(action)-3))

	elif action[0] == "addFeature": ##[addFeature, cornerID, cameraID, [x,y,0]]
		cornerID = action[1]	#store info
		cameraID = action[2]
		coords = action[3]
		f,corner_lines = cornerOpen(cornerID)	#open file
		for i in range(3, len(corner_lines)):	#excise old feature pt if it exists
			if corner_lines[i][:5] == cameraID:
				corner_lines.pop(i)
				break
		corner_lines.append(cameraID + ' ' + coords[:-2] + '\n')	#add the new feature pt
		deleteContent(f)
		writeFile(f, corner_lines)
		ImgFile_Ops.updateImgFile('c', cameraID, cornerID, 1)

	elif action[0] == "removeFeature": ##[removeFeature, CornerID, cameraID, [x,y,0]]
		cornerID = action[1]
		cameraID = action[2]
		f,corner_lines = cornerOpen(cornerID)
		target = False
		for i in range(len(corner_lines)):
			if corner_lines[i][:5] == cameraID:
				target = i
		if target:		
			corner_lines.pop(target)
		deleteContent(f)
		writeFile(f, corner_lines)
		ImgFile_Ops.updateImgFile("c_rem", cameraID, cornerID, (len(action)-3))

	elif action[0] == "addPin": ##[addPin, tileID, cornerID]
        	tileID =  action[1]
		cornerID = action[2]
		f,tile_lines = tileOpen(tileID) ##open tile file
		pin_list = tile_lines[1].split()
		if not pin_list.count(cornerID):
			tile_lines[1] = tile_lines[1].rstrip() #remove whitespace
			tile_lines[1] += (' ' + cornerID + "\n") ##append cornerID to corner list in tile file

		deleteContent(f) ##clear tile file
		writeFile(f, tile_lines) ##write local copy back to file

		f,corner_lines = cornerOpen(cornerID) ##open corner file
		pin_list = corner_lines[2].split()
		if not pin_list.count(cornerID):
			corner_lines[2] = corner_lines[2].rstrip() ##remove whitesapce
			corner_lines[2] += (' ' + tileID +"\n") ##append linked tileID

		deleteContent(f) ##clear corner file
		writeFile(f, corner_lines) ##write local copy back to file
		
	elif action[0] == "removePin": ##[removePin, tileID, cornerID]
		tileID =  action[1]
		cornerID = action[2]
		f,tile_lines = tileOpen(tileID) ##open tile file
		corner_list = tile_lines[1].split() ##copy string of corner(s) into a list
		if corner_list.count(cornerID) != 0:		
			corner_list.remove(cornerID) ##remove the cornerID associated with PIN
		tile_lines[1] = "" ##set string of corners to empty
		for corner in corner_list: ##recreate string of corners from corner_list
			tile_lines[1] += corner + ' '
		tile_lines[1] = tile_lines[1].rstrip() + '\n'
		if tile_lines[1] == "\n":
			tile_lines[1] = "blank\n"

		deleteContent(f) 
		writeFile(f, tile_lines) 

		f,corner_lines = cornerOpen(cornerID) ##open corner file
		tile_list = corner_lines[2].split() ##move string of tileIDs to list
		if tile_list.count(tileID) != 0: ##remove the tileID associated with PIN
			tile_list.remove(tileID)
		corner_lines[2] = "" ##empty the tileID string
		for tile in tile_list: ##copy edited list of tileIDs to string
			corner_lines[2] += tile + ' '
		corner_lines[2] = corner_lines[2].rstrip() + '\n'
		if corner_lines[2] == "\n":
			corner_lines[2] = "blank\n"

		deleteContent(f) 
		writeFile(f, corner_lines) 


	elif action[0] == "setName": ##[setName, tileID, name_string]
		if len(action) < 3:
			print("SetName called with no name")
			##skip
		else:
			tileID = action[1]
			tileName = action [2]
			f,tile_lines = tileOpen(tileID)
			tile_lines[0] = tile_lines[0].split()
			tile_lines[0] = tile_lines[0][0] + ' ' + tile_lines[0][1] + ' ' + tileName + '\n'
			deleteContent(f)
			writeFile(f, tile_lines)
		
	elif action[0] == "setFeaturePoint": ##[setFeaturePoint, cornerID, cameraID, [x,y,0]]
                cornerID = action[1]
                cameraID = action[2]
                action[3] = action[3][:-2]
                f,corner_lines = cornerOpen(cornerID)## open corner file
                fp_exists = 0
                for i in range(len(corner_lines)):
                        ls = corner_lines[i].split()
                        if(ls[0]==cameraID):
                                corner_lines[i]= cameraID + ' ' +action[3]+"\n"
                                fp_exists = 1
                if(fp_exists == 0):
                        temp = cameraID + ' ' +action[3]+"\n"
                        corner_lines.append(temp)
                deleteContent(f)
                writeFile(f, corner_lines)

	elif action[0] == "setCornerPt": ##[setCornerPt, cornerID, [x,y,z]]
		cornerID = action[1]
		f,corner_lines = cornerOpen(cornerID)## open corner file
		corner_lines[1] = action[2] + '\n'
		
		deleteContent(f)
		writeFile(f,corner_lines)
	elif action[0] == "setPoly3": ##[setPoly3, tileID, nVerts, nFaces, [x,y,z,u,v]*nVerts, [imageID,indices*]*nFaces ]
		action.pop(0)
		tileID = action[1]
		nVerts = int(action[2])
		nFaces = int(action[3])
		f, poly3_lines = poly3Open(tileID)
		poly3_lines.append(action.pop(0) + ' ' + action.pop(0) + ' ' + action.pop(0) + ' ' + action.pop(0) + '\n') 	##assert now at first vert
		for i in range(nVerts):
			poly3_lines.append(pop5(action))
		for i in range(nFaces):
			poly3_lines.append(findFace(action))
		writeFile(f, poly3_lines)
	elif action[0] == "setNoPoly3": ##[setNoPoly3, tileID]
                tileID = action[1]
                fname = tileID + ".poly3"
                os.remove(wPath + "t/" + tileID[0] + "/" + tileID[1] + "/" + fname)
                #os.remove("/home/cg/palantir/wTest/t/" + tileID[0] + "/" + tileID[1] + "/" + fname)

	else:
		##print action[0]+"Not Implemented"
		return 0

#Helper Functions
def deleteContent(file): ##clears file to be empty
	file.seek(0)
	file.truncate()

def writeFile(file, lines):  ##writes a list of strings to file
	file.seek(0)
	for line in lines:
	###	print "writing.... ", line
		line = line.replace("blank ", '')
		file.write(line)
	file.close()

def tileOpen(tileID): ##takes arg of form 123user
	path = wPath + "t/" + tileID[0] + '/' + tileID[1] + '/'
        full_path = path + tileID
	if os.path.exists(full_path):
		file = open(full_path, 'r+')
	else:
		file = open(full_path, 'w')
		os.chmod(full_path, 00777)
		createTile(file, tileID)
		file = open(full_path, 'r+')
	tile_lines = file.readlines()
	tile_lines = ImgFile_Ops.checkForBlanks(tile_lines)
	return file, tile_lines

def cornerOpen(cornerID): ##takes arg of form 1234user
	path = wPath + "c/" + cornerID[0] + '/' + cornerID[1] + '/' + cornerID[2] + '/'
	full_path = path + cornerID
	if os.path.exists(full_path):
		file = open(full_path, 'r+')
	else:
		file = open(full_path, 'w')
		os.chmod(full_path, 00777)
		createCorner(file, cornerID)
		file = open(full_path, 'r+')
	corner_lines = file.readlines()
	corner_lines = ImgFile_Ops.checkForBlanks(corner_lines)
	return file, corner_lines

def poly3Open(tileID):
	path = wPath + "t/" + tileID[0] + '/' + tileID[1] + '/' + tileID + ".poly3"
	##print "Path for poly 3 " + path
	new = False
	if not os.path.exists(path):
		new = True
	file = open(path, 'w')
	if new == True:
		os.chmod(path, 00777)
	poly3_lines = [] ##we are only writing to this file. no read necessary. 
	return file, poly3_lines

def createTile(file, tileID):
	tile_lines = []
	tile_lines.append("Tile " + tileID + " name\n")
	tile_lines.append("blank\n")
	for line in tile_lines:
		file.write(line)
	file.close()

def createCorner(file, cornerID):
	corner_lines = []
	corner_lines.append("Corner " + cornerID + "\n")
	corner_lines.append("0.00,0.00,0.00\n")
	corner_lines.append("blank\n")
	for line in corner_lines:
		file.write(line)
	file.close()

def pop5(my_list):
	string = ""
	for i in range(5):
		string += str(my_list.pop(0)) + " "
	string = string.rstrip()
	string += '\n'
	return string

def findFace(poly3_list):
	string = ""
	while True:
		new = poly3_list.pop(0)
		string += str(new) + " "
		if len(poly3_list) == 0 or isNewFace(poly3_list[0]):
			break
	string = string.rstrip()
	string += '\n'
	return string

def isNewFace(string):
	try:
		float(string)
		return False
	except ValueError:
		return True 


		
