import os, sys


#print os.getcwd()
#print os.path.files
#os.open(files)
#print os.getcwd()
#os.chdir(home/kathryn/week_1_project/Week_1_Project/files)

# Create a new dir for each letter of the alphabet
 directories = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
 directories = directories.split(' ')


for entry in directories:
	#how can we use os.chdir(path) to set these all up in 'files'?
	os.mkdir(./)

# Loop through files in original_files, sort each file into 
# appropriate directory (based on 1st letter)

# Set a list that contains all the (unzipped) files
# Currently returning OSError 2 - no such file or dir

file_list = os.listdir("files")

# Check if firstletter == alphabet letter and if so
# move file to appropriate directory

# create list of alphabet to iterate through
alph = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alph = alph.split(' ')

#file_list = "file.txt alpha.txt beta.txt  annabel.txt carrots.txt"
#file_list = file_list.split(' ')

for item in file_list:
	for letter in alph:
		# if filename starts with (iterate through alphabet)
		if item.startswith(letter):
			shutil.move(files, letter)
			# if path already exists, move file to existing path
			if os.path.exists(letter):
				os.chdir(letter) 
		else:
			continue
