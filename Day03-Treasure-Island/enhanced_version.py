print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`.'`, . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print("🏴‍☠️ WELCOME TO TREASURE ISLAND 🏴‍☠️")
print("Your mission is to find the legendary treasure before it's too late!\n")

name = input("What is your name, adventurer? ").strip()

print(f"\nWelcome, {name}! Your adventure begins now...\n")

choice1 = input(
    'You arrive at a mysterious crossroads.\n'
    'One path leads into a dark forest. The other leads toward the mountains.\n'
    'Type "left" to enter the forest or "right" to climb the mountains.\n'
).lower()

if choice1 == "left":

    choice2 = input(
        '\n🌊 You discover a beautiful lake.\n'
        'An island can be seen in the middle of the water.\n'
        'You notice a small boat approaching in the distance.\n\n'
        'Type "wait" to wait for the boat.\n'
        'Type "swim" to swim across the lake.\n'
    ).lower()

    if choice2 == "wait":

        choice3 = input(
            '\n🏝️ You arrive safely on the island.\n'
            'In front of you stands an old mysterious house.\n'
            'There are three doors:\n'
            '🔴 Red\n'
            '🟡 Yellow\n'
            '🔵 Blue\n\n'
            'Which door do you choose?\n'
        ).lower()

        if choice3 == "yellow":
            print(
                "\n🎉 You open the yellow door and discover a room filled with gold!\n"
                f"Congratulations, {name}! You found the treasure! 🏆💰\n"
                "YOU WIN!"
            )

        elif choice3 == "red":
            print(
                "\n🔥🔥🔥 You open the red door...\n"
                "The room suddenly bursts into flames!\n"
                "GAME OVER."
            )

        elif choice3 == "blue":
            print(
                "\n👹 You open the blue door...\n"
                "You hear a terrifying growl behind you.\n"
                "The room is full of beasts!\n"
                "GAME OVER."
            )

        else:
            print(
                "\n🚪 That isn't one of the available doors.\n"
                "The opportunity disappears forever.\n"
                "GAME OVER."
            )

    elif choice2 == "swim":
        print(
            "\n🐟 You jump into the lake and begin swimming...\n"
            "Suddenly, an angry trout attacks!\n"
            "GAME OVER."
        )

    else:
        print("\n❌ That's not a valid choice. GAME OVER.")

else:
    print(
        "\n⛰️ You head toward the mountains...\n"
        "Suddenly, the ground gives way beneath your feet!\n"
        "You fall into a hidden hole.\n"
        "GAME OVER."
    )