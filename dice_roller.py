import random

def roll_dice():
    return random.randint(1, 6)

def show_dice_face(value):
    dice_faces = {
        1: (
            "┌───────┐",
            "│       │",
            "│   ●   │",
            "│       │",
            "└───────┘"
        ),
        2: (
            "┌───────┐",
            "│ ●     │",
            "│       │",
            "│     ● │",
            "└───────┘"
        ),
        3: (
            "┌───────┐",
            "│ ●     │",
            "│   ●   │",
            "│     ● │",
            "└───────┘"
        ),
        4: (
            "┌───────┐",
            "│ ●   ● │",
            "│       │",
            "│ ●   ● │",
            "└───────┘"
        ),
        5: (
            "┌───────┐",
            "│ ●   ● │",
            "│   ●   │",
            "│ ●   ● │",
            "└───────┘"
        ),
        6: (
            "┌───────┐",
            "│ ●   ● │",
            "│ ●   ● │",
            "│ ●   ● │",
            "└───────┘"
        )
    }

    for line in dice_faces[value]:
        print(line)

def main():
    print("🎲 Dice Roller Simulator 🎲")
    while True:
        input("Press Enter to roll the dice... ")
        value = roll_dice()
        print(f"\nYou rolled a {value}!\n")
        show_dice_face(value)

        again = input("\nRoll again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing!")
            break

if __name__ == "__main__":
    main()
