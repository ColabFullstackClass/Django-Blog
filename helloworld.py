name = "John Doe"
age = 34
is_JS_good = True



print(f"My name is {name}, I am  {age}.")

print("Django is a framework")

count = 7

if count < 7:
    print("Count is less than 7")

elif count > 7:
    print("Count is greater than 7")

else:
    print("Count is Null")


landver = {
    "name": "James",
}

print(landver["name"])

users = [
    {"name": "John", "age": 25},
    {"name": "Alice", "age": 30}
]

for x in users:
    print(x)

map(users)

def greet(name):
    return 


def addition(a, b):
    return a + b

value = addition(5, 6)
print(value)


# Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hi(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

p = Person("Alice", 30)
print(p.say_hi())
