b = input()
decimal = 0
power = 0

for digit in reversed(b):
    decimal += int(digit) * (2 ** power)
    power += 1

print(decimal)