# Auction Program

This Python program simulates a simple auction where multiple users can place bids, and the highest bidder is determined at the end. The program runs in a loop, collecting bids until no more bidders are left.

## Features
- Collects bids from multiple users
- Clears the console screen for better readability between different user's inputs
- Determines the highest bidder and displays the winner

## Requirements
- Python 3.x
- `replit` module (for clearing the screen)
- `art` module (for displaying the logo)

## Installation

To run this program, you need to have Python installed. You also need to install the `replit` and `art` modules. You can install these using pip:

```sh
pip install replit
pip install art
```

## How to Use

1. **Start the Program**
   - Run the script in a Python environment.
   - The logo will be displayed at the start.

2. **Enter Bidder Details**
   - The program will prompt you to enter your name and your bid amount.
   - After entering the bid, it will ask if there are any other bidders.

3. **Continue or End Bidding**
   - If there are other bidders, type 'yes'. The screen will clear, and the next bidder can enter their details.
   - If there are no more bidders, type 'no'. The program will then determine and display the highest bidder.

## Code Explanation

```python
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
```

### Breakdown

1. **Imports and Initialization**
   - `clear` from `replit`: Clears the console screen.
   - `logo` from `art`: Displays a logo at the start of the program.
   - `al`: A boolean variable to control the loop.
   - `bidder_store`: A dictionary to store the names and bids of the bidders.

2. **findHigher Function**
   - Loops through the `bidder_store` to find the highest bid.
   - Prints the name of the highest bidder and the amount.

3. **Main Loop**
   - Continuously prompts for the bidder's name and bid.
   - Adds the bidder and their bid to the `bidder_store`.
   - Asks if there are more bidders:
     - If 'no', it stops the loop and calls `findHigher` to determine the winner.
     - If 'yes', it clears the screen for the next bidder.

## Example

```plaintext
 ____  _  _  ____  __  ____  _  _ 
(  __)( \/ )(  __)(  )(_  _)/ )( \
 ) _)  )  /  ) _) / (_/\ )(  ) __ (
(__)  (__/  (____)\____/(__) \_)(_/

What is your name?: Alice
Enter your bid: $100
Are there any other bidders? Type 'yes' or 'no': yes

# (Screen clears)

What is your name?: Bob
Enter your bid: $150
Are there any other bidders? Type 'yes' or 'no': no

The winner is Bob with a bid of $150
```

## License

This project is licensed under the MIT License. See the LICENSE file for details."# blind-auction" 
