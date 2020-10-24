print("What is your last name?")
name = input()
print("How many hours?")
hours = int(input())
print("What is your rate per hour?")
rate = int(input())
if hours > 40:
  print(name + "'s gross pay is $" + str((40 * rate) + ((hours - 40) * (rate * 1.5))) + " for $" + str(rate) + " per hour over " + str(hours) + " hours.")
else:
  print(name + "'s gross pay is $" + str(hours * rate) + " for $" + str(rate) + " per hour over " + str(hours) + " hours.")