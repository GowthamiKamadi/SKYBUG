#TASK 4:- ROCK-PAPER-SCISSOR GAME 🎱📃✂
while True:
    print("press",0,"for rock🎱")
    print("press",1,"for paper📃")
    print("press",2,"for scissor✂")
    #taking input from player
    player_input=int(input("enter number from 0-2: "))
    tools = ["rock🎱","paper📃","scissor✂"]
    #importing module called RANDOM
    import random
    computer_input=random.randint(0,2)
    print(tools[player_input],"selected by player")
    print(tools[computer_input],"selected by computer")
    #rock beats scissor, paper beats rock, scissor beats paper 
    if player_input==computer_input:
        print("got tie 😶no one wins‼😂")
    elif player_input==0 and computer_input==1:
        print("computer winner😶")
    elif player_input==1 and computer_input==0:
        print("player winner🎉")
    elif player_input==1 and computer_input==2:
        print("computer winner😶")
    elif player_input==2 and computer_input==1:
        print("player winner🎉")
    elif player_input==0 and computer_input==2:
        print("player winner🎉")
    elif player_input==2 and computer_input==0:
        print("computer winner😶")
    

    #asking computer's decision to quit or play
    print("\n")
    print("1)do you want to play again 💪")
    print("2)quit👋")
    selection = int(input("choose one option: "))
    if(selection == 2):
      break
