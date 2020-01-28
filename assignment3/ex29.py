people = 20
cats = 30
dogs = 15

## if change initial numbers, what is printed could change
if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Noy many cats! The world is saving!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
