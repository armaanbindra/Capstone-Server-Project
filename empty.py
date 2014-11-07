#!/usr/bin/python
#!/opt/local/bin/python

import os, sys

remove = (len(sys.argv) > 1) and (sys.argv[1] == '-rm')
# print remove

#workingRoot = "/Users/olaf/proj/eriol2/scripts/w"
##workingRoot = "/home/cg/palantir/w"
workingRoot = "/home/cg/palantir/SharedDB-Server/BackupDB/template"
os.chdir(workingRoot)
#print os.listdir('.')
# exit()
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

print 'saved corners:'
nCorners = 0
if os.path.exists(workingRoot + '/c'):
  # for digit0 in os.listdir(workingRoot + '/c'):
  for digit0 in ['1']:
    for digit1 in os.listdir(workingRoot + '/c/' + digit0):
      for digit2 in os.listdir(workingRoot + '/c/' + digit0 + '/' + digit1):
        path = workingRoot + '/c/' + digit0 + '/' + digit1 + '/' + digit2
        # print path
        if len(os.listdir(path)) > 0:
          print path, os.listdir(path)
        for corner in os.listdir(path):
          nCorners += 1
          if remove:
            os.remove(path + '/' + corner)
          else:
            printCorner(corner)

print 'saved tiles:'
nTiles = 0
if os.path.exists(workingRoot + '/t'):
  for digit0 in os.listdir(workingRoot + '/t'):
    for digit1 in os.listdir(workingRoot + '/t/' + digit0):
      path = workingRoot + '/t/' + digit0 + '/' + digit1
      # print path
      if len(os.listdir(path)) > 0:
        print path, os.listdir(path)
      for tile in os.listdir(path):
        nTiles += 1
        if remove:
          os.remove(path + '/' + tile)
        else:
          printTile(tile)

print 'saved imgInfo:'
nImgs = 0
if os.path.exists(workingRoot):
  for digit0 in ['0', '1','2','3','4']:
    for digit1 in os.listdir(workingRoot + '/' + digit0):
      for digit2 in os.listdir(workingRoot + '/' + digit0 + '/' + digit1):
        path = workingRoot + '/' + digit0 + '/' + digit1 + '/' + digit2
        # print path
        for fname in os.listdir(path):
          if fname.endswith('.ppm') or fname.endswith('.ppm.seg'):
            nImgs += 1
            if remove:
              os.remove(path + '/' + fname)
            else:
              camName = fname[:(len(fname)-8)]
              ##printImgInfo(camName)

print 'nCorners', nCorners, 'nTiles', nTiles, 'nImgs', nImgs
