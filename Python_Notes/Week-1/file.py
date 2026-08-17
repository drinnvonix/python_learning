# File handling

# open() key function for working with file, takes two parameter (filename, mode)

# Four different mode for opening a file:
    # "r" : Read - default value, Open a file for reading, error if file not exist.
    # "a" : Append - Open a file for appending, create file if not exist.
    # "w" : Write - Open a file for writing, create file is not exist.
    # "x" : Create - Create the specifed file, reutrns error if file not exist.

    # In addition file should be handled as binary(image) or text mode(default value).

f = open("demofile.txt", "rt")

f = open("D:\\myfiles\welcome.txt") # Open file from a specifed location
print(f.read())

# can also use with keyword
with open("demofile.txt") as f:
  print(f.read())

f.close()   # to close a file

print(f.read(5))    # returns whole text, can also specify how many characters
print(f.readline()) # to read single line from the file

with open("demofile.txt") as f:
  for x in f:   # used to read file, line by line
    print(x)

with open("demofile.txt", "a") as f:
  f.write("Now the file has more content!") # append text into the file

with open("demofile.txt") as f:
  print(f.read())

with open("demofile.txt", "w") as f:    # override the data of file
  f.write("Woops! I have deleted the content!")

f = open("myfile.txt", "x") # create new file

import os
os.remove("demofile.txt")   # delete a file

import os
if os.path.exists("demofile.txt"):  # checks if file exist
  os.remove("demofile.txt")
else:
  print("The file does not exist")

import os
os.rmdir("myfolder")    # delete an entire folder