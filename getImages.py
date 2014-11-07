import os
import sys
workingRoot = "/home/cg/palantir/w/"

def getImagePath(path):
    path = "/home/cg/palantir/w/"+path[0]+"/"+path[1]+"/"+path[2]+"/"+path
    return path

print("started")

if os.path.exists(workingRoot):
  for digit0 in ['0', '1','2','3','4']:
    for digit1 in os.listdir(workingRoot + '/' + digit0):
      for digit2 in os.listdir(workingRoot + '/' + digit0 + '/' + digit1):
        path = workingRoot + '/' + digit0 + '/' + digit1 + '/' + digit2
        for fname in os.listdir(path):
        	if fname.endswith(".ppm"):
        		command = "cp "+getImagePath(fname)+" /home/cg/palantir/SharedDB-Server/images"
        		os.system(command)

print("done")