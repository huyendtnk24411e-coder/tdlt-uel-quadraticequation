import math

def first_degree(a, b):

    if a == 0:
        if b == 0:
            return "Phương trình có vô số nghiệm"
        else:
            return "Phương trình vô nghiệm"
    else:
        x = -b / a
        return f"Phương trình có nghiệm x = {x}"

def quadratic_equation(a, b, c):

    if a == 0:

        return first_degree(b, c)

    delta = b**2 - 4*a*c

    if delta < 0:
        return "Phương trình vô nghiệm"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép x₁ = x₂ = {x}"
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có hai nghiệm phân biệt: x₁ = {x1}, x₂ = {x2}"