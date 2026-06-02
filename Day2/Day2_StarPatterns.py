# Day 2 Star Patterns: common star pattern codes

# 1. Solid square pattern
size = 5
for i in range(size):
    print("* " * size)

print()

# 2. Left-aligned right-angle triangle (increasing)
for i in range(1, 6):
    print("* " * i)

print()

# 3. Left-aligned inverted right-angle triangle
for i in range(5, 0, -1):
    print("* " * i)

print()

# 4. Right-aligned right-angle triangle
n = 5
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * i)

print()

# 5. Right-aligned inverted right-angle triangle
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * i)

print()

# 6. Centered pyramid pattern
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))

print()

# 7. Inverted centered pyramid pattern
for i in range(n, 0, -1):
    print("  " * (n - i) + "* " * (2 * i - 1))

print()

# 8. Diamond pattern
for i in range(1, n + 1):
    print("  " * (n - i) + "* " * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print("  " * (n - i) + "* " * (2 * i - 1))

print()

# 9. Hollow square pattern
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * n)
    else:
        print("* " + "  " * (n - 2) + "* ")

print()

# 10. Hollow left-aligned triangle
for i in range(1, n + 1):
    if i == 1 or i == n:
        print("* " * i)
    else:
        print("* " + "  " * (i - 2) + "* ")

print()

# 11. Hollow centered pyramid
for i in range(1, n + 1):
    if i == 1:
        print("  " * (n - 1) + "*")
    elif i == n:
        print("* " * (2 * n - 1))
    else:
        print("  " * (n - i) + "* " + "  " * (2 * i - 3) + "* ")

print()

# 12. Hourglass / diamond outline
for i in range(n, 0, -1):
    if i == n:
        print("* " * (2 * i - 1))
    else:
        print("  " * (n - i) + "* " + "  " * (2 * i - 3) + "* ")
for i in range(2, n + 1):
    if i == n:
        print("* " * (2 * i - 1))
    else:
        print("  " * (n - i) + "* " + "  " * (2 * i - 3) + "* ")
