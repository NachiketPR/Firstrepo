# Python program to check
# if a string is palindrome
# or not

x = input("Enter the string  ")

w = ""
for i in x:
	w = i + w

if (x == w):
	print("Entered string is  a palindrome")
else:
	print("Entered string is not a palindrome")

