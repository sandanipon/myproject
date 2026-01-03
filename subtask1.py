n = int(input("Enter a natural number n: "))

p = 0
while p * p <= n:
    p = p + 1

q = (p-1) * (p-1)
print("Largest square less than or equal to n is:", q)

# it looks like I learned how to use git today
