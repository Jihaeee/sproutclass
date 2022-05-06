# 2557
print("Hello World!")

# 1000
A, B = input().split()
A = int(A)
B = int(B)

if A > 0 and B < 10:
    print(A + B)

# 1001
A, B = input().split()
A = int(A)
B = int(B)

if A > 0 and B < 10:
    print(A - B)

# 10998
A, B = input().split()
A = int(A)
B = int(B)

if A > 0 and B < 10:
    print(A * B)

# 1008
A, B = input().split()
A = int(A)
B = int(B)

if A > 0 and B < 10:
    print(A / B)

# 10869
A, B = input().split()
A = int(A)
B = int(B)

if A >= 0 and B <= 10000:
    print(A + B)
    print(A - B)
    print(A * B)
    print(A // B)
    print(A % B)

# 10430
A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)
print((A + B) % C)
print(((A % C) + (B % C)) % C)
print((A * B) % C)
print(((A % C) * (B % C)) % C)

# 2558
A = int(input())
B = int(input())
if A > 0 and B < 10:
    print(A + B)

# 2588
A = int(input())
B = int(input())

print(A * (B % 10))
print(A * (B % 100 // 10))
print(A * (B // 100))
print(A * B)

# 3046
R1, S = input().split()
R1 = int(R1)
S = int(S)
R2 = 2 * S - R1
print(R2)

# 11021
T = int(input())
for i in range(1, T + 1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A + B}")

# 11022
T = int(input())
for i in range(1, T + 1):
    A, B = map(int, input().split())
    print(f"Case #{i}: {A} + {B} = {A + B}")

#2163