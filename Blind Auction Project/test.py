bidding_dict = {
    "Caleb": 250,
    "Ryan": 500,
    "Evan": 1000,
}

bidding_list = []
for key in bidding_dict:
    bidding_list.append(bidding_dict[key])

highest_bid = max(bidding_list)
print(highest_bid)