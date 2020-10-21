import math;

taylorSin = lambda x, n: \
    ((-1) ** (n - 1) * x ** (2 * n - 1)) / math.factorial(2 * n - 1);

taylorCos = lambda x, n: \
    ((-1) ** (n - 1) * x ** (2 * n - 2)) / math.factorial(2 * n - 2);

def taylor(type: str, x: float, n: int) -> float:
    while (n != 0):
        if (type == "sin"):
            if (n == 1): return x;
            else: return taylorSin(x, n) + taylor(type, x, n - 1);
        elif (type == "cos"):
            if (n == 1): return 1;
            else: return taylorCos(x, n) + taylor(type, x, n - 1);
        elif (type == "tan"):
            return taylor("sin", x, n - 1) / taylor("cos", x, n - 1);
        elif (type == "cot"):
            return 1 / taylor("tan", x, n - 1);
        else:
            pass;


# 30 градусов в радианах 0.523599
# 45 градусов в радианах 0.785398
# 60 градусов в радианах 1.0472

print(f"Самописаня функция: {taylor('sin', 0.523599, 80)}, библиотечная функция {math.sin(0.523599)}")
print(f"Самописаня функция: {taylor('cos', 0.785398, 80)}, библиотечная функция {math.cos(0.785398)}")
print(f"Самописаня функция: {taylor('tan', 1.0472, 80)}, библиотечная функция {math.tan(1.0472)}")
print(f"Самописаня функция: {taylor('cot', 0.523599, 80)}, библиотечная функция {1/math.tan(0.523599)}")
