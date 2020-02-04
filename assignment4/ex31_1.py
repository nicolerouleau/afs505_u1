print("""You entered into your favorite show.
Just kiddng, you've entered into the show that I am binge watching: Futurama.
Do you choose to go to the year 2000 or 3000.""")

year = input("> ")

if year == "2000":
    print("Really? This is your preferred place? 2000?")
    print("Choose: \n 1 Stay in 2000. \n 2 Get frozen and go to year 3000.")

    try_again = input("> ")

    if try_again == "1":
        print("""Turns out this was a great choice for you.
        You weren't ready for the future.""")
        print("You get a dead end job and marry someone you hate, the 'American Dream'.")
    elif try_again == "2":
        print("Turns out you weren't meant for the future.")
        print("A robot steals your money and a cyclopse kicks you in the face.")
        print("You proceed to a suicide booth and end it.")
    else:
        print("No one cares what you want.")

elif year == "3000":
    print("You made the right choice.")
    print("Live happily with a robot, a cyclopse, and your 160 yr old nephew.")
else:
    print("""You couldn't even pick a year right...
    All you had to do was choose a number...
    You were given two options and couldn't figure it out...
    Get out. """)
