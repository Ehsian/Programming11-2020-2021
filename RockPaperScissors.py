import random
import time
def game():
  player = input("Choose: rock, paper, or scissors.").lower() #.lower() makes the letters in the input lowercase
  if(player == "rock"):
    player = 1
  elif(player == "paper"):
    player = 2
  elif(player == "scissors"):
    player = 3
  global bot
  bot = (random.randrange(1, 3))
  if (player == bot):
      draw()
  elif (bot == 1) and (player == 2):
      win()
  elif (bot == 2) and (player == 3):
      win()
  elif (bot == 3) and (player == 1):
      win()
  elif (bot == 1) and (player == 3):
      loss()
  elif (bot == 2) and (player == 1):
      loss()
  elif (bot == 3) and (player == 2):
      loss()
  else:
      print("That is invalid, please choose again")
      game()

def loss():
    global bot
    print("Sorry you lost,")
    if(str(bot) == "1"):
        bot = "rock"
    elif(str(bot) == "2"):
        bot = "paper"
    elif(str(bot) == "3"):
        bot = "scissors"
    print("The computer got " + str(bot))
    time.sleep(3)
    game()
def win():
    global bot
    print("Good job you won")
    if(str(bot) == "1"):
        bot = "rock"
    elif(str(bot) == "2"):
        bot = "paper"
    elif(str(bot) == "3"):
        bot = "scissors"
    print("The computer got " +str(bot))
    time.sleep(3)
    game()
def draw():
    global bot
    print("Drawn game.")
    if(str(bot) == "1"):
        bot = "rock"
    elif(str(bot) == "2"):
        bot = "paper"
    elif(str(bot) == "3"):
        bot = "scissors"
    print("The computer got " + str(bot))
    time.sleep(3)
    game()
game()

