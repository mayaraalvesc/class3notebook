print("Hello! Give me a number")
num = input()

if num == "42":
   print("Right answer to everything!")
elif not num.isdigit():
   print("Sorry, invalid input, expecting number.")
elif num != "42":
   print("Wrong answer!")
