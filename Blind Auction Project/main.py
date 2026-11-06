# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art
print(art.logo)
bids = {}
another_bid = "yes"

def find_highest_bidder(bidding_dict):
    highest_bid = 0
    winner = max(bidding_dict , key=bidding_dict.get)
    highest_bid = bidding_dict[winner]
    # for bidder in bidding_dict:
    #     if bidding_dict[bidder] > highest_bid:
    #         highest_bid = bidding_dict[bidder]
    #         winner = bidder
    print(f"The winner is {winner} with the highest bid ${highest_bid}")

while another_bid == "yes":
    name = input("Please enter your name: ")
    bid = int(input("Please enter bid: $"))
    bids[name] = bid
    print(bids)
    another_bid = input("Are there other bidders? ")
    print("\n" * 100)

find_highest_bidder(bids)






