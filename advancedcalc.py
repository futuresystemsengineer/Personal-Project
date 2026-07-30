def add(x, y):
    z = (x+y)
    return z

def multiply(x, y):
    z = (x*y)
    return z

def subtract(x, y):
    z = (x-y)
    return z

def divide(x, y):
    z = round(x/y, 2)
    return z

x = int(input("What number do you want to be x? "))
y = int(input("What number do you want to be y? "))

print(add(x,y))
print(multiply(x,y))
print(subtract(x,y))
print(divide(x,y))