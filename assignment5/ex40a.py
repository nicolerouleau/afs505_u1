my_stuff = {'apple': "I AM APPLES!"}
print(my_stuff['apple'])
####
import mystuff
mystuff.apple()
#####
def apple():
    print("I AM APPLES!")
#this is just a variable
tangerine = "Living reflection of a dream"
#####
print(mystuff.tangerine)

mystuff.tangerine
######
class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM CLASSY APPLES")

thing = MyStuff()
thing.apple()
print(thing.tangerine)
########
mystuff['apples']

mystuff.apples()
print(mystuff.tangerine)

thing = MyStuff()
thing.apples()
print(thing.tangerine)
