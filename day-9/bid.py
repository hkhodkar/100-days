import bid_art;

print(bid_art.logo)

bids = []
is_it_over = False

def take_bid():
    name = input("What is your name?\n")
    price = int(input("What is your bid?\n"))

    bids.append({"name": name, "price": price})

    has_another_bid = input(
        "Are there any other bidders? Type 'yes' or 'no'\n"
    )

    while has_another_bid != "yes" and has_another_bid != "no":
        has_another_bid = input(
            "Invalid input. Please type 'yes' or 'no'\n"
        )

    if has_another_bid == "yes":
        return False
    else:
        return True


while not is_it_over:
    is_it_over = take_bid()

winner = {}
max_price = 0

for bid in bids:
    if bid["price"] > max_price:
        max_price = bid["price"]
        winner["name"] = bid["name"]
        winner["price"] = max_price

print(f"The winner is {winner["name"]} with {winner["price"]}")