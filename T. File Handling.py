# Write file

file_write = open("FileHandling.txt", "w")
file_write.write("Test write file\n")
file_write.close()

# Append to the end of file
file_append = open("FileHandling.txt","a")
file_append.write("Test append")
file_append.close()

# Read file
file_read = open("FileHandling.txt","r")
print(file_read.read())

# Delete file
# import os
# os.remove("FileHandling.txt")