<<<<<<< HEAD
# cats_name = "Oakley"
# print(f"Hayyyy {cats_name.upper()}")

cats = ['Oakley', 'Milla']

def greet(cat):
    print(f'Hello, {cat.upper()}')

for cat in cats:
    greet(cat)
greet('pat')
# greet() throws error, needs an argument
greet('')
=======
whom = "Chris"
# How do I define a function?
def greet(whom):
    print(f"Hayyyy {whom.upper()}")

# How do I use a function?
greet("Bob")
# We "call" the function by typing its name and passing it any arguments it needs.
# Another way to say this is: we "invoke" the function.

# Are arguments required?
#greet()
# Yes, they are required if there were arguments included in the definition of the function.

# Can I access arguments outside the body of a function?
print(whom)
>>>>>>> fd42aee1ade7f9e049586ff0e9a05a215ca6d39c
