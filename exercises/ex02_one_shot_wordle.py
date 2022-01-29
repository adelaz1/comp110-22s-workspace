"""EX02 - Another cute step towards Wordle."""

__author__ = "730490894"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret: str = "python"
response: str = input(f"What is your {len(secret)}-letter guess? ")
i: int = 0
emoji: str = ""

while len(response) != len(secret):  # if guess is the same number of letters
    response = input(f"That was not {len(secret)} letters! Try again: ") 

while i < len(secret):  
    if response[i] == secret[i]:  # if letter is right and in the right spot
        emoji += GREEN_BOX
    else:  # checks if letter is right, but in the wrong spot
        track: bool = False
        alternate: int = 0
        while track is not True and i < len(secret) and alternate < len(secret):
            if secret[alternate] == response[i]:
                track = True
            else:
                alternate += 1
        if track is True:
            emoji += YELLOW_BOX
        else:
            emoji += WHITE_BOX        
    i += 1
print(emoji)

if secret != response:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")