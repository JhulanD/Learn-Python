# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available

# Variables
customer_name = "Maya Shergil"
number_of_passes = 5
tokens_per_pass = 25
price_per_pass = 15.75
tokens_required_per_game = 3


# Calculations
total_tokens = number_of_passes * tokens_per_pass
total_cost = number_of_passes * price_per_pass
games_available = total_tokens // tokens_required_per_game


print("======= ^^ ARCADE DAY PASS ^^ ========")
print("Customer Name:", customer_name)
print("Passes Bought:", number_of_passes)
print("Total Tokens:", total_tokens)
print("Total Cost: $" + str(total_cost))
print("Games Available:", games_available)

