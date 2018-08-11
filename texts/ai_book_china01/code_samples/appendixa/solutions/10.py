with open("three_columns.csv","r") as f:
    numbers = [ [float(y) for y in x.split(",") ] \
                for x in f.read().split("\n") if len(x)>0 ]

i = 2
j = 1

print sum(numbers[i])
print sum([x[j] for x in numbers])
