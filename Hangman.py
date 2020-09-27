import random

words = ["katelynn","is","ki","because","she","should","do","her","homework","word","cool","smart","stupid","kill","time","to","commit","arson","on","nothing"]

secretword = random.choice(words)

guessed = []
guessedwords = []
lives = 5
multiplayer = False
p1turn = True
p1score = 0
p2score = 0

def start():
    global multiplayer
    multiplayer = False
    start = input("(S)ingleplayer or (M)ultiplayer?").lower()
    if start == "s":
        startsingleplayer()
    elif start == "m":
        startmultiplayer()
    else:
        print("Invalid request. Please try again.")
        start()

def startsingleplayer():
    global lives
    dif = input("(B)aby, (E)asy, (M)edium, or (H)ard?").lower()
    if dif == "e":
        lives = 5
        restart()
    elif dif == "m":
        lives = 3
        restart()
    elif dif == "h":
        lives = 1
        restart()
    elif dif == "b":
        lives = 9999999
        print("If you somehow screw this up...")
        restart()
    else:
        print("Invalid request. Please try again.")
        startsingleplayer()

def startmultiplayer():
    global lives
    global multiplayer
    global p1turn
    global p1score
    global p2score
    p1turn = True
    multiplayer = True
    p1score = 0
    p2score = 0
    lives = 999999
    restart()
    
def restart():
    global secretword
    global guessed
    global guessedwords
    
    secretword = random.choice(words)
    guessed = []
    guessedwords = []
    print("\n\n")
    game()

def game():
    global secretword
    global guessedwords
    global guessed
    global lives
    global multiplayer
    global p1turn
    global p1score
    global p2score
    
    incomplete = False
    for character in secretword:
        if character in guessed:
            print(character,end = " ")
        else:
            print("_",end = " ")
            incomplete = True
            
    print("")
    if incomplete == False:
        print("You guessed every character! You win!")
        if multiplayer == True:
            print(f"Final score:\nPlayer 1: {p1score}\nPlayer 2: {p2score}\n")
        start()

    if multiplayer == True:
        if p1turn == True:
            print("Player 1's turn!")
            p1turn = False
        else:
            print("Player 2's turn!")
            p1turn = True
        
    guess = input("Guess a letter or a word. ").lower()
    print("")
    
    if guess in guessed:
        print("That has already been guessed!")
    elif len(guess) > 1 and guess in guessedwords:
        print("That has already been guessed!")
    else:
        if len(guess) == 1:
            if guess not in secretword:
                print("That letter is not in the word.")
                lives -= 1
            else:
                print("Correct!")
                if p1turn == False:
                    p1score += 1
                else:
                    p2score += 1
            guessed.append(str(guess))
            print("Letters Guessed:",end = " ")
            for x in range(len(guessed)):
                print(guessed[x],end = " ")
        else:
            guessedwords.append(str(guess))
            if guess == secretword:
                if p1turn == False:
                    p1score += 1
                else:
                    p2score += 1
                print("Correct! You win!")
                if multiplayer == True:
                    print(f"Final score:\nPlayer 1: {p1score}\nPlayer 2: {p2score}\n")
                start()
            else:
                print("That word is incorrect.")
                guessedwords.append(str(guess))
                lives -= 1

    if int(lives) == 0:
        print("")
        print("You ran out of lives!\nThe word was \"" +secretword+"\"")
        start()
    else:        
        print("")
        print("Lives remaining: "+str(lives))
    print("")
    game()
start()
