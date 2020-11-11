number1 = 0
number2 = 1
print(str(number1))
print(str(number2))
for count in range(1, 8 + 1, 1):
  fibonacci = number1 + number2
  print(str(fibonacci))
  number1 = number2
  number2 = fibonacci