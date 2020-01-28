def x_and_y(x, y):
    print(f"There is {x} of x.")
    print(f"There is {y} of y.")

print("Way number 1.")
x_and_y(10, 15)

print("Way number 2.")
amount_x = 20
amount_y = 45
x_and_y(amount_x, amount_y)

print("Way number 3.")
x_and_y(7 + 4, 12 + 3)

print("Way number 4.")
x_and_y(amount_x + 32, amount_y + 2)

print("Way number 5.")
also_x = 17
also_y = 9
x_and_y(amount_x + also_x, amount_y + also_y)

print("Way number 6.")
x_and_y(input(),input())

print("Way number 7.")
oh_x = "nonsense"
oh_y = "not important"
x_and_y(oh_x , oh_y)

print("Way number 8.")
x_and_y(f"{oh_x}", f"it's {oh_y}")

print("Way number 9.")
x_and_y(input() + input(), input() + input())

print("Way number 10.")
x_and_y(input() + f"{also_x}", input() + f"{also_y}")
