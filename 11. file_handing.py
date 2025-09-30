# # # Python provides built-in functions to handle files. File operations include:


# # # ***** ***** ***** 🔹 1. Opening a File: open() ***** ***** ***** 
# #                         # file = open("path\\filename", "mode")
# # # Common Modes:
# # # Mode	    Description
# # # 'r'	    Read (default mode). Error if file doesn't exist.
# # # 'w'	    Write. Creates a new file or truncates existing.
# # # 'a'	    Append. Adds content to the end of file.
# # # 'x'	    Create. Fails if file already exists.
# # # 'b'	    Binary mode. e.g., 'rb', 'wb'
# # # 't'	    Text mode (default). e.g., 'rt', 'wt'
# # # '+'	    Read and Write. e.g., 'r+', 'w+'



# ***** ***** ***** 🔹 2. Reading from a File ***** ***** ***** 
# ***** 1. a. read()      --> Reads the entire file or specified number of characters. 
f = open("Python\Python-for-Data-Science\data2.txt", "r")
# content = f.read()
# print(content)


# # ***** 2. b. readline()       --> Reads one line at a time.
# line = f.readline()
# line2 = f.readline()
# print(line)
# print(f.tell())
# print(line2)


# ***** 3. c. readlines()       --> Returns a list of all lines.
# lines = f.readlines()
# print(lines)









# # # ***** ***** ***** 🔹 3. Writing to a File ***** ***** ***** 
# # ***** a. write()          --> Writes a string to a file (Overwrite if text is there).  Create new file if not there and write
# f = open("C:\\Users\\maham\\OneDrive\\Documents\\DS Practice\\Python\\Python-for-Data-Science\data.txt", "w")
# f.write("Hello, World!\n")
# f.write('How are you\n')
# f.write("Hello, World!\n")
# f.write('How are you')
# f.write("Hello, World!")
# f.write('How are you')
# f.write("Hello, World!")
# f.write('How are you')
# f.write("Hello, World!")
# f.write('How are you')

# # f.close()


# # ***** b. writelines()     --> Writes a list of strings.
# lines = ["Line 1\n", "Line 2\n"]
# f.writelines(lines)


# # # ⚠️ Use 'a' mode to append instead of overwriting.




# # # ***** ***** ***** 🔹 4. Closing a File: close() ***** ***** ***** 
# # # Always close the file after use:
# # f.close()



# # # ***** ***** ***** 🔹 5. Using with Statement (Context Manager) ***** ***** ***** 
# # # Automatically handles closing:
# # with open("data.txt", "r") as f:
# #     data = f.read()


# # # ***** ***** ***** 🔹 6. File Object Methods ***** ***** ***** 
# # # Method	            Description
# # # .read([size])	        Reads file content
# # # .readline()	        Reads next line
# # # .readlines()	        Returns list of all lines
# # # .write(string)	    Writes string
# # # .writelines(list)	    Writes a list of strings
# # # .seek(offset)	        Moves cursor to offset
# # # .tell()	            Returns current position of cursor
# # # .close()	            Closes the file




# # # ***** ***** ***** 🔹 7. Working with Binary Files ***** ***** ***** 
# # with open("image.jpg", "rb") as f:
# #     data = f.read()

# # # To write binary:
# # with open("copy.jpg", "wb") as f:
# #     f.write(data)




# # # ***** ***** ***** 🔹 8. File Pointer – tell() and seek() ***** ***** ***** 
# # # tell()        → Returns current cursor position.
# # # seek(offset)  → Moves cursor to the specified byte.

# f = open("data.txt", "r")
# print(f.tell())      # 0
# f.read(5)
# print(f.tell())      # 5
# print(f.read())
# f.seek(0)            # Go back to start



# # # ***** ***** ***** 🔹 9. Check if File Exists ***** ***** ***** 
# # import os

# # if os.path.exists("data.txt"):
# #     print("File exists")
# # else:
# #     print("File does not exist")


# # # ***** ***** ***** 🔹 10. Deleting a File ***** ***** ***** 
# # import os
# # os.remove("data.txt")


# # # ***** ***** ***** 🔹 11. Other Useful os Functions ***** ***** ***** 
# # # os.rename("old.txt", "new.txt")
# # # os.mkdir("new_folder")          # Create folder
# # # os.rmdir("folder")              # Delete empty folder
# # # os.listdir()                    # List all files/folders in current directory


# # # ***** ***** ***** 🔹 12. Example: Read & Write ***** ***** ***** 
# # # Write to file
# # with open("hello.txt", "w") as f:
# #     f.write("Welcome to Python File Handling!")


# # # Read from file
# # with open("hello.txt", "r") as f:
# #     print(f.read())

