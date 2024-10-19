import random
from logo import logo

card_list = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]
card_value = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

seleted_card_pc = [[], []]
seleted_card_user = [[], []]


def choice (card, value):   
    item = random.randint(0, 12)
    name = card[item]
    scope = value[item]
    return [name, scope]
       
flag = True

win = 0
lose = 0
draw = 0

while flag:
    if win != 0 or lose != 0 or draw != 0:
        answer = input("CONTINUE GAME! Y/N").lower()
        if answer == "y":
            print(f"Ration between your win / lose / draw is {win}/{lose}/{draw}.")
            print("Distribution of cards!")
            print(logo)
            print("START GAME")
            #for PC
            for i in range(2):
                card = choice(card_list, card_value)
                seleted_card_pc[0].append(card[0])
                seleted_card_pc[1].append(card[1])
            # for user
            for i in range(2):
                card = choice(card_list, card_value)
                seleted_card_user[0].append(card[0])
                seleted_card_user[1].append(card[1])
            print(f"First card in PC is {seleted_card_pc[0][0]}\nYou have next card{seleted_card_user[0]}. Summary {sum(seleted_card_user[1])} scopes")
            user_answer = "y"
            while sum(seleted_card_user[1])<21 and user_answer == "y":
                user_answer = input("Are you wanting to get new card? Y/N").lower()
                if user_answer =="y":
                    card = choice(card_list, card_value)
                    seleted_card_user[0].append(card[0])
                    seleted_card_user[1].append(card[1])
                    if sum(seleted_card_user[1])<21:
                        print(f"First card in PC is {seleted_card_pc[0][0]}\nYou have next card {seleted_card_user[0]}. Summery {sum(seleted_card_user[1])} scopes")
                    elif sum(seleted_card_user[1]) > 21 and 11 not in seleted_card_user[1]:
                        print(f"YOU LOSE! Becouse total your scope is {sum(seleted_card_user[1])}. You are having next cards {seleted_card_user[0]}. ")
                        user_answer = input("Will deal cards for next game? Y/N ").lower()
                        user_answer = "n"
                        lose +=1
                        seleted_card_user = [[], []]
                        seleted_card_pc = [[], []]
                    elif sum(seleted_card_user[1]) > 21 and 11 in seleted_card_user[1]:
                        for i, val in enumerate(seleted_card_user[1]):
                            if val==11:
                                seleted_card_user[1][i] = 1
                        print(f"Your total scope is {sum(seleted_card_user[1])}. You are having next cards {seleted_card_user[0]}. ")
                    else:
                        print("You have 21 points")
                        if sum(seleted_card_user[1]) == sum(seleted_card_pc[1]):
                            print(f"************\nDRAW! You and PC are having equal points {sum(seleted_card_user[1])}")
                            draw += 1
                            seleted_card_user = [[], []]
                            seleted_card_pc = [[], []]
                        else:
                            print(f"************\nYOU WIN! You is having points {sum(seleted_card_user[1])}! PC is having points {sum(seleted_card_pc[1])}!")
                            win += 1
                            seleted_card_user = [[], []]
                            seleted_card_pc = [[], []]
  
                else:
                    user_answer = "n"
                    print(f"Your total scope is {sum(seleted_card_user[1])}. You are having next cards {seleted_card_user[0]}.")
                    print(f"PC total scope is {sum(seleted_card_pc[1])}. You are having next cards {seleted_card_pc[0]}.")
                    if sum(seleted_card_user[1]) == sum(seleted_card_pc[1]):
                        print(f"************\nDRAW! You and PC are having equal points {sum(seleted_card_user[1])}")
                        draw += 1
                        seleted_card_user = [[], []]
                        seleted_card_pc = [[], []]
                    elif sum(seleted_card_user[1]) > sum(seleted_card_pc[1]):
                        print(f"************\nYOU WIN! You is having points {sum(seleted_card_user[1])}! PC is having points {sum(seleted_card_pc[1])}!")
                        win += 1
                        seleted_card_user = [[], []]
                        seleted_card_pc = [[], []]
                    else:
                        print(f"************\nYOU LOSE! You is having points {sum(seleted_card_user[1])}! PC is having points {sum(seleted_card_pc[1])}")
                        lose += 1
                        seleted_card_user = [[], []]
                        seleted_card_pc = [[], []]                

        elif answer == "n":
            print("GOOD BYE")
            flag = False
        else:
            print("YOU TAPED NOT CORRECT COMMAND!")
            flag = False            

    else:        
        print('************\nWill you want to start Black Jack`s game now? Type "Y" \n For exit from game! Type "N"\n************')
        answer = input("Your answer? Y/N\n").lower()
        if answer == "y":
            print(logo)
            print("START GAME")
            #for PC
            for i in range(2):
                card = choice(card_list, card_value)
                seleted_card_pc[0].append(card[0])
                seleted_card_pc[1].append(card[1])
            # for user
            for i in range(2):
                card = choice(card_list, card_value)
                seleted_card_user[0].append(card[0])
                seleted_card_user[1].append(card[1])
            print(f"First card in PC is {seleted_card_pc[0][0]}\nYou have next card{seleted_card_user[0]}. Summary {sum(seleted_card_user[1])} scopes")
            user_answer = "y"
            while sum(seleted_card_user[1])<21 and user_answer == "y":
                user_answer = input("Are you wanting to get new card? Y/N").lower()
                if user_answer =="y":
                    card = choice(card_list, card_value)
                    seleted_card_user[0].append(card[0])
                    seleted_card_user[1].append(card[1])
                    if sum(seleted_card_user[1])<21:
                        print(f"First card in PC is {seleted_card_pc[0][0]}\nYou have next card {seleted_card_user[0]}. Summery {sum(seleted_card_user[1])} scopes")
                    elif sum(seleted_card_user[1]) > 21 and 11 not in seleted_card_user[1]:
                        print(f"YOU LOSE! Becouse total your scope is {sum(seleted_card_user[1])}. You are having next cards {seleted_card_user[0]}. ")
                        user_answer = input("Will deal cards for next game? Y/N ").lower()
                        user_answer = "n"
                        lose +=1
                        seleted_card_user = [[], []]
                        seleted_card_pc = [[], []]
                    elif sum(seleted_card_user[1]) > 21 and 11 in seleted_card_user[1]:
                        for i, val in enumerate(seleted_card_user[1]):
                            if val==11:
                                seleted_card_user[1][i] = 1
                        print(f"Your total scope is {sum(seleted_card_user[1])}. You are having next cards {seleted_card_user[0]}. ")
                    else:
                        print("You have 21 points")
                        if sum(seleted_card_user[1]) == sum(seleted_card_pc[1]):
                            print(f"************\nDRAW! You and PC are having equal points {sum(seleted_card_user[1])}")
                            draw += 1
                            seleted_card_user = [[], []]
                            seleted_card_pc = [[], []]
                        else:
                            print(f"************\nYOU WIN! You is having points {sum(seleted_card_user[1])}! PC is having points {sum(seleted_card_pc[1])}!")
                            win += 1
                            seleted_card_user = [[], []]
                            seleted_card_pc = [[], []]
  
                else:
                    user_answer = "n"
                    print(f"Your total scope is {sum(seleted_card_user[1])}. You are having next cards {seleted_card_user[0]}.")
                    print(f"PC total scope is {sum(seleted_card_pc[1])}. You are having next cards {seleted_card_pc[0]}.")
                    if sum(seleted_card_user[1]) == sum(seleted_card_pc[1]):
                        print(f"************\nDRAW! You and PC are having equal points {sum(seleted_card_user[1])}")
                        draw += 1
                        seleted_card_user = [[], []]
                        seleted_card_pc = [[], []]
                    elif sum(seleted_card_user[1]) > sum(seleted_card_pc[1]):
                        print(f"************\nYOU WIN! You is having points {sum(seleted_card_user[1])}! PC is having points {sum(seleted_card_pc[1])}!")
                        win += 1
                        seleted_card_user = [[], []]
                        seleted_card_pc = [[], []]
                    else:
                        print(f"************\nYOU LOSE! You is having points {sum(seleted_card_user[1])}! PC is having points {sum(seleted_card_pc[1])}")
                        lose += 1
                        seleted_card_user = [[], []]
                        seleted_card_pc = [[], []]                

        elif answer == "n":
            print("GOOD BYE")
            flag = False
        else:
            print("YOU TAPED NOT CORRECT COMMAND!")
            flag = False
