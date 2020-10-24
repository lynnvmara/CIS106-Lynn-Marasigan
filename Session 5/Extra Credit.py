print("What is your last name?")
name = input()
print("How many hours?")
hours = int(input())
print("What is your rate per hour?")
rate = int(input())
if hours > 40:
  print(name + "'s regular pay for the first 40 hours is $" + str(rate) + " per hour for a total of $" + str(40 * rate) + ". The " + str(hours - 40) + " hours of overtime have an overtime pay of $" + str(rate * 1.5) + " per hour for a total of $" + str((hours - 40) * (rate * 1.5)) + ".")
  print(name + "'s gross pay is $" + str((40 * rate) + ((hours - 40) * (rate * 1.5))) + " for $" + str(rate) + " per hour over " + str(hours) + " hours.")
else:
  print(name + "'s regular pay is $" + str(rate) + " per hour for a total of $" + str(hours * rate) + ". " + name + " did not work any overtime, so " + name + " gets $0 for 0 hours of overtime.")
  print(name + "'s gross pay is $" + str(hours * rate) + " for $" + str(rate) + " per hour over " + str(hours) + " hours.")