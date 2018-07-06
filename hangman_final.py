import random # to use the random function
import time # to use the time.sleep() function

count = 0 # global count
word = "" # global word

# player can choose to quit the game of play campaign or custom
def menu(menu):
    global count # count can be used in any function
    choice = None # choice has no value
    while choice != "0":
        print(
        """
         _    _   _____   _       _____   ______   _    _   _____
        | |  | | |  ___| | |     /  ___| /  __  \ | \  / | |  ___|
        | |/\| | | |__   | |     | |     | |  | | |  \/  | | |__
        | /  \ | |  __|  | |     | |     | |  | | | \  / | |  __|
        |  /\  | | |___  | |___  | |___  | |__| | | |\/| | | |___
        |_/  \_| |_____| |_____| \_____| \______/ |_|  |_| |_____|

         _______   ______
        |__   __| /  __  |
           | |    | |  | |
           | |    | |  | |
           | |    | |__| |
           |_|    \______/

         _    _       ___   _   _   _____   _    _       ___   _   _   _
        | |  | |     /   | | \ | | /  ___| | \  / |     /   | | \ | | | |
        | |__| |    / /| | |  \| | | |___  |  \/  |    / /| | |  \| | | |
        |  __  |   / __  | | | \ | | |_  \ | \  / |   / __  | | | \ | |_|
        | |  | |  / /  | | | |\  | | \_/ | | |\/| |  / /  | | | |\  |  _
        |_|  |_| /_/   |_| |_| \_| \_____/ |_|  |_| /_/   |_| |_| \_| |_|
        
          
        0 - Quit
        1 - Campaign
        2 - Custom
        """
        )

        choice = str(input("Choice:  "))
        print("\n") # prints extra line for spacing

        # exit
        if choice == "0" or choice.lower() == "quit": # can enter response in lower or upper
            print(
            """
              _______   __    __       ___   _   _   _    _   ______
             |__   __| |  |  |  |     /   | | \ | | | |  / / /  ____|
                | |    |  |__|  |    / /| | |  \| | | |_/ /  | |____
                | |    |   __   |   / __  | | | \ | |  _ |   \_____ |
                | |    |  |  |  |  / /  | | | |\  | | | \ \   _____| |
                |_|    |__|  |__| /_/   |_| |_| \_| |_|  \_\ |______/
              _____   ______   _____
             |  ___| /  __  \ |  _  |
             | |__   | |  | | | |_| |
             |  __|  | |  | | |  _  /
             | |     | |__| | | | \ |
             |_|     \______/ |_|  \_|
              _____   _           ___   _    _   _   _   _   _____   _
             |  _  \ | |         /   | \ \  / / | | | \ | | /  ___| | |
             | |_| | | |        / /| |  \ \/ /  | | |  \| | | |___  | |
             |  ___/ | |       / __  |   \  /   | | | | \ | | |_  | |_|
             | |     | |___   / /  | |   | |    | | | |\  | | \_/ |  _
             |_|     |_____| /_/   |_|   |_|    |_| |_| \_| \_____/ |_|
            
            """
            )
            time.sleep(.5) # to slow the script down
            quit() # quits the game

        # campaign
        elif choice == "1" or choice.lower() == "campaign": # acepting value
            count = 1 # setting count to = 1
            campaign(campaign) # calling the campaign code
            break # break the loop
        # custom
        elif choice == "2" or choice.lower() == "custom": # acepting value
            print("\n" * 30) #to clear the screen
            count = 0 # setting count to = 0
            custom(custom) # calling the custom code
            break # break the loop

