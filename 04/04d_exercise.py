weight = int(input("apa berat anda?"))
height = int(input("apa tinggi anda?"))

BMI = (weight/((height/10)**2)*100)
print(BMI)


if BMI >= 30:
    print("Obese")
elif BMI >= 25:
    print("fatty boom boom")
elif BMI >= 18:
    print("okay")
else:
    print("kurus")
