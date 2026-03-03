#multiplication table generator

Factor = int(input("please give your multiplication number:"))


for i in range (1,13):
    print(f"{i} * {Factor} = {i * Factor}")



"""Another way"""
Factor = int(input("please give your multiplication number:"))

count = 1
while count <= 12:
    print(f"{count} * {Factor} = {count * Factor}")
    count=count + 1