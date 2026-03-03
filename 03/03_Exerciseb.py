Score= 0

Quiz = int(input("Lets do a quiz. what is 1+8?"))
if Quiz == 9:
    print("correct")
    Score= Score + 1
else:
    print("False")

Quiz_2= int(input("Next. what is 2+8?"))
if Quiz_2== 10:
    print("correct")
    Score= Score + 1
else:
    print("False")


Quiz_3= int(input("Next. what is 3+8?"))
if Quiz_3== 11:
    print("correct")
    Score= Score + 1
else:
    print("False")

print("Marks:", Score, "/3")