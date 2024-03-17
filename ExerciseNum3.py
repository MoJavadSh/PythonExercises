# # This file is or Exercises chapter3 and will name the exercises as the file in Ex_Program
#
# # Exercise 3-1-1 -----------------------------------------
# radius = int(input("Enter the radius of the circle: "))
# area = radius * radius * 3.14
# perimeter = 2 * 3.14 * radius

# print("The area is", area)
# print("The perimeter is", perimeter)

# # Exercise 3-1-2 -----------------------------------------
# number = int(input("Enter the Number "))
# square = number ** 2
# cube = number ** 3
# print("The square is", square)
# print("The cube is", cube)

# # Exercise 3-1-3 -----------------------------------------
# number = int(input("Enter x : "))
# number2 = int(input("Enter y : "))
# power = number ** number2
# print("x ^ y = ", power)

# # Exercise 3-1-4 -----------------------------------------
# number = int(input("Enter Number 1 : "))
# number2 = int(input("Enter Number 2 : "))
# number3 = int(input("Enter Number 3 : "))
# average = (number + number2 + number3)/3

# # Exercise 3-2-1 -----------------------------------------
# s = input("Enter String")
# print("number of all characters is: ", len(s))
# sentences = s.count(".") + s.count("?") + s.count("!") + s.count(";")
# print("Number of sentences is: ", sentences)
# print("Number of english letters is: ", s.count("a"))
# print("Number of words is: ", s.count(" ")+1 )

# Exercise 3-2-3 -----------------------------------------
s = input("Enter a number: ").strip()
print(s.isnumeric())

