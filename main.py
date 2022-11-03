import DiceRolling.roll

# print("D6: " + str(DiceRolling.roll.d6()))

result = DiceRolling.roll.roll_stat_array()
print()
print("---stat Array---")
print("str: " + str(result[0]))
print("dex: " + str(result[1]))
print("con: " + str(result[2]))
print("int: " + str(result[3]))
print("wis: " + str(result[4]))
print("cha: " + str(result[5]))

total = 0
for stat in result:
    total += stat
print()
print("total: " + str(total))
