import random # to use the random function
import time # to use the time.sleep() function

count = 0 # global count
word = "" # global word

# player can choose to quit the game of play campaign or custom
def quit_or_campaign_or_custom(quit_or_campaign_or_custom):
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

         __    __       ___   _   _   _____   _    _       ___   _   _   _
        |  |  |  |     /   | | \ | | /  ___| | \  / |     /   | | \ | | | |
        |  |__|  |    / /| | |  \| | | |___  |  \/  |    / /| | |  \| | | |
        |   __   |   / __  | | | \ | | |_  \ | \  / |   / __  | | | \ | |_|
        |  |  |  |  / /  | | | |\  | | \_/ | | |\/| |  / /  | | | |\  |  _
        |__|  |__| /_/   |_| |_| \_| \_____/ |_|  |_| /_/   |_| |_| \_| |_|
        
          
        0 - Quit
        1 - Campaign
        2 - Custom
        """
        )
        choice = str(input("Choice:  "))
        print()

        # exit
        if choice == "0" or choice.lower() == "quit": # 
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
              _____   _           ___   _    _   _   _   _   _____
             |  _  \ | |         /   | \ \  / / | | | \ | | /  ___|
             | |_| | | |        / /| |  \ \/ /  | | |  \| | | |___
             |  ___/ | |       / __  |   \  /   | | | | \ | | |_  |
             | |     | |___   / /  | |   | |    | | | |\  | | \_/ |
             |_|     |_____| /_/   |_|   |_|    |_| |_| \_| \_____/
            
            """
            )
            time.sleep(.5)
            quit()

        # campaign
        elif choice == "1" or choice.lower() == "campaign":
            count = 1
            campaign(campaign) # calling the campaign code
            break
        # custom
        elif choice == "2" or choice.lower() == "custom":
            print("\n" * 30) #to clear the screen
            count = 0
            custom(custom) # calling the custom code
            break
        
# choosing random word from level one.txt
def level(level_choice):
    global word # word can be used in any function
    word = random.choice(list(open('words/word_list_level_' + level_choice + '.txt'))) # chooses a word to be guessed
    word = word.replace("\n","") # changing the enter into nothing
    print(word)


# the player can complete all the levels, but if the person fails they have to restart
def campaign(campaign):
    global count # count can be used in any function
    while count < 6: # while count is < 6
        print(count)
        if count == 1:
            level("one")
            break
        elif count == 2:
            level("two")        
            print(count)
            break
        elif count == 3:
            level("three")           
            break
        elif count == 4:
            level("four")            
            break
        elif count == 5:
            level("five")           
            break
        elif count == 6:
            quit_or_restart(quit_or_restart)
            break


# choose what level the player wants to play
def custom(custom):
    choice = None # choice has no value
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
        print()

        # choosing level 1
        if choice == "1" or choice.lower() == "level 1":
            level("one")
            break
        # choosing level 2
        elif choice == "2" or choice.lower() == "level 2":
            level("two")
            break
        # choosing level 3
        elif choice == "3" or choice.lower() == "level 3":
            level("three")
            break
        # choosing level 4
        elif choice == "4" or choice.lower() == "level 4":
            level("four")
            break
        # choosing level 5
        elif choice == "5" or choice.lower() == "level 5":
            level("five")
            break


# wheather the player wants to play again or quit
def restart_or_menu(restart_or_menu):
    print("\n\nEnter 'quit' to Quit the Quiz or 'restart' to Restart the Quiz")
    playagain = input("What is your answer?: ").lower()
    if playagain == "quit":
        print("Thanks for Playing")
        time.sleep(.5)
        quit()
    elif playagain == "restart":
        print("Here We Go")
        time.sleep(.5)
        quit_or_campaign_or_custom(quit_or_campaign_or_custom)      
    else:
        print("Thanks for Playing")
        time.sleep(.5)
        quit()

if count == 0:
    count += 10
    quit_or_campaign_or_custom(quit_or_campaign_or_custom)



def main():
    global count # count can be used in any function
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
     """) # to show hangman's lives

# define other setup variables
    max_wrong = len(HANGMAN) - 1
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    so_far = "-" * len(word) # one dash for each letter in word to be
    'guessed'
    wrong = 0 # number of wrong guessed player has made
    used = [] # letters already guessed
    
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

    while wrong < max_wrong and so_far != word:
        print(HANGMAN[wrong])
        print("\nYou've used the following letters:\n", used)
        print("\nSo far, the word is:\n", so_far)
        
        guess = input("\n\nEnter your guess: ")
        guess = guess.lower()

        if guess == "quit":
            print("Thanks for Playing")
            time.sleep(.5)
            quit()

        while guess in used:
            print("You've already guessed the letter", guess)
            guess = input("\n\nEnter your guess: ")
            guess = guess.lower()

        used.append(guess)
        
        if guess in alphabet:
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

    if wrong == max_wrong:
        print(HANGMAN[wrong])
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
          __    __       ___   _   _   _____   _____   ______    _
         |  |  |  |     /   | | \ | | /  ___| |  ___| /  __  \  | |
         |  |__|  |    / /| | |  \| | | |___  | |__   | |  \  \ | |
         |   __   |   / __  | | | \ | | |_  \ |  __|  | |   | | |_|
         |  |  |  |  / /  | | | |\  | | \_/ | | |___  | |__/  /  _
         |__|  |__| /_/   |_| |_| \_| \_____/ |_____| \______/  |_|
        been hanged!
        """
        )
        print("\nThe word was", word)
        restart_or_menu(restart_or_menu)
    else:
        print("\nYou guessed it!")
        print(word)
        if count == 0:
            restart_or_menu(restart_or_menu)
        elif count == 1 or 2 or 3 or 4 or 5 or 6:
            count += 1
            campaign(campaign)
  
main()


