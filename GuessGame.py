from logging.config import stopListening

GuessCount=0
SecretNo=4
Guess_Limit=3
while GuessCount < Guess_Limit:
    Guess = int(input("Guess: "))
    GuessCount += 1
    if Guess== SecretNo:
        print("Correct")
        break
    else:
        print("Incorrect!Retry again.")
else:
    print("Limit is over!")


