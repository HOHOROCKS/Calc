def calc (a, b, function):
    function = str(function)
    if function == "mul":
        return a*b
    elif function == "div":
        return a/b
    elif function == "sub":
        return a-b
    else:
        return a+b
    

