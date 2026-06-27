import random
def displayCard(dealer,player):
    print(f"dealer :{dealer} player : {player}   player sum = {sum(player)}")
def stand(dealer,player,card):
    while True:
        playersum = sum(player)
        dealersum = sum(dealer)
        if dealersum <= 16:
            dealer.append(random.choice(card))
        elif dealersum > 21:


            if 11 in dealer:
                    dealer.remove(11)
                    dealer.append(1)
                    dealersum = sum(dealer)
                    displayCard(dealer,player)
                    
            else:  
                    displayCard(dealer,player)
                    print("you win")
                    return False
                   


           
            
        elif dealersum > playersum:
            displayCard(dealer,player)
            print("----------------------you loose-----------------------")
            return False
        elif dealersum < playersum:
            displayCard(dealer,player)
            print("-----------------------you won-----------------------")
            return False
        elif dealersum == playersum:
            displayCard(dealer,player)
            print("-----------------------TIE -----------------------")
            return False


card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
play = input("do you want to play a game")
status = True
new = False
while ((True if play == "y" else False) and status) or new :
    dealer = random.sample(card,2)
    player = random.sample(card,2)
    playersum = sum(player)
    dealersum = sum(dealer)
    print(f"deales :[{dealer[0]}, H ] player : {player}   player sum = {sum(player)}")
    
    while True:
        if dealersum == 21:
            displayCard(dealer,player)
            print("you loose dealer has a black jack ")
            break
        elif playersum == 21:
            displayCard(dealer,player)
            print("you won Black jack")
            break
        elif playersum > 21:
            if 11 in player:
                player.remove(11)
                player.append(1)
                displayCard(dealer,player)
                playersum = sum(player)
            else:  
                displayCard(dealer,player)
                print("you loose")
                status = False
                break
        elif playersum <21:
            hitorstand = input("do you want to hit or stand(hit/stand)")
            if hitorstand == "hit":
                player.append(random.choice(card))
                playersum = sum(player)
                print(f"YOU HIT SO new set of card is {player}")
                print(f"deales :[{dealer[1]}, H ] player : {player}   player sum = {sum(player)}")
            elif hitorstand == "stand":
                status = stand(dealer,player,card)
                break

    newgame = input("NEW GAME (y/n)")
    if newgame == "y":
        new = True
    else:
        new = False

