import random

wordlist = ["bit", "protocol", "computer", "router", "transmission", "domain", "python", "compression", "pixel", "abstraction", "internet", "language", "sequence", "function", "algorithm", "iteration", "condition", "library", "parameter"]
                                    # above is my list of words to use in my game
word = random.choice(wordlist)
mixedword = list(word)              # the command "list" takes the word and breaks the letters into a list
random.shuffle(mixedword)           # next I used the command random.shuffle to shuffle the letters (that are now a list) into a new order
    
print "I have a word but the letters are mixed up."     # I introduce the game to the user
print mixedword                                         # I tell the user the word with the letters mixed up
count=1                                                 # this and the next line starts a counter of the guesses
guess=1   
print "Guess what word it is!"                          # This is the prompt for the user to start playing
  
guess=raw_input()                                       # This intiates the counting of the guesses, as it is looped below.
while guess != word:                                    # This is a loop for when the guess is not the original word (see line 5)
    count += 1                                          # this adds one to the counter every time the user guesses
    print "---------------Your guess was " +str(guess)+ " and it is incorrect. Guess again!---------------"
    print
    print "-------------------------------  Try again.  -------------------------------"
    guess=raw_input()
print "Great job!  My word is " +word+ "!  You guessed in " +str(count)+ " guesses!"
print
print "Let's play again."

 # Is there a way to start the program without making it a function?   