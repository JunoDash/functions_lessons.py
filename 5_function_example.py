# def happy_birthday_function(name, age):
#     print(f"Happy birthday to {name}!")
#     print(f"You are {age}")
#     print("Happy birthday to you!")
#     print()

# happy_birthday_function("bro", 20)

# happy_birthday_function("mom", 51)

# happy_birthday_function("dad", 30)

# def displayinvioce(user, amount, due):
#     print(f"Hello, {user}!")
#     print(f"Your bill of ${amount:.2f} is due: {due}")

# displayinvioce("mom", 67, "6/7")

# # return used to end a function and send a result back to the caller
# def add(x, y):
#     z = x + y
#     return z

# def subtract(x, y):
#     z = x - y
#     return z

# def multiply(x, y):
#     z = x * y
#     return z

# def divide(x, y):
#     z = x / y
#     return z

# print(add(1, 2))
# print(subtract(1, 2))
# print(multiply(1, 2))
# print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + last

print(create_name("Yes", "No"))