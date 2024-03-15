def solve(numheads, numlegs):
    # Calculate the number of chickens and rabbits
    # Let c be the number of chickens and r be the number of rabbits
    # We have two equations:
    # 1. c + r = numheads (total number of heads)
    # 2. 2c + 4r = numlegs (total number of legs)
    # Solving these equations gives us the values of c and r.

    for c in range(numheads + 1):
        r = numheads - c
        if 2 * c + 4 * r == numlegs:
            return c, r

    # If no solution is found, return None
    return None

# Example usage
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)

if result:
    chickens, rabbits = result
    print(f"Number of chickens: {chickens}\nNumber of rabbits: {rabbits}")
else:
    print("There is no solution.")
