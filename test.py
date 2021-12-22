import random

a = (12, 13, 14)
for elt in reversed(a):
    print(elt)

print(a)



print('\n')

towers = (
    (5, 4, 'rapid'),
    (30, 0.4, 'long'),
    (8, 2, 'normal')
)


def attack(n, a, b, S):
    U = S
    for i in range(n):
        U *= a
        U += 3
    return U


def attack_speed(n, a, S):
    U = S
    for i in range(n):
        U *= a
    return U


for tower in towers:
    for i in range(1, 11):
        print('\n', tower)
        print(round(attack(i, 1.1, 10, tower[0]) * attack_speed(i, 1.2, tower[1])))
