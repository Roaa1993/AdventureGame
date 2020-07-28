import time
import random


def print_s(msg_stop):
    print(msg_stop)
    time.sleep(2)


def explain():
    print_s("Welcome to the challenge.")
    print_s("We have two goalkeepers, Roaa and Hassan.")
    print_s("To win the game you must defeat both.")
    print_s("Both are to defeated by two goals.")
    print_s("The number of goals will be randomly chosen for you.")
    print_s("Let's go..")


def choose_goalkp(item):
    print_s("\nWant to play against who?")
    goalkeeper = input("1.Roaa / 2.Hassan, enter '1' or '2':\n")
    if goalkeeper == '1':
        print_s("You chose to start with Roaa..")
        roaa(item)
    elif goalkeeper == '2':
        print_s("Well, you will first play against Hassan..")
        hassan(item)
    else:
        choose_goalkp(item)


def roaa(item):
    goal = random.choice(["one", "two"])
    print_s("\nYour number of goals scored is: " + goal)
    if "win" in item:
        if goal == 'two':
            print_s("Bravo, you won the game.")
            play_again()
        else:
            print_s("\nYou was close to winning, do not despair..")
            play_again()
    elif "win" not in item:
        if goal == 'two':
            print_s("Now you will play against Hassan to win the game.")
            item.append("win")
            hassan(item)
        else:
            print_s("\nUnfortunately, you lost..")
            play_again()


def hassan(item):
    goal = random.choice(["one", "two"])
    print_s("\nYour number of goals scored is: " + goal)
    if "win" in item:
        if goal == 'two':
            print_s("Bravo, you won the game.")
            play_again()
        else:
            print_s("\nYou was close to winning, do not despair..")
            play_again()
    elif "win" not in item:
        if goal == 'two':
            print_s("Now you will play against Roaa to win the game.")
            item.append("win")
            roaa(item)
        else:
            print_s("\nUnfortunately, you lost..")
            play_again()


def play_again():
    again = input("\nDo you want to play again? enter 'yes' / 'no';\n").lower()
    if again == 'yes':
        print_s("\nYou are a great player, let's go ..")
        play_game()
    elif again == 'no':
        exit(print_s("\nOk, goodbye..!"))
    else:
        print_s("Please, enter 'yes' or 'no'")
        play_again()


def play_game():
    item = []
    explain()
    choose_goalkp(item)
    play_again()


play_game()
