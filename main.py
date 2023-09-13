# --------------------<< MENU MAKER >>--------------------
def menuload(menu):
    count = 1
    for z in menu:
        print(f"{count}. {z}")
        count += 1
    print(f"0. EXIT")
    choice = input("\nEnter Number: ")

    if choice.isnumeric():
        choice = int(choice)

        if choice in range(0, count):
            answer = choice

        else:
            print("Error: Number out of RANGE.")
            answer = 99

    else:
        print("Error: Input NOT a number.")
        answer = 99

    return answer


