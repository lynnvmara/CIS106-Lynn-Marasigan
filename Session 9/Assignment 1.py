def displayArray(name):
  for offset in range(0, 9 + 1, 1):
    print(name[offset])

def displayBack(name):
  for offset in range(9, 0 - 1, -1):
    print(name[offset])

name = [""] * (10)

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
displayArray(name)
displayBack(name)