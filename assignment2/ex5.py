name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 * 2.54 # inches to cm
weight = 180 * 0.4536 # lbs to kg
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print(f"Let's talk about {name}.")
# does the math from above for height
print(f"He's {height} cm tall.")
print(f"He's {weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
# takes the math from total and prints it 
print(f"If I add {age}, {height}, and {weight} I get {total}.")