def main():
    global count # count can be used in any function
    # 10 x hangman designs and prints
    HANGMAN = (
    """
     ------
     |    
     |
     |
     |
     |
     |
     |
     |
     ----------
     """,
     """
     ------
     |    |
     |    0
     |
     |
     |
     |
     |
     |
     ----------
     """,
     """
     ------
     |    |
     |    0
     |   -+-
     |
     |
     |
     |
     |
     ----------
     """,
     """
     ------
     |    |
     |    0
     |  /-+-
     |
     |
     |
     |
     |
     ----------
     """,
     """
     ------
     |    |
     |    0
     |  /-+-\ 
     |
     |
     |
     |
     |
     ----------
     """,
     """
     ------
     |    |
     |    0
     |  /-+-\ 
     |    | 
     |
     |
     |
     |
     ----------
     """,
     """
     ------
     |    |
     |    0
     |  /-+-\ 
     |    | 
     |    | 
     |   |  
     |    
     |
     ----------
     """,
     """
     ------
     |    |
     |    0
     |  /-+-\ 
     |    | 
     |    | 
     |   | 
     |   | 
     |
     ----------
     """,
     """
     ------
     |    |
     |    0
     |  /-+-\ 
     |    | 
     |    | 
     |   | | 
     |   | 
     |
     ----------
     """,
     """
     ------
     |    |
     |    0
     |  /-+-\ 
     |    | 
     |    | 
     |   | | 
     |   | | 
     |
     ----------
     """)

    # define other setup variables
    max_wrong = len(HANGMAN) - 1 # changes the hangman design
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    so_far = "-" * len(word) # one dash for each letter in word to be
    'guessed'
    wrong = 0 # number of wrong guessed player has made
    used = [] # letters already guessed
    

    # prints the setup design
    while wrong < max_wrong and so_far != word:
        print(HANGMAN[wrong])
        print("\nYou've used the following letters:\n", used)
        print("\nSo far, the word is:\n", so_far)
        
        guess = input("\n\nEnter your guess: ")
        guess = guess.lower() # can enter response in lower or upper
        print("\n") # prints extra line for spacing
        # any time during the game you can quit or return to menu
        if guess == "quit":
            print("Thanks for Playing")
            time.sleep(.5) # to slow the script down
            quit() # quits  the game
        if guess == "menu":
            menu(menu)
        # if guess has already been guessed
        while guess in used:
            print("You've already guessed the letter", guess)
            guess = input("\n\nEnter your guess: ")
            guess = guess.lower()

        used.append(guess)
        # checks to see if guess is in alphabet
        if guess in alphabet:
            # checks to see if guess is in word
            if guess in word:
                print("\nYes!", guess, "is in the word!")
                # create a new so_far to include guess
                new = ""
                for i in range(len(word)):
                    if guess == word[i]:
                        new += guess
                    else:
                        new += so_far[i]
                so_far = new
            else:
                print("\nSorry,", guess, "isn't in the word.")
                wrong += 1

        else:
            print("\nSorry,", guess, "isn't in the word.")
            wrong += 1
    # if you run out of lives
    if wrong == max_wrong:
        print(HANGMAN[wrong])
        print("\n" * 30) #to clear the screen
        print(
        """
          _    _   ______   _    _    _   _     _   _____
         \ \  / / /  __  \ | |  | |  / / \ \   | | |  ___|
          \ \/ /  | |  | | | |  | | /_/   \ \  | | | |__
           \  /   | |  | | | |  | |        \ \ | | |  __|
           | |    | |__| | | |__| |         \ \| | | |___
           |_|    \______/ \______/          \___| |_____|
          ______    _____   _____   _   _
         /  __  |  |  ___| |  ___| | \ | |
         | |__| /  | |__   | |__   |  \| |
         |  ___ \  |  __|  |  __|  | | \ |
         | |___| | | |___  | |___  | |\  |
         \_______/ |_____| |_____| |_| \_|
          _    _       ___   _   _   _____   _____   ______    _
         | |  | |     /   | | \ | | /  ___| |  ___| /  __  \  | |
         | |__| |    / /| | |  \| | | |___  | |__   | |  \  \ | |
         |  __  |   / __  | | | \ | | |_  \ |  __|  | |   | | |_|
         | |  | |  / /  | | | |\  | | \_/ | | |___  | |__/  /  _
         |_|  |_| /_/   |_| |_| \_| \_____/ |_____| \______/  |_|
        """
        )
        print("\nThe word was", word)
        quit_or_menu(quit_or_menu)
    else:
        print("\nYou guessed it!")
        print(word)
        if count == 0:
            quit_or_menu(quit_or_menu)
        else:
            count += 1
            campaign(campaign)

            
# wheather the player wants to play again or quit
def quit_or_menu(quit_or_menu):
    print("\n\nEnter 'quit' to Quit the Quiz or 'menu' to return to Menu")
    playagain = input("What is your answer?: ")
    playagain = playagain.lower() # can enter response in lower or upper
    print("\n") # prints extra line for spacing
    if playagain == "quit":
        print("Thanks for Playing")
        time.sleep(.5) # to slow the script down
        quit() # quits the game
    elif playagain == "menu":
        menu(menu) # calls menu     
    else:
        print("Thanks for Playing!")
        time.sleep(.5) # to slow the script down
        quit() # quits the game


