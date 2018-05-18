import random
import time
levelOne = [ 'ant', 'bee', 'star', 'this', 'code', 'fork', 'word', 'work', 'wrap', 'cow', 'dog', 'cat', 'last' ]
levelTwo = [ 'issue', 'watch', 'spaces', 'cancel', 'horse', 'piglet', 'cracks', 'crates', 'boats', 'heart', 'first', 'school', 'think' ]
levelThree = [ 'project', 'explore', 'request', 'insight', 'hangman', 'respect', 'blanket', 'meeting', 'practice', 'setting', 'personal', 'finding', 'uniform', 'college' ]
levelFour = ['leadership', 'challenge', 'excellence', 'powerpoint', 'structure', 'generate', 'preforming', 'together', 'dashbourd', 'calendar']
levelFive = ['marketplace', 'stratergies', 'questioning', 'exploration', 'motivation', 'connections', 'visualising', 'mathematics']
import time
name = input("What is your name? ")
print("Hello, " + name, "Time to play hangman!")
print("")
time.sleep(1)
print("Start guessing...")
time.sleep(0.5)
import random
word = random.choice(levelOne)
guesses = ''
turns = 10
while turns > 0:         
    failed = 0                
    for char in word:      
        if char in guesses:    
            print(char)   
        else:
            print("_")    
            failed += 1    
    if failed == 0:        
        print("You won")
        break              
    print
    guess = input("guess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1        
        print("Wrong")   
        print("You have", + turns, "more guesses") 
        if turns == 0:           
            print("You Lost, sad face")
            print("the word was:")
            print(word)
            
    
