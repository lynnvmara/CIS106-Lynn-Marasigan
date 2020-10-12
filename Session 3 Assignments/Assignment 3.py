def itemQuantity():
  print ("How many items?")
  itemQuantity = int(input())

  return itemQuantity

def itemPrice():
  print ("How much per item?")
  itemPrice = int(input())

  return itemPrice

def computeTax(total):
  quantity = itemQuantity()
  price = itemPrice()
  print ("The total after %7 sales tax is $" + str(total * 1.07) + " for " + str(quantity) + " items for $" + str(price) + " each item.")

quantity = itemQuantity()
price = itemPrice()
total = quantity * price
print ("The total cost is $" + str(total) + ".")
computeTax(total)