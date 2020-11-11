def startAmount():
  print("What is the starting amount you will invest into the CD?")
  start = int(input())

  return start

def interestRate():
  print("What is the interest rate of the CD? Enter in percentage.")
  rate = int(input())

  return rate

def termYears():
  print("How long is the term in years?")
  years = int(input())

  return years

def forLoop(start, rate, years, count):
  for count in range(1, years + 1, 1):
    print("For year " + str(count) + ", the starting amount is $" + str(start) + " and the interest for this year is $" + str(start * (rate / 100)) + " for a total of $" + str(start + (start * (rate / 100))) + ".")
    start = start + (start * (rate / 100))

start = startAmount()
rate = interestRate()
years = termYears()
count = 1
forLoop(start, rate, years, count)