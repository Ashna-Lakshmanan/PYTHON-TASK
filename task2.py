def print_hexagon():
    print("", end="")
    print("\n /    \\", end="")
    print("\n/      \\", end="")
    print("\n\\      /", end="")
    print("\n \\____/", end="")

def print_hexagon_pattern(rows, columns):
    for i in range(columns):
        print("  ____ ", end="")
        if i % 2 == 0:
            for _ in range(3):
                print_hexagon()
        else: 
            for _ in range(2):
                print_hexagon()
        print() 
rows = 3
columns = 5
print_hexagon_pattern(rows, columns)