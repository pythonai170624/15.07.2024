# print 6 random numbers between 1-45

import random  # bring this module into my program

for i in range(1, 7):
    rnd: int = random.randint(1, 45)  # random between 1-45 (include 45)
    print(rnd, end=" ")

# nosaf
print()
nosaf: int = random.randint(1, 6)  # random between 1-10
print(f'mispar nosaf = {nosaf}')