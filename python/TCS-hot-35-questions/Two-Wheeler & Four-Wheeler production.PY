# An automobile company manufactures both a two-wheeler (TW) and a four-wheeler (FW). Given:
#   V = total number of vehicles (TW + FW)
#   W = total number of wheels
# Find how many TW and FW to manufacture.
# Print "INVALID INPUT" if constraints not met.
# Constraints: W%2==0, W>=2, V

# Sample input
# 200
# 540

# Sample output
# TW=130 FW=70

V = int(input()) #total vehicles
W = int(input()) # total wheels

if W%2 != 0 or W<2:
    print("INVALID INPUT")
else:
    FW= (W - ((V)*2) )//2
    TW = V-FW
    
print(f"TW={TW} FW={FW}")
    