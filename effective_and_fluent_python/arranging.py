names = ['Cecilia','Lise','Marie']
counts = [len(n) for n in names]

max_numbers = 0
longest_name = None
for i, check in enumerate(names):
    count = counts[i]
    if count  > max_numbers:
        longest_name = check
        max_numbers = count

print(longest_name)