# choosing random word from level one.txt
def level(level_choice):
    global word # word can be used in any function
    word = random.choice(list(open('words/word_list_level_' + level_choice + '.txt'))) # chooses a word to be guessed
    word = word.replace("\n","") # changing the enter into nothing
    main() # calls main

# the player can complete all the levels, but if the person fails they have to restart
def campaign(campaign):
    global count # count can be used in any function
    print("\n" * 30) #to clear the screen
    lv = (
        """
         _       _____   _     _   _____   _
        | |     |  ___| \ \   | | |  ___| | |
        | |     | |__    \ \  | | | |__   | |
        | |     |  __|    \ \ | | |  __|  | |
        | |___  | |___     \ \| | | |___  | |___
        |_____| |_____|     \___| |_____| |_____|
        """
        )
    while count < 7: # while count is < 6
        if count == 1:
            print(lv)
            print(
            """
              ______   _   _   _____   _
             /  __  \ | \ | | |  ___| | |
             | |  | | |  \| | | |__   | |
             | |  | | | | \ | |  __|  |_|
             | |__| | | |\  | | |___   _
             \______/ |_| \_| |_____| |_|
            """
            )
            level("one") # calls level one word
            break # break the loop
        elif count == 2:
            print(lv)
            print(
            """
              _______   _    _   ______   _
             |__   __| | |  | | /  __  \ | |
                | |    | |/\| | | |  | | | |
                | |    | /  \ | | |  | | |_|
                | |    |  /\  | | |__| |  _
                |_|    |_/  \_| \______/ |_|
            """
            )
            level("two") # calls level two word
            break # break the loop
        elif count == 3:
            print(lv)
            print(
            """
              _______   _    _   _____    _____   _____   _
             |__   __| | |  | | |  _  \  |  ___| |  ___| | |
                | |    | |__| | | |_| |  | |__   | |__   | |
                | |    |  __  | |  _  /  |  __|  |  __|  |_|
                | |    | |  | | | | \ \  | |___  | |___   _
                |_|    |_|  |_| |_|  \_\ |_____| |_____| |_|
            """
            )
            level("three") # calls level three word
            break # break the loop
        elif count == 4:
            print(lv)
            print(
            """
              _____   ______   _    _   _____    _
             |  ___| /  __  \ | |  | | |  _  \  | |
             | |__   | |  | | | |  | | | |_| |  | |
             |  __|  | |  | | | |  | | |  _  /  |_|
             | |     | |__| | | |__| | | | \ \   _
             |_|     \______/ \______/ |_|  \_\ |_|
            """
            )
            level("four") # calls level four word
            break # break the loop
        elif count == 5:
            print(lv)
            print(
            """
              _____   _   _     _   _____   _
             |  ___| | | \ \   | | |  ___| | |
             | |__   | |  \ \  | | | |__   | |
             |  __|  | |   \ \ | | |  __|  |_|
             | |     | |    \ \| | | |___   _
             |_|     |_|     \___| |_____| |_|
            """
            )
            level("five") # calls level five word
            break # break the loop
        elif count == 6:
            print(
            """
              _    _   _____   _       _              
             | |  | | |  ___| | |     | |            
             | |/\| | | |__   | |     | |           
             | /  \ | |  __|  | |     | |            
             |  /\  | | |___  | |___  | |___
             |_/  \_| |_____| |_____| |_____|        
              ______    ______   _   _   _____
             /  __  \  /  __  \ | \ | | |  ___|
             | |  \  \ | |  | | |  \| | | |__
             | |   | | | |  | | | | \ | |  __|
             | |__/  / | |__| | | |\  | | |___   _
             \______/  \______/ |_| \_| |_____| / /
                                               /_/
            """
            )
            time.sleep(1) # to slow the script down
            print("\n" * 30) #to clear the screen
            print(
            """
             _    _   ______   _    _                
            \ \  / / /  __  \ | |  | |          
             \ \/ /  | |  | | | |  | |          
              \  /   | |  | | | |  | |          
              | |    | |__| | | |__| |          
              |_|    \______/ \______/          
              _    _       ___   _     _   _____
             | |  | |     /   | \ \   | | |  ___|
             | |__| |    / /| |  \ \  | | | |__
             |  __  |   / __  |   \ \ | | |  __|
             | |  | |  / /  | |    \ \| | | |___
             |_|  |_| /_/   |_|     \___| |_____|
             _____   ______   _    _   _       _____   _______   _____   ______
            /  ___| /  __  \ | \  / | | |     |  ___| |__   __| |  ___| /  __  |
            | |     | |  | | |  \/  | | |     | |__      | |    | |__   | |  \  |
            | |     | |  | | | \  / | | |     |  __|     | |    |  __|  | |   | |
            | |___  | |__| | | |\/| | | |___  | |___     | |    | |___  | |__/  /
            \_____| \______/ |_|  |_| |_____| |_____|    |_|    |_____| \______/
            """
            )
            time.sleep(1) # to slow the script down
            print("\n" * 30) #to clear the screen
            print(
            """
              _______   _    _   _____          
             |__   __| | |  | | |  ___|        
                | |    | |__| | | |__          
                | |    |  __  | |  __|         
                | |    | |  | | | |___         
                |_|    |_|  |_| |_____|        
              _____       ___   _    _   _____     ___   _   _____   _   _
             /  ___|     /   | | \  / | |  _  \   /   | | | /  ___| | \ | |
             | |        / /| | |  \/  | | |_| |  / /| | | | | |___  |  \| |
             | |       / __  | | \  / | |  ___/ / __  | | | | |_  \ | | \ |
             | |___   / /  | | | |\/| | | |    / /  | | | | | \_/ | | |\  |
             \_____| /_/   |_| |_|  |_| |_|   /_/   |_| |_| \_____/ |_| \_|
              _    _   ______   ______    _____   _
             | \  / | /  __  \ /  __  \  |  ___| | |
             |  \/  | | |  | | | |  \  \ | |__   | |
             | \  / | | |  | | | |   | | |  __|  |_|
             | |\/| | | |__| | | |__/  / | |___   _
             |_|  |_| \______/ \______/  |_____| |_|
            """
            )
            time.sleep(1) # to slow the script down
            print("\n" * 30) #to clear the screen
            menu(menu) # calls menu
            break # break the loop


