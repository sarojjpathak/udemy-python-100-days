import random
def stand(dealer,player):
    while True:
        playersum = sum(player)
        dealersum = sum(dealer)
        if dealersum <= 16:
            dealer.append(random.choice(card))
        elif dealersum > 21:
            print(f"dealer : {dealer} sum: {dealersum} \n player : {player} sum : {playersum}")
            print("you won")
            break
        elif dealersum > playersum:
            print(f"dealer : {dealer} sum: {dealersum} \n player : {player} sum : {playersum}")
            print("you loose")
            return False
card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
play = input("do you want to play a game")
status = True
while ((True if play == "y" else False) and status) or new :
    dealer = random.sample(card,2)
    player = random.sample(card,2)
    print(f"deales :[{dealer[1]}, H ] player : {player}   player sum = {sum(player)}")

    while True:
        if sum(dealer) == 21:
            print(f"deales :{dealer} player : {player}   player sum = {sum(player)}")
            print("you loose ")
            break
        elif sum(player) == 21:
            print(f"deales :{dealer} player : {player}   player sum = {sum(player)}")
            print("you won")
        elif sum(player) > 21:
            if 11 in player:
                player.remove(11)
                player.append(1)
            else:  
                print(f"deales :{dealer} player : {player}   player sum = {sum(player)}")
                print("you loose")
                status = False
                break
        elif sum(player) <21:
            hitorstand = input("do you want to hit or stand(hit/stand)")
            if hitorstand == "hit":
                player.append(random.choice(card))
                print(f"YOU HIT SO new set of card is {player}")
                print(f"deales :[{dealer[1]}, H ] player : {player}   player sum = {sum(player)}")
            elif hitorstand == "stand":
                status = stand(dealer,player)
                break

    newgame = input("NEW GAME (y/n)")
    if newgame == "y":
        new = True
    else:
        new = False


