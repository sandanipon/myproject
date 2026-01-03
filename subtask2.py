n = 0          # count
s = 0          # sum
m = None       # minimum
x = int(input("Enter a natural number (or -1 to stop): "))

while x != -1:
    n = n + 1
    s = s + x

    if m is None or x < m:
        m = x

    x = int(input("Enter a natural number (or -1 to stop): "))

if n == 0:
    m = -1
    a = -1
else:
    a = s / n

print("n =", n)
print("s =", s)
print("m =", m)
print("a =", a)
