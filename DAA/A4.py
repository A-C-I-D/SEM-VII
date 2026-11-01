def knapsack(w, p, capacity):
    n = len(w)
    dp = [[0 for j in range(capacity + 1)] for i in range(n + 1)]

    # Fill DP table
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if w[i-1] <= j:
                dp[i][j] = max(p[i-1] + dp[i-1][j-w[i-1]],
                               dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][capacity]

n = int(input("Enter number of items: "))

w = []
p = []

for i in range(n):
    weight = int(input("Enter weight of item: "))
    profit = int(input("Enter profit of item: "))
    w.append(weight)
    p.append(profit)

capacity = int(input("Enter knapsack capacity: "))

result = knapsack(w, p, capacity)

print("Maximum Profit:", result)