# choose what level the player wants to play
def custom(custom):
    choice = None # choice has no value
    print("\n" * 30) #to clear the screen
    while choice != "0":
        print(
        """
        Choose What Level you Would Like to Play!
          
        1 - Level 1
        2 - Level 2
        3 - Level 3
        4 - Level 4
        5 - Level 5
        """
        )
        choice = str(input("Choice:  "))
        print("\n") # prints extra line for spacing
        print(
        """
          _____   ______   ______   ______
         /  ___| /  __  \ /  __  \ /  __  |
         | |___  | |  | | | |  | | | |  \  |
         | |_  \ | |  | | | |  | | | |   | |
         | \_/ | | |__| | | |__| | | |__/  /
         \_____/ \______/ \______/ \______/
          _       _    _   _____   _    _   _
         | |     | |  | | /  ___| | |  / / | |
         | |     | |  | | | |     | |_/ /  | |
         | |     | |  | | | |     |  _ |   |_|
         | |___  | |__| | | |___  | | \ \   _
         |_____| \______/ \_____| |_|  \_\ |_|
        """
        )
        # choosing level 1
        if choice == "1" or choice.lower() == "level 1": # can enter response in lower or upper
            level("one") # calls level one word
            break # break the loop
        # choosing level 2
        elif choice == "2" or choice.lower() == "level 2": # can enter response in lower or upper
            level("two") # calls level two word
            break # break the loop
        # choosing level 3
        elif choice == "3" or choice.lower() == "level 3": # can enter response in lower or upper
            level("three") # calls level three word
            break # break the loop
        # choosing level 4
        elif choice == "4" or choice.lower() == "level 4": # can enter response in lower or upper
            level("four") # calls level four word
            break # break the loop
        # choosing level 5
        elif choice == "5" or choice.lower() == "level 5": # excepts ethier value
            level("five") # calls level five word
            break # break the loop



# this is the first thing the code reads
if count == 0:
    count += 10 # adds 10 to count
    menu(menu) # sends it to the menu

main() # calls main


