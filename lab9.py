# with open("lab9/notes.txt","r") as file:
#     for line in file:
#         print(line)


#read from your new file
with open("lab9/text.txt","r") as file:
    contents=file.read()
    print(contents)

#read your updated again and add two line
with open("lab9/text.txt","r") as file:
    for line in file:
        print(line)

txt_data = "I like pizza!"

file_path = "output.txt"

#read your update file again

with open("lab9/text.txt", "a") as file:
    file.write("\n")
    file.write("this should appear at the very end, cause we used  mode A")

#challenge: modify a previous program to have rither user input save to file 


text_data = {"name": "Patrick", "age": 20}
file_path = "output.txt"







    


