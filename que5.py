import math
for angle in range(0,346,15):
    radians=math.radians(angle)
    sine=round(math.sin(radians),4)
    cosine=round(math.cos(radians),4)
    print(f"{angle}, {sine}, {cosine}")