#!/usr/bin/python
#!/opt/local/bin/python

import os, sys
#test_name = "Wall_Stone"
all_tiles = {}

# print remove
checkRoot = (len(sys.argv) > 1)
#workingRoot = "/Users/olaf/proj/eriol2/scripts/w"
#workingRoot = "/home/cg/palantir/w"
workingRoot = sys.argv[1]
print "workingRoot is "+workingRoot
#workingRoot = "/Users/olaf/proj/eriol2/scripts/w"
#workingRoot = "/home/cg/palantir/w"
##workingRoot = "/home/cg/palantir/wTest"
os.chdir(workingRoot)
#print os.listdir('.')
# exit()

 
def getLength(tile):
  path = workingRoot + '/t/' + tile[0] + '/' + tile[1] + '/' + tile
  listImgs = []
  currentTile = open(path,'r')
  tile_lines = currentTile.readlines()
  return len(tile_lines)

def getImg(tile):
  corners = []
  
  path = workingRoot + '/t/' + tile[0] + '/' + tile[1] + '/' + tile
  listImgs = []
  currentTile = open(path,'r')
  tile_lines = currentTile.readlines()
  for i in tile_lines[1].split():
    corners.append(i)
  if tile_lines[0]=="\n":
    print "blank placed at " + tile_lines[0]
    tile_lines[0]="blank\n"
  for i in range(2,len(tile_lines)):
    listImgs.append(tile_lines[i].split()[0])
  return listImgs+corners

nTiles = 0
##Loop Through All Tile Files
if os.path.exists(workingRoot + '/t'):
  for digit0 in os.listdir(workingRoot + '/t'):
    for digit1 in os.listdir(workingRoot + '/t/' + digit0):
      path = workingRoot + '/t/' + digit0 + '/' + digit1
      # print path
      if len(os.listdir(path)) > 0:
      	for tile in os.listdir(path):
	  if not tile.endswith('.poly3'):
	    len_tile = getLength(tile)
            nTiles += 1
	    if len_tile > 4:
	      all_tiles[tile]= getImg(tile)
for i in all_tiles:
  print i+":"+str(all_tiles[i])
