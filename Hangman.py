import random

words = ["katelynn","is","ki","because","she","should","do","her","homework"]

secretword = random.choice(words)

guessed = []
guessedwords = []
incomplete = False
lives = 5

def restart():
    global secretword
    global guessed
    global guessedwords
    global lives
    
    secretword = random.choice(words)
    guessed = []
    guessedwords = []
    lives = 5
    print("\n\n")

while True:
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
        restart()
        
    guess = input("Guess a letter or a word. ").lower()
    print("")
    
    if guess in guessed:
        print("You already guessed that!")
    elif len(guess) > 1 and guess in guessedwords:
        print("You already guessed that!")
    else:
        if len(guess) == 1:
            if guess not in secretword:
                print("That letter is not in the word.")
                lives -= 1
            guessed.append(str(guess))
            print("Letters Guessed:",end = " ")
            for x in range(len(guessed)):
                print(guessed[x],end = " ")
        else:
            guessedwords.append(str(guess))
            if guess == secretword:
                print("Correct! You win!")
                restart()
            else:
                print("That word is incorrect.")
                guessedwords.append(str(guess))
                lives -= 1

    if int(lives) == 0:
        print("")
        print("You ran out of lives!\nThe word was \"" +secretword+"\"")
        restart()
    else:
        if len(guessed) == 0 and len(guessedwords) == 0:
            continue
        else:
            print("")
            print("Lives remaining: "+str(lives))
    print("")
    
