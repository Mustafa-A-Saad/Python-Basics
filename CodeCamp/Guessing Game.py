secret_word = "giraffe"
guess = ""
count = 3

while guess != secret_word:
    print("You have " + str(count) +" Guesses left")
    guess = input("Enter guess: ")
    count -= 1
    if guess == secret_word:
        print("Congratz You Won!!")
    else:
        if count == 0:
            print("You lost")
            break
        print("Try Again")
