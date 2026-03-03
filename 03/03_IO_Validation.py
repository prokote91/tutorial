name = input("Nama anda?")
height = float(input("tinggi?"))     #Covert to float

#input validation
while True:
    try: 
        age= int(input("umur?"))
        if age>0:
            break
        else:
            print("Umur kena atas 0 la zzz")
    except ValueError:
        print("nombor please, jangan main main")

#output validation
print(f"Hello, {name}")
print(f"you are{age} and {height} cm")

