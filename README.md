# coin-flipping-simulator
Coin Flip Simulator

A simple Python script that simulates flipping a coin. The program randomly generates either "Heads" or "Tails" using the random module.
Features

    Simulates a coin flip.
    Generates a random outcome of either "Heads" or "Tails."
    Simple and easy to customize.

Prerequisites

    Python 3.x installed.

How to Run

    Clone this repository:

git clone https://github.com/jackshaojiewei/coin-flipping-simulator.git
cd coin-flip-simulator

Run the script:

    python coin flip.py

    Output: The script will print either "Heads" or "Tails."

Code Explanation

import random

def flip_coin():
    outcome = random.choice(["Heads", "Tails"])
    return outcome

result = flip_coin()
print(f"The coin landed on: {result}")

    Imports: Uses the random module to select a random choice.
    Function: flip_coin() returns a random outcome.
    Output: Prints the result of the coin flip.

Customization

You can modify the script to flip the coin multiple times or track statistics over several flips.
