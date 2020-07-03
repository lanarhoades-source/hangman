from getpass import getpass

    #type the guess word here
secret_word=getpass().lower()

#cartoon hangman code
cartoon_list=[
                "\t\t______\n\t\t      |\n\t\t      |\n\t\t      |\n\t\t      |\n\t\t   ___|___",
                "\t\t______\n\t\t |    |\n\t\t      |\n\t\t      |\n\t\t      |\n\t\t   ___|___",
                "\t\t______\n\t\t |    |\n\t\t O    |\n\t\t      |\n\t\t      |\n\t\t   ___|___",
                "\t\t______\n\t\t |    |\n\t\t O    |\n\t\t |    |\n\t\t      |\n\t\t   ___|___",
                "\t\t______\n\t\t |    |\n\t\t O    |\n\t\t/|    |\n\t\t      |\n\t\t   ___|___",
                "\t\t______\n\t\t |    |\n\t\t O    |\n\t\t/|\   |\n\t\t      |\n\t\t   ___|___",
                "\t\t______\n\t\t |    |\n\t\t O    |\n\t\t/|\   |\n\t\t/     |\n\t\t   ___|___",
                "\t\t______\n\t\t |    |\n\t\t O    |\n\t\t/|\   |\n\t\t/ \   |\n\t\t   ___|___",
            ]
cartoon_list


strikes=0
wrong_guess=''
masked_secret_word=['_' for x in secret_word]

while strikes <7:
    guess=input().lower()[0]
    if guess in secret_word:
        for digit,letter in enumerate(secret_word):
            if letter == guess:
                masked_secret_word[digit]=guess
        print("secret word: "+' '.join(masked_secret_word))
        print(cartoon_list[strikes])
        print("wrong guess: "+wrong_guess)
    else:
        strikes+=1
        wrong_guess+=guess
        print("secret word: "+' '.join(masked_secret_word))
        print(cartoon_list[strikes])
        print("wrong guess: "+wrong_guess)
    if '_' not in masked_secret_word:
        print('you win')
        break
if strikes==7:
    print('you lose')



