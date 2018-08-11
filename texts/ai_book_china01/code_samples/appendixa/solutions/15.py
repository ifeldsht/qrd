from random import randint

N = 10

longest_zeros = 0
current_zeros = 0
previous_outcome = -1
for _ in range(N):
    outcome = randint(0,1)
    if previous_outcome < 0:
        previous_outcome = outcome
        if outcome == 0: 
            current_zeros = 1
        continue
    if outcome == 0:
        if outcome == previous_outcome:
            current_zeros += 1
        else:
            current_zeros = 1
    else:
        if longest_zeros < current_zeros:
            longest_zeros = current_zeros
        current_zeros = 0
    previous_outcome = outcome

# think why we need additional check
if longest_zeros < current_zeros:
    longest_zeros = current_zeros

print longest_zeros
