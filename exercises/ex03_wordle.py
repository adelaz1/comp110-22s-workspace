"""EX03 - Basically Wordle."""

__author__ = "730490894"


def contains_char(searched_through: str, searched_for: str) -> bool:
    """Searches for a single letter in a given string."""
    assert len(searched_for) == 1
    i: int = 0
    while i < len(searched_through):
        if searched_for == searched_through[i]:
            return True
        else:
            i += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Checks if guess is in secret and returns emoji boxes."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    emoji: str = ""
    i: int = 0
    while i < len(guess) and len(secret):  # creates an emoji string based on letters
        if guess[i] == secret[i]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret, guess[i]) is True:  # calling contains_char function
                emoji += YELLOW_BOX
            else:
                emoji += WHITE_BOX
        i += 1
    return emoji


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess until guess is expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ") 
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    track: bool = False
    secret: str = "codes"
    while track is False and turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(secret))  # calling input_guess function
        print(emojified(guess, secret))  # calling emojified function
        if guess == secret:
            track = True
            print(f"You won in {turn}/6 turns!")
        turn += 1
    if guess != secret:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()