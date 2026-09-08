with open("./Day24-Files-Directories-and-Paths/Mail Merge Project Start/Input/Letters/starting_letter.txt") as f:
    starting_letter = f.read()

with open("./Day24-Files-Directories-and-Paths/Mail Merge Project Start/Input/Names/invited_names.txt") as n:
    invited_names = n.readlines()

    for name in invited_names:
        new_name = name.strip()
        new_letter = starting_letter.replace("[name]", new_name)

        with open(f"./Day24-Files-Directories-and-Paths/Mail Merge Project Start/Output/ReadyToSend/letter_for_{new_name}.txt", mode='w') as l:
            new_letter = l.write(new_letter)