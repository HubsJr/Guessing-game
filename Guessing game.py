import random
secreat_number=random.randint(1,50)
guess_number=0
guess_limit=5
while guess_number<guess_limit:
    guesx=input('guess the number:')
    guess=int(guesx)
    guess_number=guess_number+1
    if secreat_number<guess:
        print("my number is less")
    elif secreat_number>guess:
        print("my number is greater")
    else:
        print('Great Job!')
    if guess == secreat_number:
        print("You win!!congrats")
        break
    elif guess_number==guess_limit:
        print("Sorry you lose")
        break

