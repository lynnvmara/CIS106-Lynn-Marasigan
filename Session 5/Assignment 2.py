print("Is the widget A or B?")
widget = input()
if widget == "A":
  price = 10
  widget = "A"
  print("The price per widget is $10.00.")
else:
  price = 20
  widget = "B"
  print("The price per widget is $20.00.")
print("How many widgets?")
quantity = int(input())
print("The extended price for " + str(quantity) + " units of widget " + widget + " costing $" + str(price) + " each is $" + str(quantity * price) + ".")