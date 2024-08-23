import random


def random_roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll


# todo: get a random roll of dice - done
# todo: get the number of players playing - done
# todo: get the game logic where the scores will be added if the dice is rolled or it will be skipped if no
# todo : get to number 50 and you won the match

while True:
    players = input("Enter the Number of Players (2,4) :")

    if players.isdigit():
        if int(players) >= 2 and int(players) <= 4:
            players = int(players)
            print("Number of players selected :", players)
            break
        else:
            print("Please enter a valid number between (2,4) :")
            continue
    else:
        print("Please enter a valid player number")
        continue

print(players)

players_lst = [0 for _ in range(players)]
print(players_lst)

while True:

    for player in range(len(players_lst)):

        print("player number :", player + 1, "turn \n")
        current_score = 0
        while True:
            roll_dice = input("want to roll the dice , y to roll n to skip ").lower()

            if roll_dice == "n":
                break

            roll = random_roll()

            if roll == 1:
                current_score = 0
                players_lst[player] = 0
                print("you rolled 1 ")
                print("your turn is lost, your score will be back to :", current_score)
                break
            current_score += roll

            players_lst[player] += current_score
            score = players_lst[player]
            print("the score of player", player + 1, "is :", players_lst[player])

            if score > 50:
                break
    if players_lst[player] > 50:
        break

for i in range(len(players_lst)):
    if players_lst[i] > 50:
        print("Players ", i + 1, "won !!")
