# # string concatenation (aka how to put strings together)
# # suppose we want to create a string that says "Learn Python with ______."
# name = "Francisco Martinez" # some string variable 

# # a few ways to do this
# print ("Learn Python with " + name)
# print ("Learn Python with {}".format(name))
# print (f"Learn Python with {name}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
