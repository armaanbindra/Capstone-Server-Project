##import sys
actions = ["addFiber","removeFiber","addFeature","removeFeature","addPin","removePin","setFeaturePoint","setCornerPt", "setPoly3","setNoPoly3","setName"]
def process(fname):
	poly3_dic = {}
	f = open(fname,"r+")
	ls = f.readlines()
	print("BEFORE PREPROCESSOR: " + str(len(ls)) + " lines")
	new_ls = []
	fin_ls = []
	for line in ls:
	    temp = line.split()
            if len(temp) == 0:
                continue
	    elif temp[0] in actions:
		new_ls.append(line)
	new_ls.append("last line")
	fname2 = fname+"_p"
	temp_str = ""
	for i in range(len(new_ls)):
	    temp = new_ls[i].split()
	    if temp[0] == "last":
		break
	    elif temp[0]=="addFiber":
		orig = temp[:8]        
		temp = temp[8:]
		orig_str = orig[0]
		for arg in range(1,len(orig)):
		    orig_str+=" "+orig[arg]
		for j in range(len(temp)):
		    temp_str += " " + temp[j]
		checkNext = new_ls[i+1].split()
		if not checkNext[:8] == orig:
		    temp_str = orig_str + " " + temp_str + '\n'
		    fin_ls.append(temp_str)
		    temp_str = ""
	    elif temp[0]=="removeFiber":
		orig = temp[:8]        
		temp = temp[8:]
		orig_str = orig[0]
		for arg in range(1,len(orig)):
		    orig_str+=" "+orig[arg]
		for j in range(len(temp)):
		    temp_str += " " + temp[j]
		checkNext = new_ls[i+1].split()
		if not checkNext[:8] == orig:
		    temp_str = orig_str + " " + temp_str + '\n'
		    fin_ls.append(temp_str)
		    temp_str = ""
	    elif temp[0]=="setPoly3":
		orig = temp[:4]        
		temp = temp[4:]
		temp2_str = ""
		orig_str = orig[0]
		for arg in range(1,len(orig)):
		    orig_str+=" "+orig[arg]
		for j in range(len(temp)):
		    temp2_str += " " + temp[j]
		poly3_dic[orig_str] = temp2_str
	    else:
		fin_ls.append(new_ls[i])
		
	for key in poly3_dic:
		poly_action_str = key + poly3_dic[key] + "\n"
		fin_ls.append(poly_action_str)
	#print poly3_dic	
	f.seek(0)
	f.truncate()
	for line in fin_ls:
	    f.write(line)
	f.close()
