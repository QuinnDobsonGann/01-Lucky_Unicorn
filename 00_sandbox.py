greeting = "hello world"
sides = "*" * 3

greeting = "{} {} {}".format(sides, greeting, sides)

print(greeting)

top_bottom = "*" * len(greeting)

print(top_bottom)
print(greeting)
print(top_bottom)
    