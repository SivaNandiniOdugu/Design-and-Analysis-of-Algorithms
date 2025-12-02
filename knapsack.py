
container_capacity = 50  


syrups = [(6, 10), (5, 20), (4, 30)]

syrups.sort(reverse=True)

t_p = 0
used = []

for profit, avail in syrups:
    if container_capacity == 0:
        break
    if avail <= container_capacity:
        t_p += profit * avail
        used.append((avail, profit))
        container_capacity -= avail
    else:
        t_p += profit * container_capacity
        used.append((container_capacity, profit))
        container_capacity = 0

print("Max(Profit):", t_p)
print("Syrups used:")
for litres, p in used:
    print(litres, "litres at", p, "profit/litre")