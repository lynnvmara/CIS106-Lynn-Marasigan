print ("What is your last name?")
name = input()
print ("What is the first exam score?")
score1 = int(input())
print ("What is the second exam score?")
score2 = int(input())
print (name + "'s total score, with a first exam score of " + str(score1) + " worth 40% and a second exam score of " + str(score2) + " worth 60%, is " + str(score1 * .4 + score2 * .6) + "%.")