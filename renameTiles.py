#!/usr/bin/python
#!/opt/local/bin/python

import os, sys

remove = (len(sys.argv) > 1) and (sys.argv[1] == '-rm') ## removes tilda
# print remove

#workingRoot = "/Users/olaf/proj/eriol2/scripts/w"
workingRoot = "/home/cg/palantir/w"
##workingRoot = "/home/cg/palantir/wTest"
os.chdir(workingRoot)
#print os.listdir('.')
# exit()

nameFile = open("/home/cg/palantir/SharedDB-Server/changeNames",'r')
nameList = nameFile.readlines() 

def printCorner(corner):
  print '  ' + corner
  path = workingRoot + '/c/' + corner[0] + '/' + corner[1] + '/' + corner[2] + '/' + corner
  for line in open(path):
    print '    ' + line,

def renameTile(tile):
  ##print '  ' + tile
  changesToMake = open("/home/cg/palantir/SharedDB-Server/changesToMake",'a')
  path = workingRoot + '/t/' + tile[0] + '/' + tile[1] + '/' + tile
  username = tile[3:]
  currentTile = open(path, 'r+')
  tile_lines = currentTile.readlines()
  if tile_lines[0]=="\n":
    print "blank placed at " + tile_lines[0]
    tile_lines[0]="blank\n"
  firstLine = tile_lines[0].split()
  currentName = firstLine[2]
  check = 0
  final_newName = ""
  for name in nameList:
    temp = name.split()
    oldName = temp[0]
    newName = temp[1]
    shinyNewName = "!"+temp[1]
    if oldName == currentName or newName == currentName or shinyNewName == currentName:
      firstLine[2] = newName
      final_NewName = newName
      check = 1
      break
  if check == 0:
    if not (currentName == final_newName):
      check_str =  username+": should rename "+tile+" with name "+currentName+" at "+path+"\n"
      changesToMake.write(check_str)
    
  tile_lines[0] = "Tile " + firstLine[1]+" "+firstLine[2]+"\n"
  
  currentTile.seek(0)
  currentTile.truncate()
  for line in tile_lines:
    currentTile.write(line)
  currentTile.close()
  changesToMake.close()

def printImgInfo(camName):
  print '  ' + camName
  path = workingRoot + '/' + camName[0] + '/' + camName[1] + '/' + camName[2] + '/' + camName + '.imgInfo'
  for line in open(path):
    print '    ' + line,

##print 'saved tiles:'
nTiles = 0
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
            if remove:
	      if tile[-1] == '~':				#eliminating tilda ~ files
                os.remove(path + '/' + tile)
            else:
          ##printTile(tile)
              renameTile(tile)
