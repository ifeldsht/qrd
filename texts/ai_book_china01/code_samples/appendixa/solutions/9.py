with open("one_column.txt","r") as f:
    numbers = [ float(x) for x in f.read().split("\n") if len(x)>0 ]

print sum(numbers)
print max(numbers)
print min(numbers)
print numbers.index(max(numbers))
print numbers.index(min(numbers))
