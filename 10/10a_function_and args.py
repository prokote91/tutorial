#function wiht parameter
def greet_person(name):
    print(f"Hello,{name}")


greet_person("azim")

#function with return value
def add_numbers(a,b):
    return a+b

result = add_numbers(5,3)
print(result)

##default parameter
def greet_with_title(name,title="Mr."):    #ada default value,MR
    return f"HELLO, {title} {name}"

print(greet_with_title("azim"))
print(greet_with_title("mabb", "dr"))

#args (to unpack lists)
def sum_all(*args):
    return sum(args)

print(sum_all(1,2,3,4,5))

#kwargs (to unpack dictionary)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="alice" , age = 25, city = "new york")

#args and kwargs
def flexible_function(*args, **kwargs):
    print("positional argument:", args)
    print("keyword arguments:", kwargs)

flexible_function(2,3,4, name= "Alice", age= 25)

#lambda
square = lambda x: x**2
print(square(5))

add= lambda x, y : x + y
print(add(3,4))