# defines cheese_and_crackers, includes all indetations underneath it
def cheese_and_crackers(cheese_count, boxes_of_crackers):
        print(f"You have {cheese_count} cheeses!")
        print(f"You have {boxes_of_crackers} boxes of crackers!")
        print("Man that's enough for a party!")
        print("Get a blanket.\n")


print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

# gives cheese and crackers amount by settign it aboves
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# we can do math to set cheese ans cracker amounts
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

# we can comine math with previous setting amounts for cheese and cracker amounts
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
