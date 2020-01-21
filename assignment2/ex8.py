# formatter creates 4 empty spots that can be filled
formatter = "{} {} {} {}"

# formatter is placed and .format fills those spots with what is listed
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
# here formatter is filled with itself so we are included more {}
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        "Try your",
        "Own text here",
        "Maybe a poem",
        "Or a song about fear"
))
