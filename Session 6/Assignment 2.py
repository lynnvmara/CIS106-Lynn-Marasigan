print("How many items were ordered?")
quantity = int(input())
if quantity > 1000:
  price = 8
  print("The cost per item is $" + str(price) + ". For " + str(quantity) + " items, the extended price is $" + str(quantity * price) + ".")
else:
  if quantity >= 500:
    price = 10
    print("The cost per item is $" + str(price) + ". For " + str(quantity) + " items, the extended price is $" + str(quantity * price) + ".")
  else:
    price = 12
    print("The cost per item is $" + str(price) + ". For " + str(quantity) + " items, the extended price is $" + str(quantity * price) + ".")