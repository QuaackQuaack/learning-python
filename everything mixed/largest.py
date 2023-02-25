largest = None
print("before :",largest)
for itervar in [9,4,64,54,22,55,60]:
    if largest is None or itervar > largest:
        largest = itervar
    print(" loop :",itervar,largest)

print("largest: ",largest)

