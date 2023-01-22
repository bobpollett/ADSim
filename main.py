import random
import textout

#global variables used to score the game
approval = 50;
budget = 1000000;
tenure = 0;
ncaa_heat = 0;
game_continues = True;


def main():
    #starting text
    start()
    #main game loop
    while game_continues:
        status(approval, budget, tenure, ncaa_heat)
        choiceloop()
        checkforgameend()


def start():
    print("Welcome to Athletic Director Simulator 3001, a ripoff of a good idea.")
    print("Subscribe to Extra Points.")
    print("")
    print("In this game, you are the Athletic Director of a mid-major university.")
    print("You win the game by either being liked enough to get poached by a Power Five school or by lasting in the job for thirty years and cashing out a university pension.")
    print("You lose the game if you become too unpopular, bankrupt the athletic department, or get a SHOW-CAUSE PENALTY.")


def status(approval, budget, tenure, ncaa_heat):
    print("")
    print("")
    print("Approval = " + str(approval) + "%")
    print("Budget = $" + str(budget))
    print("Tenure = " + str(tenure) + " years")
    print("Wanted Level: " + str(ncaa_heat) + " stars")

def checkforgameend():
    global game_continues
    if approval < (tenure):
        print ("")
        print ("You're not popular enough to keep this job! YOU'RE FIRED!")
        print ("YOU LOSE!")
        game_continues = False
    elif approval > 110:
        print ("")
        print ("You're the new AD at Missouri!")
        print ("YOU WIN... kinda.")
        game_continues = False
    elif budget < 0:
        print ("")
        print ("You've driven this department into the poorhouse! Now we have to mortgage the dorms.")
        print ("YOU LOSE!")
        game_continues = False
    elif tenure >= 30:
        print ("")
        print ("You've been employed here for 30 years without getting fired!")
        print ("You've worked here long enough to rake in that sweet, sweet university pension!")
        print ("ULTIMATE VICTORY!!!!")
        game_continues = False
    elif ncaa_heat >= 6:
        print ("")
        print ("You've done it now! The NCAA has given you a SHOW-CAUSE PENALTY")
        print ("YOU LOSE!")
        game_continues = False

def choiceloop():
        global approval, budget, tenure, ncaa_heat, game_continues
        print("")
        print("Spend money?")
        print("1. Yes")
        print("2. No")
        choice = input("Enter your choice:")

        if choice == "1":
            approval = approval + 1
            budget = budget - 10000
            tenure = tenure + 1
        elif choice == "2":
            approval = approval - 1
            budget = budget + 5000
            tenure = tenure + 1
        else:
            print("That is not a valid choice.")

if __name__ == '__main__':

    main()