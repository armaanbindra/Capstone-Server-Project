#!/usr/bin/python
#!/opt/local/bin/python

import os, sys
#test_name = "Wall_Stone"
all_imgs = [] ## List, to eventually keep track of all images associated with the given tile Name
tileName = "" ## variable to hold the queried tile name passed as a commandline argument
arg_bool = (len(sys.argv) >= 1)
if not arg_bool:
  print "You did not provide any command line arguments, please give a tile name for the Query"
  exit(0)
else:
  tileName = sys.argv[1]
# print remove

#workingRoot = "/Users/olaf/proj/eriol2/scripts/w"
workingRoot = "/home/cg/palantir/w"
##workingRoot = "/home/cg/palantir/wTest"
os.chdir(workingRoot)
#print os.listdir('.')
# exit()

nameFile = open("/home/cg/palantir/SharedDB-Server/changeNames.txt",'r')
nameList = nameFile.readlines() 

def getName(tile):
  path = workingRoot + '/t/' + tile[0] + '/' + tile[1] + '/' + tile
  username = tile[3:]
  currentTile = open(path,'r')
  tile_lines = currentTile.readlines()
  if tile_lines[0]=="\n":
    print "blank placed at " + tile_lines[0]
    tile_lines[0]="blank\n"
  firstLine = tile_lines[0].split()
  currentName = firstLine[2]
  currentTile.close()
  return currentName

def getImg(tile):
  path = workingRoot + '/t/' + tile[0] + '/' + tile[1] + '/' + tile
  listImgs = []
  currentTile = open(path,'r')
  tile_lines = currentTile.readlines()
  if tile_lines[0]=="\n":
    print "blank placed at " + tile_lines[0]
    tile_lines[0]="blank\n"
  for i in range(2,len(tile_lines)):
    listImgs.append(tile_lines[i].split()[0])
  return listImgs

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
	    if getName(tile)==tileName:
	      all_imgs += getImg(tile)

if not all_imgs:		##Checks to make sure the given tile name is in database or not
  print "Sorry There are no Tiles By the name "+tileName+" in our database"
  exit(0)

all_imgs = list(set(all_imgs))
all_imgs.sort() 
result = tileName + ": "
for img in all_imgs:
  result+=img+","
result = result[:-1]
print result
