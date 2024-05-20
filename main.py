from replit import clear
from art import logo

print(logo)

al = False
bidder_store = {}

# Function to find the highest bidder
def findHigher():
  highest_bidder = 0
  winner = ""
  for bidder in bidder_store:
    if bidder_store[bidder] > highest_bidder:
      highest_bidder = bidder_store[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bidder}")

# Loop to get bids from users
while not al:
  name = input("What is your name?: ")
  price = int(input("Enter your bid: $"))

  # Add the bidder and their bid to the store
  bidder_store[name] = price

  # Ask if there are other bidders
  chose = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  if chose == "no":
    al = True
    findHigher()
  elif chose == "yes":
    clear()
