#basic exception error

'''try: 
    number = int(input("kasi satu number:"))
    result = 10/ number
    print(f"result: {result}")
except ValueError:
    print(f"nombor {number} tak mantap la")
except ZeroDivisionError:
    print(f" {number} tak boleh oi")

#using else and finally
try:
    file= open("data.txt""r")
except FileNotFoundError:
    print("tak jumpa")
else: #execute if no exception occurs
    content: file.read()
    print("boleh2")
finally: 
    if "file" in locals() and not file.closed:
        file.close()
    print("Cleanup completed")'''


#exceptions
def validate_age(age):
    if age <0:
         raise ValueError("tak logik la umur")
    if age >150:
        raise ValueError("lg tua dri madey oi")
    return True

try: 
    validate_age(160)
except ValueError as e:
    print (f"validation error: {e}")