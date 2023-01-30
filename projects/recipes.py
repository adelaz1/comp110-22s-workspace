"""Recipes proj."""

recipes: dict[str, list[str]] = {}


def menu():
    print("Hello! Welcome to your Recipe Book!")
    print("[1] Add a new recipe")
    print("[2] Find a recipe")
    print("[3] Print all recipes")
    print("[0] Close")


def option1():
    name: str = input("Name of Dish: ")
    ingredients: list[str] = []
    one_ingredient: str = " "
    step: str = " "
    i: int = 1
    print("Press enter when done.")
    while one_ingredient != "":
        one_ingredient = input(f"Ingredient {i}: ")
        ingredients.append(one_ingredient)
        i += 1
    j: int = 1
    print("Press enter when done.")
    while step != "":
        step = input(f"Step {j}: ")
        ingredients.append(f"Step {j}: " + step)
        j += 1
    recipes[name] = ingredients
    print("Recipe added!")


def option2():
    if recipes != {}:
        k: int = 0
        name: str = input("Which dish are you looking for? ")
        for key in recipes:
            if key == name:
                print(f"Recipe Name: {name}")
                print("Ingredients: ")
                for value in recipes[key]:
                    if k < len(recipes[key]) - 1:
                        print(value)
                    k += 1
                        
            else:
                print("Recipe not found!")
    else:
        print("Recipe Book is empty!")


def option3():
    if recipes != {}:
        k: int = 0
        for key in recipes:
            print(f"Name of Dish: {key}")
            print("Ingredients: ")
            for value in recipes[key]:
                if k < len(recipes[key]) - 1:
                    print(value)
                k += 1
    else:
        print("Recipe Book is empty!")


menu()
option = int(input("Enter your option: "))

while option != 0:
    if option == 1:
        option1()

    elif option == 2:
        option2()

    elif option == 3:
        option3()

    else:
        print("Sorry, that is invalid!")

    print()
    menu()
    option = int(input("Enter your option: "))


print("Thank you for using your Recipe Book!")