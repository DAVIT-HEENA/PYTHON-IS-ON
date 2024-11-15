import random
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""" 
figure=[rock,paper,scissors]
print("\nwelcome to the rock paper and scissores game\n ")
player_chooice=int(input("what do you want to choose \n1 for rock\n2 for paper\n3 for scissores\n"))
comp_choice=random.randint(1,3)
if(player_chooice==1): #1 for rock\n2 for paper\n3 for scissores\n
    print("YOU CHOOSE ROCK")
    print(figure[player_chooice-1])
    if(comp_choice==1):
        print("COMPUTER CHOOSE ROCK")
        print(figure[comp_choice-1])
        print("IT'S A TIE")
    if(comp_choice==2):
        print("COMPUTER CHOOSE PAPER")
        print(figure[comp_choice-1])
        print("YOU LOSE ")
    if(comp_choice==3):
        print("COMPUTER CHOOSE SCICCORES") 
        print(figure[comp_choice-1])
        print("YOU WIN")
                  
if(player_chooice==2):
    print("YOU CHOOSE PAPER")
    print(figure[player_chooice-1])#1 for rock\n2 for paper\n3 for scissores
    if(comp_choice==1):
        print("COMPUTER CHOOSE ROCK")
        print(figure[comp_choice-1])
        print("YOU WIN")
    if(comp_choice==2):
        print("COMPUTER CHOOSE PAPER")
        print(figure[comp_choice-1])
        print("IT'S A TIE ")
    if(comp_choice==3):
        print("COMPUTER CHOOSE SCICCORES")
        print(figure[comp_choice-1])
        print("YOU LOSE") 
   
if(player_chooice==3): #1 for rock\n2 for paper\n3 for scissores\n
    print("YOU CHOOSE SCICCORES")
    print(figure[player_chooice-1])
    if(comp_choice==1):
        print("COMPUTER CHOOSE ROCK")
        print(figure[comp_choice-1])
        print("YOU LOSE")
    if(comp_choice==2):
        print("COMPUTER CHOOSE PAPER")
        print(figure[comp_choice-1])
        print("YOU WIN")
    if(comp_choice==3):
        print("COMPUTER CHOOSE SCICCORES")
        print(figure[comp_choice-1])
        print("IT'S A TIE") 

else:
    print("MAKE A REAL CHOICE")
    