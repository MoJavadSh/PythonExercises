from datetime import date

# Exercise 1
x = 5
y = 3
print(x, y)
x, y = y, x
print(x, y)

# Exercise 2
x = 6
y = 8
print('area =', x*y)
print('perimeter =', (x+y)*2)

# Exercise 3
Temperature = 1
print((Temperature * 1.8) + 32)

# Exercise 4
Radius = 6
print(Radius)
print("perimeter =", 2*Radius*3.14)
print("area =", 3.14*Radius**2)

# Exercise 5
FirstNum = 19
SecondNum = 5
Sum = FirstNum + SecondNum
difference = FirstNum - SecondNum
multiplication = FirstNum * SecondNum
division = FirstNum / SecondNum
print(Sum, difference, multiplication, division)

# Exercise 6
x = 89
y = 57
z = 45
average = (x + y + z) / 3
print('Average of', x,',', y,',', z, '=', average)

# Exercise 7
base = 6
height = 19
area = (base * height) / 2
print('Area =', area)

# Exercise 8
age = 21
yearOfBirth = date.today().year - age
print(yearOfBirth)
print('Year of 100 Years-Old Birth is ', yearOfBirth + 100)
