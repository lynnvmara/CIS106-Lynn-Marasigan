def inputValues(indexes, index):
  for index in range(0, indexes):
    print("Enter value" + str(index + 1) + ":")
    value = input()
    list.append(value)

def outputValues(indexes, index):
  for index in range(0, indexes):
    print(list[index])

list = []
print("How many values?")
index = 0
indexes = int(input())
inputValues(indexes, index)
outputValues(indexes, index)