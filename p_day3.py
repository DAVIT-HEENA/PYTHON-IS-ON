print('''

                            .=""_;=._
                       ,-"_,=""     `"=._
                       "=._o`"-._        `"=._
                           `"=._o`"=._      _`"=._                     
                                :=._o "=._."_.-="'"=..
                        __.--" , ; `"=._o." ,-"""-._ ".   
                      ._"  ,. .` ` `` ,  `"-._"-._   ". '
                      |o`"=._` , "` `; .". ,  "-._"-._; ;              
                      | ;`-.o`"=._; ." ` '`."\` . "-._ /
                      |o;    `"-.o`"=._``  '` " ,__.--o;   
                      | ;     (#) `-.o `"=.`_.--"_o.-; ;
                      | o;._    "      `".o|o_.--"    ;o;
                        "=._o--._        ; | ;        ; ; 
                             "=._o--._   ;o|o;     _._;o;
                               "=._o._; | ;_.--"o.--"
                                      "=.o|o_.--""

''')
print("welcome to the treasure island")
print("your mission is to find the treasure")
direction=input("where do you want to go ? 'left' to LEFT  'right' to RIGHT\n").lower()
if(direction=="left" ):
    lake=input("you came across a lake ! \ndo you wan to swim or wait for the boat ? 'swim' to SWIM AND GO 'wait' to WAIT FOR THE BOAT\n" ).lower()
    if(lake=="wait" ):
        door=input("you came to an island \nThere are three doors red yellow and blue \nchoose a door 'red' for RED 'yellow' for YELLOW 'blue' for BLUE \n").lower()
        if(door=="yellow" ):
            print ("TREASURE FOUND  \n YOU WON ")
        else:
            print("DOOR HAS FLAMES \n GAME OVER ")
    else:
        print("CROCODILE ARE THERE \n GAME OVER ")
if(direction=="right" ):
    print("ROAD CLOSED \n GAME OVER ")
else:
    print("PLEASE CHOOSE CORRECT OPTION ")