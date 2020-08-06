amount_of_atoms = int(input())
final_quantity = int(input())

half_life_cycle = 0

while amount_of_atoms >= final_quantity:
    amount_of_atoms /= 2
    half_life_cycle += 1

print(half_life_cycle * 12)
