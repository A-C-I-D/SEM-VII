def fractional_knapsack(w, p, capacity):
    n = len(w)

    ratio = []
    for i in range(n):
        ratio.append(p[i] / w[i])

    items = sorted(zip(ratio, w, p), reverse=True)

    total_profit = 0

    for r, weight, profit in items:
        if capacity >= weight:
            capacity -= weight
            total_profit += profit
        else:
            total_profit += r * capacity
            break

    return total_profit

n = int(input("Enter number of items: "))

w = []
p = []

for i in range(n):
    weight = int(input("Enter weight of item: "))
    profit = int(input("Enter profit of item: "))
    w.append(weight)
    p.append(profit)

capacity = int(input("Enter knapsack capacity: "))

max_profit = fractional_knapsack(w, p, capacity)

print("Maximum Profit:", max_profit)