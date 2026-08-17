import os

bidders = {}

def add_new_bidder(bidder_name, bid_amount):
    bidders[bidder_name] = bid_amount

def find_highest_bidder(bid_record):
    highest_bid = 0
    highest_bidder = ''
    for bidder in bid_record:
        bid_amount = bid_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder

    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
    
from art import logo
print(logo)

continue_bid = True

while continue_bid:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))

    add_new_bidder(bidder_name=name, bid_amount=bid)

    user_option = input("Are there any other bidders? Type 'yes or 'no'.\n").lower().strip()

    if user_option == 'yes':
        os.system("cls")
    else:
        continue_bid = False

find_highest_bidder(bidders)




