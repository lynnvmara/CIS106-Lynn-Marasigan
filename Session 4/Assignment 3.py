def ticketQuantity():
  print ("How many tickets?")
  ticketQuantity = int(input())

  return ticketQuantity

def ticketCost():
  print ("What is the cost per ticket?")
  ticketCost = int(input())

  return ticketCost

def computeTax(total):
    print ("For " + str(quantity) + " tickets worth $" + str(cost) + " each, the total is $" + str(total) + "." + " With a 7% tax, the new total is $" + str(total * 1.07) + ".")

quantity = ticketQuantity()
cost = ticketCost()
total = quantity * cost
computeTax(total)