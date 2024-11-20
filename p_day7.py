import random
print(''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  ''')
stages=['''_______
     |/      |
     |      (_)
     |      / /
     |       |
     |      / /
     |
    _|___'''
    ,
    '''_______
     |/      |
     |      (_)
     |      / /
     |       |
     |      / 
     |
    _|___'''
    ,
    '''_______
     |/      |
     |      (_)
     |      / /
     |       |
     |      
     |
    _|___'''
    ,
    '''_______
     |/      |
     |      (_)
     |      / /
     |      
     |      
     |
    _|___'''
    ,
    '''_______
     |/      |
     |      (_)
     |        /
     |      
     |      
     |
    _|___'''
    ,
    '''_______
     |/      |
     |      (_)
     |        
     |       
     |      
     |
    _|___'''
    ,
    '''_______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___''']
word_list = ["aardavark", "baboon", "camel"]
chosen_word = random.choice(word_list)
placeholder = ""
word_len=len(chosen_word)
for i in range(word_len):
    placeholder += "_"
print(placeholder)
game_over=False
correct_letters=[]
life=6
while not game_over:
    
    user_guess = input("guess the word: ").lower()
    display = ""
    if user_guess in correct_letters:
        print(f"you already guess the letter {user_guess}")
        
    for letter in chosen_word:
        if (user_guess == letter):
            display += letter
            correct_letters.append(user_guess)
            
        elif letter in correct_letters:
            display+=letter
            
        else:
            display += "_"
        
    print(display)
    if user_guess not in chosen_word:
            life=life-1
            print(f"you guessed {user_guess} which is not in the word so. Remaining life are = {life}")
            if life==0:
                print("you lose")
                print(f"word was {chosen_word}")
                game_over=True
            
    print(stages[life])
            
    if "_" not in display:
        print("you win")
        game_over=True
    