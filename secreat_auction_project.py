print("$$$$$$$WELCOME TO THE AUCTION OF ANCIENT GOLD AXE$$$$$$$$$")

auction_dictionary = {}

def register_bid():
    name = input("Enter your name for registration :")
    price = int(input("ENter your bidding price in USD :"))
    auction_dictionary[name] = price
    

def auction_result():
    print("Auction completed")

    if len(auction_dictionary) == 0:
        print("No bids were placed.")
        return

    winner = max(auction_dictionary, key=auction_dictionary.get)

    print(
        f"The winner of the auction is {winner} "
        f"with a bid of ${auction_dictionary[winner]}"
    )
  
    
    

    
run = True
while run:
    participation = input("DO You want to Participate in auction :")
    if participation == "y":
        print("\n"*100)#this is done so that other bidder wwill not see our bid
        register_bid()
    else:
        auction_result()
        run = False


