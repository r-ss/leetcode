# testing matching feature from python 3.10

def greet(name):
    match name:
        case "Guido":
            print("Hi, Guido!")
        case _:
            print("Howdy, stranger!")

greet('Guido')
greet('Ress')