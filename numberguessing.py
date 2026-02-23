import random
def number_guessing():
    com=random.randint(1,10)
    for i in range(4):
        num=int(input("Enter a number"))
        if num==com:
            print("Correct guess\n")
            print("You won")
            break
        else:
            print("Not a correct guess try again")
    print("Do you want to paly again?")
    choice=input("Enter yes/No")
    if choice=="yes":
        number_guessing()
    else:
        print("ThankYou!")


number_guessing()