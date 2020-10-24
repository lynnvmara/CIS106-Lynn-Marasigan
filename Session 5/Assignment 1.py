def itemQuantity():
  print("How many items were ordered?")
  quantity = int(input())

  return quantity

def itemPrice():
  print("What is the unit price (price per item)?")
  price = int(input())

  return price

def computeTax(total):
  print("The extended price is $" + str(total) + ". The extended price plus a 7% tax is $" + str(total * 1.07) + ".")
  if total >= 100:
    print("This order has a shipping fee of $0. The total cost for " + str(quantity) + " items for $" + str(price) + " each is $" + str(total * 10.7) + ".")
  else:
    print("This order has a shipping fee of $" + str(total * 0.10) + " which is 10% of the cost before tax. The total cost for " + str(quantity) + " items for $" + str(price) + " each is $" + str(total + (total * 0.07) + (total * 0.10)) + ".")

quantity = itemQuantity()
price = itemPrice()
total = quantity * price
computeTax(total)