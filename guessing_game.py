import random

def main():
    play= True
    
    while(play):
        win=False

        print("""
        Welcome to the NUMBER GUESSING GAME!!!
        I'm thinking of a number between 1 and 100 
        You have limited chances to guess the number

        Select the difficulty level: 
        1. Easy (10 chances)
        2. Medium (5 chances)
        3. Hard (3 Chances)
        """
        )
        option= int(input("Enter your choice: "))

        chances= 10 if option==1 else 5 if option==2 else 3 if option==3 else 0
        if not chances: 
            continue

        generated_number=random.randint(1,100)
        attempts=0
        for _ in range (chances): 
            guess= int(input("Enter your guess: "))
            attempts+=1
            if (guess==generated_number):
                win=True
                break 
            else: 
                print("\nERRR Try again")
                if (guess<generated_number):
                    print("\nHIGHER!!")
                else:
                    print("\nLOWER!!")
            
        if win:
            print(f"\nYOU GUESSED THE NUMBER!! CONGRATULATIONS\nIt only took {attempts} attempts")
        else: 
            print("\nYou lost :( \nThe correct number was: ", generated_number)


        print("""Do you want to continue? 
        1. Yes
        2. No
        """)
        again= int(input("Enter your choice: "))
        if again==2:
            play=False
    print("\nMay luck be with you :)")


main()