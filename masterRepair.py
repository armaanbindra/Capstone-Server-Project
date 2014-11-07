import sys
import os

f = open("165wray",'r+')
tile_lines = f.readlines()
cornerID_list = tile_lines[1].split()
temp = ""
popped = []
new_tile_lines = []
for i in range(2,len(tile_lines)):
	if not temp == tile_lines[i].split[0][:-1]:
		popped.append(i)
	else:
		temp = tile_lines[i].split[0][:-1]

for i in range(2,len(tile_lines)):
	if i not in popped:
		new_tile_lines.append(tile_lines[i])

f.seek(0)
f.truncate()

for line in new_tile_lines:
	f.write(line)
f.close()
