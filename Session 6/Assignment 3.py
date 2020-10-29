def lastName():
  print("What is your last name?")
  name = input()

  return name

def jobCode():
  print("What is your job code?")
  code = input()

  return code

def serviceYears():
  print("How many years of service?")
  years = int(input())
  
  return years

name = lastName()
code = jobCode()
years = serviceYears()
if code == "A":
  if years > 10:
    bonus = 10000
    print(name + "'s employee bonus is $" + str(bonus) + ".")
  else:
    if years >= 5:
      bonus = 8000
      print(name + "'s employee bonus is $" + str(bonus) + ".")
    else:
      bonus = 5000
      print(name + "'s employee bonus is $" + str(bonus) + ".")
else:
  if years > 15 and code == "B":
    bonus = 9000
    print(name + "'s employee bonus is $" + str(bonus) + ".")
  else:
    bonus = 5000
    print(name + "'s employee bonus is $" + str(bonus) + ".")
