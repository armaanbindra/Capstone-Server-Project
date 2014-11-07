import sys
import os

workingRoot = "/home/cg/palantir/w"

def repair(fname):
	f = open(fname,"r+")
	corner_lines = f.readlines()
	line_3=corner_lines[2].split()
	if len(line_3)>1:
		##print line_3
		line_3 = list(set(line_3))
		##print line_3
		newLine3 = ""
		for i in line_3:
			newLine3+=i+" "
		##print newLine3
		newLine3 += "\n"
		corner_lines[2] = newLine3
	f.seek(0)
	f.truncate()	
	for line in corner_lines:
		f.write(line)
	f.close()


def findandRepairCorner(corner):
  path = workingRoot + '/c/' + corner[0] + '/' + corner[1] + '/' + corner[2]+'/'+corner
  repair(path)

nCorners = 0
if os.path.exists(workingRoot + '/c'):
  # for digit0 in os.listdir(workingRoot + '/c'):
  for digit0 in ['1','2']:##remember to add more digits here
    for digit1 in os.listdir(workingRoot + '/c/' + digit0):
      for digit2 in os.listdir(workingRoot + '/c/' + digit0 + '/' + digit1):
        path = workingRoot + '/c/' + digit0 + '/' + digit1 + '/' + digit2
        for corner in os.listdir(path):
          nCorners += 1
          findandRepairCorner(corner)

