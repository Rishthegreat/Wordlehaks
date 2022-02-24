import sys
global words

with open('words.txt') as f:
  global words
  words = f.readlines()

for i in range (0, len(words)):
  words[i] = words[i][:-1]
  words[i] = words[i].lower()

wordstemp = []
for word in words:
  if (len(word) == 5) & word.isalpha():
    wordstemp.append(word)
words = wordstemp

def remKeep(letter, index = -1):
  global words
  wordstemp = []
  for word in words:
    if (index == -1) & (letter not in word):
      wordstemp.append(word)
    elif word[index] == letter:
      wordstemp.append(words)
  words = wordstemp

if __name__ == "__main__":
  args = sys.argv[1:]
  if len(args) <= 0:
    print(words[0])
    quit()
  if "-w" in args:
    clue = args[args.index("-w")+1]
    for x in range(0, len(clue)):
      character = clue[x]
      if character != '_':
        remKeep(character, x)
  if "-r" in args:
    lettersToRemove = []
    i = 1
    while (i < len(args)):
      if '-' in args[i]:
        break
      lettersToRemove.append(args[i])
      i+=1
    for letter in lettersToRemove:
      remKeep(letter)
  print(words[0])
