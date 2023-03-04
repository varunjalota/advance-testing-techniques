def addthis(x, y):
    print(f"This is x {x} and x-type {type(x)}")
    print(f"This is y {y} and y-type {type(y)}")
    
    try:
        result = x + y
    except TypeError:
        print("The wrong type passed")
        result =  int(x) + int(y)
    print(f"This is Result {result}")
    return result

print(addthis(1, 2))