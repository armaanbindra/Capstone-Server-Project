import sys
import os
workingRoot = "/home/cg/palantir/w"
#workingRoot = "/home/cg/palantir/wTest"
def repair(fname):
	f = open(fname,"r+")
	poly_lines = f.readlines()
	while poly_lines[len(poly_lines)-1]=="\n":	##deleting all blanks from end
		poly_lines.pop(len(poly_lines)-1)
	#print poly_lines
	
	first_line = poly_lines[0].split()
	nFaces = 0
	nVerts = 0
	#print "the length of first line is "+str(len(first_line))
	##print "fl[2] is "+first_line[4]
	try:
		if len(first_line) < 4:
			for i in range(1,len(poly_lines)):
				#print "working"
				if poly_lines[i][4]=='L' or poly_lines[i][4] == 'R':
					nFaces+=1
					#print "count++"
				else:
					nVerts+=1
		elif len(first_line) == 4:
			for i in range(1,len(poly_lines)):
				#print "working"
				if poly_lines[i][4]=='L' or poly_lines[i][4] == 'R':
					nFaces+=1
					#print "count++"
				else:
					nVerts+=1	

		
	except IndexError:
		print "Yup it is an index error again"
		print first_line
		print poly_lines
			
	poly_lines[0] = "Poly3 "+first_line[1]+" "+str(nVerts)+" "+str(nFaces)+"\n"##first_line[2]
	f.truncate()
	
	f.seek(0)
	for line in poly_lines:
		f.write(line)
	f.close()

def findandRepairPoly(poly3):
  #print '  ' + poly3
  path = workingRoot + '/t/' + poly3[0] + '/' + poly3[1] + '/' + poly3
  repair(path)

if os.path.exists(workingRoot + '/t'):
  for digit0 in os.listdir(workingRoot + '/t'):
    for digit1 in os.listdir(workingRoot + '/t/' + digit0):
      path = workingRoot + '/t/' + digit0 + '/' + digit1
      for poly3 in os.listdir(path):
				if poly3.endswith('.poly3'):
					findandRepairPoly(poly3)
