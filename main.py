#region Import

# Used for the algorithmy
import time
import random

#endregion



#region Variables

# Score
patern = []
best_score = 0
score = 0
init_chain = 5
chain = 0

# Lists
btn_list = ['A', 'B', 'C', 'D', 'E']

#endregion



#region Start()

def start_game():
    global score, best_score, patern, chain, init_chain, btn_list
    # Check the score
    if score > best_score:
        best_score = score

    # Show the starting menu
    print('Best Score : ' + str(best_score))
    print('Last Score : ' + str(score))
    print('Press any button to START!')

    # Reset the variable
    patern = []
    score = 0
    chain = init_chain

    # Ask for difficulty
    difficulty()

    # Start the game when a button is pressed
    input("Press Enter to start...")
    light_patern(chain, btn_list)

#endregion



#region Light()

def light_patern(chain, btn_list):
    global patern
    patern = []  # Reset the pattern for the new game
    for x in range(chain):
        # Define a led
        led_r = random.randrange(0, len(btn_list))
        # Save this led in a list
        patern.append(led_r)
        # Show the led
        print(f"LED {btn_list[led_r]} is ON")
        time.sleep(0.5)
        print(f"LED {btn_list[led_r]} is OFF")
        time.sleep(0.75)
    # Next step of the game
    check_patern(patern, btn_list)

#endregion

def difficulty():
    global init_chain
    difficulty_question = input("Do you want to change the difficulty? (Y/N): ").upper()
    if difficulty_question == "Y":
        init_chain = int(input("Enter the new difficulty (number of initial patterns): "))
        light_patern(init_chain, btn_list)
    else:
        print("Starting with default difficulty.")

def restart_game():
    global score, best_score, patern, chain, init_chain
    print("Restart Game!")
    time.sleep(2) 
    start_game()

def game_over():
    global score, best_score, patern, chain, init_chain
    print("Game Over!")
    time.sleep(2)  # Laisser le temps de voir la fin du jeu
    start_game()

def check_patern(patern, btn_list):
    global score, chain
    for expected_led in patern:
        # Attente d'un appui sur un bouton
        pressed = False
        while not pressed:
            user_input = input("Press the corresponding button (A, B, C, D, E): ").upper()
            if user_input in btn_list:
                pressed = True
                if btn_list.index(user_input) == expected_led:
                    score += 1
                    print("Good job!")
                else:
                    game_over()
                    return
            time.sleep(0.1)  # Petite pause pour éviter une détection multiple

    # Nouveau tour
    chain += 1
    restart_question = input("Do you want to continue to the next round? (Y/N): ").upper()
    if restart_question == "Y":
        difficulty_question = input("Do you want to change the difficulty? (Y/N): ").upper()
        if difficulty_question == "Y":
            chain = int(input("Enter the new difficulty (number of initial patterns): "))
            light_patern(chain, btn_list)
        else:
            print("Starting with default difficulty.")
        light_patern(chain, btn_list)
    else:
        restart_game()

#region Exec

start_game()

#endregion