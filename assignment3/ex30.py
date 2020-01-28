# creates variables
people = 40
cars = 30
trucks = 25

# if statment
if cars > people:
    print("We should take the cars.")
# elif = else if
elif cars < people:
    print("We should not take the cars.")
# if none of the above options print this
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

if people < trucks:
    print("Wait why aren't we taking the cars?")
