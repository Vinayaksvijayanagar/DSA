# A fully automatic washing machine estimates wash time based on weight:
#   0g → 0 min
#   1–2000g → 25 min (low)
#   2001–4000g → 35 min (medium)
#   4001–7000g → 45 min (high)
#   >7000g → "OVERLOADED"
#   Invalid input → "INVALID INPUT"
# Print: "Time Estimated: X minutes"
# Sample input
# 2000
# Sample output
# Time Estimated: 25 minutes

n = int(input())
if n<0:
    print("INVALID INPUT")
else:

    if n == 0:
        print("Time Estimated: 0 minutes")
    elif n>=1 and n<2001:
        print("Time Estimated: 25 minutes")
    elif n>=2001 and n<4001:
        print("Time Estimated: 35 minutes")
    elif n>=4001 and n <7001:
        print("Time Estimated: 45 minutes")
    else:
        print("OVERLOADED")
