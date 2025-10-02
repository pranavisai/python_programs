from art import logo

print(logo)

should_continue = True
bidders = {}
max_bid = 0
max_bid_name = ""

while should_continue:
    continue_text = input("Does anyone want to bid? Yes/No").lower()
    if continue_text == "no":
        should_continue = False
        print(f"The highest bid was {max_bid}")
        print(f"Congratulations! {max_bid_name}")
    elif continue_text == "yes":
        print("\n" * 20)
        name = input("Please state your name.")
        bid = input("How much do you want to bid? $")
        bidders[name] = bid

        for name in bidders:
            bid = int(bidders[name])
            if bid > max_bid:
                max_bid = int(bid)
                max_bid_name = name
    else:
        print("Wrong input entered")










