"""Example of writing a function to search a list."""


def main() -> None:
    guess: str = input("What is the code word? ")
    possible_answers: list[str] = ["pokemon", "wordle"]
    if contains(guess, possible_answers):
        print("We're letting you in the secret club...")
    else:
        print("Go back to Davis.")


def contains(needle: str, haystack: list[str]) -> bool:
    """Searches a str list to find a str."""
    for item in haystack:
        if item == needle:
            return True
    return False


if __name__ == "__main__":
    main()