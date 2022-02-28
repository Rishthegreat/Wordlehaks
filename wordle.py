import sys

from matplotlib.pyplot import text
global words
import random
import tkinter as tk

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

def keep(letter, index = -1):
  global words
  wordstemp = []
  for word in words:
    if (index != -1) & (word[index] == letter):
      wordstemp.append(word)
    elif (index == -1) & (letter in word):
      wordstemp.append(word)
  words = wordstemp

if __name__ == "__main__":
  args = sys.argv[1:]
  if len(args) <= 0:
    quit()
  if "-w" in args:
    clue = args[args.index("-w")+1]
    for x in range(0, len(clue)):
      character = clue[x]
      if character != '_':
        keep(character, x)
  if "-r" in args:
    lettersToRemove = []
    i = args.index("-r")+1
    while (i < len(args)):
      if '-' in args[i]:
        break
      lettersToRemove.append(args[i])
      i+=1
    for letter in lettersToRemove:
      rem(letter)
  if "-i" in args:
    lettersToKeep = []
    i = args.index("-i")+1
    while (i < len(args)):
      if '-' in args[i]:
        break
      lettersToKeep.append(args[i])
      i+=1
    for letter in lettersToKeep:
      keep(letter)
  if "-open" in args:
    root = tk.Tk()
    greeting = tk.Label(text="Wordle Haks")
    greeting.pack()
    root.mainloop()
  else:
    random.shuffle(words)
    print(words[0:20])
