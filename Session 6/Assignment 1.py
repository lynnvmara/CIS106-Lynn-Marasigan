print("How many years of service?")
years = int(input())
if years > 10:
  print("Service level award: 1,000")
else:
  if years >= 5:
    print("Service leve award: 500")
  else:
    print("Service level award: 100")