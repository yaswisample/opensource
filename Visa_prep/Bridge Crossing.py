x, y, z = map(int, input().split())
max_carry_weight = z - y
max_mangoes = max_carry_weight // x
print(max_mangoes)
