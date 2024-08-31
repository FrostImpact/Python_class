file1 = open("fileio", "r") #r  is for reading a file
str1 = file1.read() #read just prints whats in a file
print(str1)
file1.close()

file2 = open("fileio", "a") #a is for append
file2.write("More Text") #adds stuff to a file, cant remove anything that already exists
file2.close()

file3 = open("fileio", "r")
print(file3.read())
file3.close()

file4 = open("fileio", "w") #w is for write
file4.write("No more text") #overrides everything in a file with whats in the bracket
file4.close()

file5 = open("fileio", "r")
print(file5.read())
file5.close()