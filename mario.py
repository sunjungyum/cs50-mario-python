# Sun-Jung Yum
# Problem Set 6
# 25 October 2018

from cs50 import get_int

while True:
    # Prompts user for height
    height = get_int("Height: ")

    # Breaks out of loop if height is valid (between 1 and 8, inclusive)
    if height >= 1 and height <= 8:
        break

# Iterates through each row
for i in range(height):
    # Prints spaces (height - i - 1) times
    print(" " * (height - i - 1), end="")
    # Prints hashes (i + 1) times
    print("#" * (i + 1))