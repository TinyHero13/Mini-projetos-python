import random, sys

def rock(playerAnswer):
    game = ["rock", "paper", "scissors"]
    computerAnswer = game[random.randint(0,2)]
    
    if playerAnswer == computerAnswer:
        print("Computer: {}, You: {}.\n It's a tie!".format(computerAnswer,playerAnswer))

    elif playerAnswer == "paper":
        if computerAnswer == "rock":
            print("Computer: {}, You: {}.\n You won!".format(computerAnswer,playerAnswer))

        else:
            print("Computer: {}, You: {}.\n You lose!".format(computerAnswer,playerAnswer))

    elif playerAnswer == "scissors":
        if computerAnswer == "paper":
            print("Computer: {}, You: {}.\n You won!".format(computerAnswer,playerAnswer))

        else:
            print("Computer: {}, You: {}.\n You lose!".format(computerAnswer,playerAnswer))

    elif playerAnswer == "rock":
        if computerAnswer == "scissors":
            print("Computer: {}, You: {}.\n You won!".format(computerAnswer,playerAnswer))

        else:
            print("Computer: {}, You: {}.\n You lose!".format(computerAnswer,playerAnswer))

    else: 
        print("Wrong input! ")
        

def initGame():
    while True:
        validation = input("Let's play rock, paper and scissors? Y/N ").lower()
        if validation == "y":
            answer = input("Rock, paper or scissors? ").lower()
            
            rock(answer)
        
        elif validation == "n":
            sys.exit()

        else:
            print("Wrong input. Try again!\n")


initGame()