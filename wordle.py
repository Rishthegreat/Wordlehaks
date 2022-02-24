with open('words.txt') as f:
  words = f.readlines()

for i in range (0, len(words)):
  words[i] = words[i][:-1]
  words[i] = words[i].lower()

for i in range (0, len(words)):
  if len(words[i]) > 5:
    words.pop(i)
print(words[0:20])
