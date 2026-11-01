def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_non_recursive(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


n = int(input("Enter the number of terms: "))

print("\nFibonacci Series using Non-Recursive Method:")
fibonacci_non_recursive(n)

print("\nFibonacci Series using Recursive Method:")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")