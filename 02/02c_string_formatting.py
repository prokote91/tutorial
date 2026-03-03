name = "Azim"
age = 30

message_1 = f"my name is {name} and i am {age}"
message_2 = "my name is {} and i am {}".format(name,age)
message_3 = "my name is %s and i am %d" %(name,age)

print(message_1)
print(message_2)
print(message_3)