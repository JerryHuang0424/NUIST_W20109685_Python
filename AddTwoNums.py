# Add Two Numbers in Python
# Author : Jerry Huang
# Using a function

# function a add two numbers
def add(a,b):
	result = float(a) + float(b)
	return result

#taking user input
a = input("First Number:")
b = input("Second Number:")

#Calling function
res = add(a,b)
print("The Answer is:")
print(res)
