import os
import time
import random

money = 1000
print("Welcome to the Casino, This is the rullete")
while True:
    print("------------------------------------------")
    print("you have", money)
    try:
        select = input('Place your bet, "black", "red", "green": ')
        bet = int(input("Input the amount of money that you want to bet: "))
        value = money - bet
        if value < 0:
            print("you dont have enogh money")
        elif bet < 0:
               print("you have to input a positive number")
               break
        elif select in ("black", "red", "green"):
                money = money - bet
                print(".")
                time.sleep(0.6)
                print("..")
                time.sleep(0.6)
                print("...")
                time.sleep(0.6)
                winner = random.randint(1, 38)
                if 1 <= winner <= 18:
                    num = "black"
                elif 19 <= winner <= 36:
                    num = "red"
                elif 37 <= winner <= 38:
                    num = "green"
                ##############################
                if num == "black":
                    if select == "black":
                        m = bet * 2
                        money = money + m
                        print(money)
                elif num == "red":
                    if select == "red":
                                    m = bet * 2
                                    money = money + m
                                    print(money)
                elif num == "green":
                    if select == "green":
                                                m = bet * 18
                                                money = money + m
                                                print(money)
                os.system("cls")
                print("Winner:", num)
        else:
              print('You have to input ')
    except ValueError:
        os.system("cls")
        print('------ !!!! you have to type "red" or "black" or an integer !!!! ------')
        print()

#black = 1
#red = 2
