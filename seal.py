import os
import stat
import shutil
import time
import GELL_actions
import preprocessor
import random

##action_dir = "/home/cg/palantir/w/submit/" #directory path where log files will be stored
action_dir = "/home/cg/palantir/w/submit/"
#action_dir = "/home/cg/palantir/wTest/submit/"#Test Directory
def main():
        print("Shared-DB server running")
	while True:   						#run the server indefinitely
		if there_is_file_in(action_dir):           		#if there are log files
			start_time = time.time()
			oldest_file, oldest_file_path, oldest_file_name = get_oldest_file_from(action_dir) #find the oldest
			action_list = oldest_file.readlines()
			print "Found File and Started Processing " + oldest_file_path
			print "AFTER PREPROCESSOR: " + str(len(action_list)) + " lines"			
			while action_list:				#take the oldest log file
				action = action_list.pop(0).split()
				action_len = len(action)
				i = 0  		                  #format its actions as lists		
				while (i < len(action)):
					if (action[i] == "x") or (action[i] == "."):
						popped = action.pop(i)
						action_len -= 1
					else: 
						i += 1				
				GELL_actions.execute(action)# executed each action,see GELL_Actions.py
			end_time = time.time()
			elapsed_time = end_time - start_time
			print("Completed Processing of " + oldest_file_path + " in " + str(elapsed_time) + " seconds.")
			oldest_file.close()## We Forgot to Add this Before
                	move_to_backup(oldest_file_path, oldest_file_name)

def there_is_file_in(dir): 
	there_is_txt = False
	files = os.listdir(dir)  		#func for checking for new log files
	for file in files:
		if os.access(dir+file, os.W_OK):
			return True
	return False


def get_oldest_file_from(dir):
	files = os.listdir(dir)
	oldest_file = ""
	oldest_file_mod_time = 9999999999999999999
	for file in files:
		file_mod_time = os.stat(action_dir + file).st_mtime
		if (file_mod_time < oldest_file_mod_time) and not (file[-1:] == "~"):
			oldest_file_mod_time = file_mod_time
			oldest_file_name = file
	fname = dir + oldest_file_name
	preprocessor.process(fname)
	f = open(fname, 'r+')
		
	return f,fname, oldest_file_name #returning file descriptor and file path

def move_to_backup(curr_file_path, file_name):
	folder_path = "/home/cg/palantir/SharedDB-Server/BackupLogs/" + time.strftime("%Y_%m_%d") + "/"
	if not os.path.exists(folder_path): 
		os.makedirs(folder_path)
		os.system("chmod 777 " + folder_path)
	if os.path.exists(folder_path + file_name):
		file_name += str(random.randint(0,100))
	os.rename(curr_file_path, (folder_path + file_name))



main()
