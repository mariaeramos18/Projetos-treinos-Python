""" string concatenation (aka how to put string together)
#lets suppose that we want to create a string that says "subscribe to ____"
youtuber = "Maria Ramos"

# ways to do it
#print("Subscribe to {}".format(youtuber)) or
print(f"Subscribe to {youtuber}")"""

adj = input("Adjective: ")
verb1 = input("Verb 1: ")
verb2 = input("Verb 2: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so{adj}! it makes me so excited all the time, because I love {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)