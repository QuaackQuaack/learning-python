smallest= None
for intervar in [4,3,4,583,37,2,4,5,9]:
    if smallest is None or intervar < smallest:
        smallest = intervar
    print("Loop: ",smallest,intervar)

print("smallest is ",smallest)
a=[4,3,4,583,37,2,4,5,9]
print(min(a))
