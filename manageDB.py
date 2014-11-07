#!/usr/bin/python
#!/opt/local/bin/python

import os, sys 
import backups
import time
from funcs_for_manageDB import *

remove = (len(sys.argv) > 1) and (sys.argv[1] == '-rm')
backup = (len(sys.argv) > 1) and (sys.argv[1] == '-bu')
analyze = (len(sys.argv) > 1) and (sys.argv[1] == '-a')
printing = (len(sys.argv) > 1) and (sys.argv[1] == '-pr')
print_img = (len(sys.argv) > 2) and (sys.argv[1] == '-i')
findTile = (len(sys.argv) > 2) and (sys.argv[1] == '-t')
print_poly3 = (len(sys.argv) > 1) and (sys.argv[1] == '-p3')
old_version = (len(sys.argv) > 1) and (sys.argv[1] == '-old')
#newVal = raw_input("Where would you like to run the analysis?"


if old_version:
	
	workingRoot,old_time = run_old()
	analyze = True
	'''
	print "Please Choose a Root Directory to Analyze:\n"
	for i in range(len(all_versions)):
		print str(i+1)+'\t'+all_versions[i]
	choice = raw_input("\nChoice:")
	changeRoot("home/cg/palantir/SharedDB-Server/BackupDB/"+all_versions[int(choice)-1])
	analyze = True
	'''
#changeRoot("home/cg/palantir/wTest")

if findTile:
  tileToFind = sys.argv[2]
if print_img:
  imgToFind = sys.argv[2]
polyPrint = False
if (len(sys.argv) > 2) and sys.argv[1] == "-p3":
	print_poly3 = False
	polyToFind = sys.argv[2]+".poly3"
	polyPrint = True

os.chdir(workingRoot)

print "Current Root is:" + workingRoot
if print_img:
  printImgInfo(imgToFind)
if findTile:
  printTile(tileToFind)
if polyPrint:
  printTile(polyToFind)

if remove:
	print "Are you sure you want to delete everything!"
	checking = raw_input("Type yes to continue: ")
	if checking == "yes" or "Yes":
		if workingRoot[-1:] == 'w':
			print "Sorry We are in the Real Shared Database, No Wipe Allowed"
			remove = False
		else:
			remove = True
	else:
		remove = False
if backup:
	newBackupPath = backups.make_new_back_directory()
if printing:
	print 'saved corners:'
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
          if remove:
            os.remove(path + '/' + corner)
          if printing:
            printCorner(corner)
	  if backup:
	    backups.db_backup(corner, 'c')
if printing:
	print 'saved tiles:'
nTiles = 0
if os.path.exists(workingRoot + '/t'):
  for digit0 in os.listdir(workingRoot + '/t'):
    for digit1 in os.listdir(workingRoot + '/t/' + digit0):
      path = workingRoot + '/t/' + digit0 + '/' + digit1
      # print path
      #if len(os.listdir(path)) > 0:
        #print path, os.listdir(path)
      for tile in os.listdir(path):
	if not tile.endswith('.poly3'):
            nTiles += 1
            if remove:
              os.remove(path + '/' + tile)
            if printing:
              printTile(tile)
	    if backup:
	      backups.db_backup(tile, 't')

if printing:
	print 'saved poly3s:'
nPoly3 = 0
if os.path.exists(workingRoot + '/t'):
  for digit0 in os.listdir(workingRoot + '/t'):
    for digit1 in os.listdir(workingRoot + '/t/' + digit0):
      path = workingRoot + '/t/' + digit0 + '/' + digit1
      # print path
      #if len(os.listdir(path)) > 0:
        #print path, os.listdir(path)
      for poly3 in os.listdir(path):
	if poly3.endswith('.poly3'):
        	nPoly3 += 1
        	if remove:
         		os.remove(path + '/' + poly3)
       		if printing or print_poly3:#
         		printTile(poly3)
			#print poly3
		if backup:
	    		backups.db_backup(poly3, 'p')

if printing:
	print 'saved imgInfo:'
nImgs = 0
if os.path.exists(workingRoot):
  for digit0 in ['0', '1','2','3','4']:
    for digit1 in os.listdir(workingRoot + '/' + digit0):
      for digit2 in os.listdir(workingRoot + '/' + digit0 + '/' + digit1):
        path = workingRoot + '/' + digit0 + '/' + digit1 + '/' + digit2
        # print path
        for fname in os.listdir(path):
          if fname.endswith(".imgInfo"):
            #print fname,
            nImgs += 1
            if remove:
              os.remove(path + '/' + fname)
            if printing:
              camName = fname[:(len(fname)-8)]
              printImgInfo(camName)
	    if backup:
	      camName = fname[:(len(fname)-8)]
	      backups.db_backup(camName, 'i')
	    if analyze:
	      camName = fname[:(len(fname)-8)]
	      countFibers(camName)

#################
all_users = {}
for key in all_tiles:
  if key[3:] in all_users:
    all_users[key[3:]][0] += 1
  else:
   all_users[key[3:]] = [1]


for key in all_corners:
        if key[4:] in all_users:
                if (len(all_users[key[4:]]) > 1):
                        all_users[key[4:]][1] += 1
                else:
                        all_users[key[4:]].append(1)


#################	 
if backup:
	backups.recursiveChmod()
	print "Server Has Been Backed up at "+ newBackupPath
	
if printing:
	print 'nCorners', nCorners, 'nTiles', nTiles,'nPoly3s', nPoly3, 'nImgs', nImgs
if analyze:

	analysis_bu = "/home/cg/palantir/SharedDB-Server/BackupDB/Analysis/Analysis_at_"+time.strftime("%d.%m.%Y-%X")
	if old_version:
		analysis_bu = "/home/cg/palantir/SharedDB-Server/BackupDB/Analysis/Analysis_at_"+old_time
	#print analysis_bu
	f2 = open(analysis_bu,'w')
	os.chmod(analysis_bu,00777)
	print "Currently in our Shared Data Base:\n"
	f2.write("Currently in our Shared Data Base:\n")
	print "We Have "+ str(nCorners)+ " corners," +str(nTiles)+ " tiles and "+str(nImgs)+ " imageInfo Files, and "+str(nPoly3)+" Poly3s\n"
	f2.write("We Have "+ str(nCorners)+ " corners," +str(nTiles)+ " tiles and "+str(nImgs)+ " imageInfo Files, and "+str(nPoly3)+" Poly3s\n")
	print "The Top Ten Tiles with the most Fibers are:"
	for i in range(10):
		maxTile = max(all_tiles, key=all_tiles.get)
		print str(i+1)+".\t"+maxTile+' '+str(all_tiles[maxTile])
		del all_tiles[maxTile]
	print "\nThe Users With the Most Tiles are:"
	for i in range(10):
		maxTiles = max(all_users, key=all_users.get)
		print str(i+1)+".\t"+maxTiles+"\t"+str(all_users[maxTiles])
		del all_users[maxTiles]
	f2.close()

	for i in all_users:
		all_users[i][0] = (int(all_users[i][0]) + 100)
        for i in all_users:
		if len(all_users[i]) > 1:
                        all_users[i][1] = (int(all_users[i][1]) + 1000)
                else:
                        all_users[i].append(1000)
        for k,v  in all_users.items():
                print k + " " + ' '.join(map(str, v))
