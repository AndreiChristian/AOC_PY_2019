def find_fuel(mass: int) -> int:
    """Calculate fuel requirement for given mass."""
    return max(0, int(mass / 3) - 2)


def find_recursive_fuel(mass: int) -> int:
    """Calculate total fuel requirement for given mass, considering fuel's mass."""
    fuel = find_fuel(mass)
    if fuel == 0:
        return 0
    return fuel + find_recursive_fuel(fuel)


with open('./input.txt', 'r') as file:
    lines = file.readlines()

simple_sum = sum(find_fuel(int(line)) for line in lines)

recursive_sum = sum(find_recursive_fuel(int(line)) for line in lines)

print(f"Simple fuel sum: {simple_sum}")
print(f"Recursive fuel sum: {recursive_sum}")

# Test with the given value
print(find_recursive_fuel(654))
