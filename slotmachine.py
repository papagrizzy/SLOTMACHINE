import random

digits = "0123456789"
slot_rolls = ["🍉", "🍒", "🍋", "🍑", "🔔"]


#FUNCTIONS
def deposit():
    bool_flag = True
    while True:
        dep_amount = input("What would you want to deposit?: $")
        temp_list = dep_amount.split(".")
        dep_amount = temp_list[0]
        for i in dep_amount:
            if i not in digits:
                bool_flag = False
        if bool_flag:
            break
        else:
            print("Invalid Input! Enter again!")
            continue
    return int(dep_amount)


def roll():
    count = 0
    luck_list = []
    while count<3:
        luck = random.randint(0, 4)
        luck_list.append(luck)
        count+=1
    return luck_list


def win_result(num):
    print(slot_rolls[num]*3)

def lose_result(num):
    print(slot_rolls[num], end="")


while True:
    ch = input("Deposit or quit?(y/n): ").upper()
    if ch == "Y":
        depo = deposit()
        copy = depo
        while depo>0:
            spin = input("Spin for $1?(y/n): ").upper()
            if spin == "Y":
                lis = roll()
                if lis[0] == lis[1] and lis[1]==lis[2]:
                    win_result(lis[0])
                    depo+=7
                    print("+$7")
                else:
                    depo-=1
                    lose_result(lis[0])
                    lose_result(lis[1])
                    lose_result(lis[2])
                    print()
                    print("-$1")
                    
            elif spin == "N":
                choice = input("Do you want to cash-out(y/n) or quit(q)?").upper()
                if choice == "Y":
                    if copy>depo:
                        print(f"You lost ${copy-depo}!")
                    elif depo>copy:
                        print(f"You gained ${depo-copy}!")
                    else:
                        print("You neither gained nor lost.")
                elif choice == "Q":
                    print("Quitting....")
                    quit()
            
            
            if depo == 0:
                print("You are left with no balance!")
                print("Deposit again to play!")
    else:
        print("Quitting....")
        quit()

    