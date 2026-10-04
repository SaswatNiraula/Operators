def allops():

    # Samples of Operators
    # Arithmetic Operators
    print("Addition: ", 5 + 3)              # 8
    print("Subtraction: ", 5 - 3)           # 2
    print("Multiplication: ", 5 * 3)        # 15
    print("Division: ", 5 / 3)              # 1.66
    print("Modulus: ", 5 % 3)               # 2
    print("Exponentiation: ", 5 ** 3)       # 125
    print("Floor Division: ", 5 // 3)       # 1
    # Comparison (Relational) Operators
    print("Equal: ", 5 == 3)                # False
    print("Not Equal: ", 5 != 3)            # True
    print("Greater Than: ", 5 > 3)          # True
    print("Less Than: ", 5 < 3)             # False
    print("Greater Than or Equal To: ", 5 >= 3)  # True
    print("Less Than or Equal To: ", 5 <= 3)     # False
    # Assignment Operators
    x = 10
    x += 5
    print("Add Assignment: ", x)             # 15
    x -= 3
    print("Subtract Assignment: ", x)        # 12
    x *= 2
    print("Multiply Assignment: ", x)        # 24
    x /= 4
    print("Divide Assignment: ", x)         # 6.0
    x //= 2
    print("Floor Divide Assignment: ", x)   # 3.0
    x %= 2
    print("Modulus Assignment: ", x)        # 1.0
    x **= 3
    print("Exponent Assignment: ", x)       # 1.0
    # Logical Operators
    print("Logical AND: ", True and False)  # False
    print("Logical OR: ", True or False)    # True
    print("Logical NOT: ", not True)        # False
    # Bitwise Operators
    print("Bitwise AND: ", 5 & 3)           # 1
    print("Bitwise OR: ", 5 | 3)            # 7
    print("Bitwise XOR: ", 5 ^ 3)           # 6
    print("Bitwise NOT: ", ~5)              # -6
    # Left shift — multiply by powers of 2
    print("Left Shift 1: ", 5 << 1)          # 10 (5 × 2)
    print("Left Shift 2: ", 5 << 2)          # 20 (5 × 4)
    # Right shift — divide by powers of 2
    print("Right Shift 1: ", 20 >> 1)        # 10 (20 ÷ 2)
    print("Right Shift 2: ", 20 >> 2)        # 5 (20 ÷ 4)
    # Membership Operators
    print("Membership: ", 5 in [1, 2, 3, 4, 5])       # True
    print("Not Membership: ", 6 not in [1, 2, 3, 4, 5]) # True
    
    # Identity Operators
    a = [1, 2, 3]
    b = a
    c = [1, 2, 3]
    print("Identity: ", a is b)              # True
    print("Non-Identity: ", a is not c)     # True
allops()
