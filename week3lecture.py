#whats the difference between int and float
#int is whole number(10,2,5,6,67)
#float contain decimals (10,25,058,12,52)


x=15 #int value

y=2.5 #float

print(x)
print(y)

print(x,type(x))
print(y,type(y))

print(x//y) # floor division, will give whole number value 
print(x/y) #regular division, this will give float(decimal) value

user_text=input("Type something:") 
print("hello, {user_text}")

age=input("What is your age?:")#ask for age , makes input strin
print(age, type(age)) 

#strint is text data
#message = CISW 125
#print(message, type(message))

word="python"
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[5])

#slicing is when we want to print a range from string text
print(word[0:3])
# start:ends means start at and stop before end 

#buil in python function
#upper(), this converts string to all UPPER CASE
#lower(), this converts string to all LOWER CASE

fruits=["apple", "banana","oranges"]
numbers=[10,2,3,5,]
mixed=[100,"score",3.5]
print(fruits[0])
print(fruits[0:2]) #this prints my first 2 items
#to add to a list, we append the list name

