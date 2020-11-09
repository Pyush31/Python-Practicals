def digits():
    num = input('Enter a number >=10 :')
    s = []
    for i in num:
        s.append(i)
    return set(s)
    
print("Set : ", digits())
