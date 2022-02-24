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

def rem(letter):
  global words
  wordstemp = []
  for word in words:
    if letter not in word:
      wordstemp.append(word)
  words = wordstemp

if __name__ == "__main__":
  args = sys.argv[1:]
  if len(args) <= 0:
    print(words[0].isalpha())
  elif args[0] == "-w":
    given = args[1]
  elif args[0] == "-r":
    lettersToRemove = []
    i = 1
    print(len(args))
    while ((i < len(args)) & ('-' not in args[i])):
      lettersToRemove.append(args[i])
      i+=1    
