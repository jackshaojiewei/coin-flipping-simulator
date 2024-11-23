import random

def flip_coin():
    outcome = random.choice(["Heads", "Tails"])
    return outcome

# Flip the coin and print the result
result = flip_coin()
print(f"The coin landed on: {result}")
