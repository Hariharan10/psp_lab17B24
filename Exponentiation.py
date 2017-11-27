def expo(base, expo):
    ans = 1.0
    if type(base) == str or type(expo) == str:
        return "Invalid Input"
    elif expo >= 0:
        for i in range(1, expo + 1):
            ans = base*ans
    else:
        for i in range(expo, 0):
            ans = 1/base*ans
    return ans
print expo(2, 3)
