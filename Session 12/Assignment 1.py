def displayHigh(name, score):
  h = 0
  for offset in range(0, 5 + 1, 1):
    if int(score[offset]) > h:
      h = int(score[offset])
      high = offset
  print("The highest score is a " + str(score[high]) + "% from " + name[high] + ".")

def displayLow(name, score):
  l = 999
  for offset in range(0, 5 + 1, 1):
    if int(score[offset]) < l:
      l = int(score[offset])
      low = offset
  print("The highest score is a " + str(score[low]) + "% from " + name[low] + ".")

def displayAverage(name, score):
  total = 0
  for offset in range(0, 5 + 1, 1):
    total = total + int(score[offset])
  average = total / 10
  print("The average score in a class of 6 students is " + str(average) + "%.")
name = [""] * (10)
score = [""] * (10)

name[0] = "Marasigan"

scores = open("scores.txt", "r")
file = scores.read()
text = file.splitlines()
name = [""] * 6
score = [""] * 6
name[0],score[0] = text[0].split(",")
name[1],score[1] = text[1].split(",")
name[2],score[2] = text[2].split(",")
name[3],score[3] = text[3].split(",")
name[4],score[4] = text[4].split(",")
name[5],score[5] = text[5].split(",")
displayHigh(name, score)
displayLow(name, score)
displayAverage(name, score)
scores.close()