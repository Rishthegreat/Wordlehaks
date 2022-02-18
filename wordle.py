with open('words.txt') as f:
  words = f.readlines()

for i in range (0, len(words)):
  words[i] = words[i][:-1]
  words[i] = words[i].lower()

