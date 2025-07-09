#Hangman in Python
import random
from wordslist import words #importing words from another file

#defining a simple list to choose from
words=("apple","orange","banana","cocont","pineapple","sugarcane")

#dictionary of key containing tuple value:() => creating a ASCI art 
#key=>incorrect number of guesses
#value =>tuple of strings representing each line of hangman drawing
hangman_art={0: ("   ",
                 "   ",
                 "   "),
             1: (" o ",
                 " | ",
                 "   "),
             2: (" o ",
                 " | ",
                 "   "),
             3: (" o ",
                 "/| ",
                 "   "),
             4: (" o ",
                 "/|\\", #single backslash is a escape sequence so using double backslash to print one
                 "   "),
             5: (" o ",
                 "/|\\",
                 "/  "), 
             6: (" o ",
                 "/|\\",
                 "/ \\ ")}

#function to display hangman based on wrong guess count
def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)

#function to display current progress (hint) with underscores and guessed letters
def display_hint(hint): #hint is a list of characters ("_")
    print(" ".join(hint)) 
#" ".join(hint) joins all the letters into a single string, with a space (" ") between each letter
    

#function to display the full correct answer
def display_answer(answer):
    print(" ".join(answer))

def main():
    answer=random.choice(words) #chooses random words form list
    hint=["_"]*len(answer)#list of underscores equal to word length
    wrong_guesses=0
    guessed_letters=set() #set to store already guessed letters
    is_running=True

    while is_running:
        display_man(wrong_guesses)#function to display the full correct answer
        display_hint(hint) #display current hint status
        guess=input('Enter a letter:').lower()

        #validating the input: only single alphabet allowed
        if len(guess)!=1 or not guess.isalpha():
            print("INvalid input")
            continue
                
        #if the letter is already guessed
        if guess in guessed_letters:
            print(f'{guess} is already guessed')
            continue

        guessed_letters.add(guess) #add guess to the set

        
        #if guessed letter is in the answer
        if guess in answer:
            for i in range(len(answer)):
                if answer[i]==guess:
                    hint[i]=guess #reveal the letter at correct positions
        else:
            wrong_guesses+=1 #increase wrong guess counter if incorrect


        #check win condition
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!")
            is_running=False
        
        #check lose condition
        elif wrong_guesses >=len(hangman_art)-1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE")
            is_running =False


if __name__ =="__main__":
    main()

