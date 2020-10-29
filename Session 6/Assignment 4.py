print("What is the term in years?")
term = int(input())
if term == 5 or term == 10:
  rate = 2
  print("The interest rate for a " + str(term) + " year term is " + str(rate) + "%.")
else:
  if term == 1 or term == 2 or term == 3:
    rate = 1
    print("The interest rate for a " + str(term) + " year term is " + str(rate) + "%.")
  else:
    rate = 0.5
    print("The interest rate for a " + str(term) + " year term is " + str(rate) + "%.")