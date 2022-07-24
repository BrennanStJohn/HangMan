import random

f = open("text/wordlist.txt", 'r')

file = open("text/wordlist.txt").read().split()

wordlist = []

for word in range(len(file)):
  wordlist += file

word = wordlist[random.randint(0, len(wordlist)-1)]

blanks = len(word)

guessWord = []

for _ in range(blanks):
  guessWord += "_"

  
hang = ["""    _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___\n\n""" ,
"""    _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /
     |
    _|___\n\n""" ,
        """    _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___\n\n""",
"""    _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___\n\n""" ,
"""    _______
     |/      |
     |      (_)
     |      \|
     |       
     |      
     |
    _|___\n\n""",
"""    _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___\n\n""",
"""     _______
     |/      
     |     
     |     
     |       
     |      
     |
    _|___\n\n"""]

print("Welcome to HangMan!\n")

lives = 6

endGame = False

while("_" in guessWord):
  
  print(hang[lives])

  print("".join(guessWord))

  guess = input("\nGuess a letter: ").lower()
  
  for _ in range(blanks):
    letter = word[_]
    if letter == guess:
      guessWord[_] = letter
  if guess not in word:
    lives -= 1
    if lives == 0:
      endGame = True
      break
      
if endGame == True:
  print(hang[0])
  print("You lose!")
elif endGame == False:
  print("\nYou win!")

f.close()