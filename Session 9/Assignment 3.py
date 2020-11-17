def displayHigh(name, score):
  h = 0
  for offset in range(0, 9 + 1, 1):
    if score[offset] > h:
      h = score[offset]
      high = offset
  print("The highest score is a " + str(score[high]) + "% from " + name[high] + ".")

def displayLow(name, score):
  l = 999
  for offset in range(0, 9 + 1, 1):
    if score[offset] < l:
      l = score[offset]
      low = offset
  print("The highest score is a " + str(score[low]) + "% from " + name[low] + ".")

def displayAverage(name, score):
  total = 0
  for offset in range(0, 9 + 1, 1):
    total = total + score[offset]
  average = total / 10
  print("The average score in a class of 10 students is " + str(average) + "%.")
name = [""] * (10)
score = [""] * (10)

name[0] = "Marasigan"
name[1] = "Garcia"
name[2] = "Hamilton"
name[3] = "Niemiec"
name[4] = "Klem"
name[5] = "Weiss"
name[6] = "Meyers"
name[7] = "Sheridan"
name[8] = "Schafernak"
name[9] = "Joyce"
score[0] = 100
score[1] = 90
score[2] = 80
score[3] = 70
score[4] = 60
score[5] = 50
score[6] = 40
score[7] = 30
score[8] = 20
score[9] = 10
displayHigh(name, score)
displayLow(name, score)
displayAverage(name, score)