import os

f = open("/home/cg/palantir/w/1/1/3/1132L.imgInfo",'r')
img_lines = f.readlines()
f.close()
tile_list = []
for i in range(2,len(img_lines)):
	ls = img_lines[i].split()
	if not ls[1]== 0:
		tile_list.append(ls[0]+"\n")
f2 = open("maggie_list",'w')
for line in tile_list:
	f2.write(line)
	 
f2.close()
