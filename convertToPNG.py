import os

print("started")
for fname in os.listdir("images"):
	#command = "convert images/"+fname+" images/"+fname[0:-3]+"png"
	command = "convert images/"+fname[0:-3]+"ppm images/"+fname[0:-3]+"png"
	command2 = "rm images/"+fname[0:-3]+"ppm"
	if not os.path.exists("images/"+fname[0:-3]+"png"):
		os.system(command)
		print command
		os.system(command2)
		print command2
print("done")