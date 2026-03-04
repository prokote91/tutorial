grocery = ["air", "telur", "ikan", "ayam", "cincau"]
grocery.insert(3, "tofu")
grocery.remove("cincau")
grocery.reverse()


print(grocery)
print(("tofu") in grocery)


number = [1, 2, 3, 4, 5, 6, 7]
number.sort()
highest = number[0]
print(highest)

number.reverse()
lowest = number[0]
print(lowest)

print(f"the highest number is {lowest} while the lowest number is {highest}")
