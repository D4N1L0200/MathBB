import math

class Ansi:
    def __init__(self):
        self.save = "\033[s"
        self.load = "\033[u"
    
    def up(self, num = 1):
        return f"\033[{num}A"
    
    def down(self, num = 1):
        return f"\033[{num}B"
    
    def right(self, num = 1):
        return f"\033[{num}C"
    
    def left(self, num = 1):
        return f"\033[{num}D"

ANSI = Ansi()

print("Quadratic equation solver")
print("Type each integer in order (a, b, c)")
while True:
    a = input(f"0 = {ANSI.save}")
    b = input(f"{ANSI.load}{ANSI.right(len(a))}x² + {ANSI.save}")
    c = input(f"{ANSI.load}{ANSI.right(len(b))}x + ")
    print(f"\na = {a}, b = {b}, c = {c}")

    # Full formula => -b+-sqrt(b²-4ac)/2a

    try:
        a = int(a)
        b = int(b)
        c = int(c)
    except ValueError:
        print("Some value is not an integer, the inputs are invalid.")
        break 

    delta = b**2-4*a*c
    if delta < 0:
        print("The value for delta is negative, the inputs are invalid.")
        break
    else:
        x1 = (-b+math.sqrt(delta))/2*a
        x2 = (-b-math.sqrt(delta))/2*a
        print(f"delta = {delta}, x' = {x1}, x\" = {x2}")
    
    print("\nContinue? (y/n)")
    if input("> ").lower() != "y":
        break

# Test cases

# a = 1, b = 3, c = -4
# delta = 25, x' = 1, x" = -4

# a = 1, b = -3, c = -10
# delta = 49, x' = 5, x" = -2

# a = 6, b = -17, c = 12
# delta = 1, x' = 54, x" = 48
