import math;

# сигма по нулю
taylorSin = lambda x, n: \
    (((-1) ** (n) * x ** (2 * n + 1))) / math.factorial(2 * n + 1);

# сигма по нулю
taylorCos = lambda x, n: \
    (((-1) ** (n) * x ** (2 * n))) / math.factorial(2 * n);

# сигма по нулю
taylorAtan = lambda x, n: \
    (((-1) ** (n) * x ** (2 * n + 1))) / (2 * n + 1);


def taylor(type: str, x: float, n: int) -> float:
    while (n >= 0):
        if (type == "sin"):
            if (n == 0): return taylorSin(x, 0);
            else: return taylorSin(x, n) + taylor(type, x, n - 1);
        elif (type == "cos"):
            if (n == 0): return taylorCos(x, 0);
            else: return taylorCos(x, n) + taylor(type, x, n - 1);
        elif (type == "tan"):
            return taylor("sin", x, n - 1) / taylor("cos", x, n - 1);
        elif (type == "atan"):
            if (n == 0): return taylorAtan(x, 0);
            else: return taylorAtan(x, n) + taylor(type, x, n - 1);
        else:
            pass;


# 30 градусов в радианах 0.523599
# 45 градусов в радианах 0.785398
# 60 градусов в радианах 1.0472

print(f"Самописная функция: {taylor('sin', 0.523599, 2)}, библиотечная функция {math.sin(0.523599)}");
print(f"Самописная функция: {taylor('cos', 0.785398, 2)}, библиотечная функция {math.cos(0.785398)}");
print(f"Самописная функция: {taylor('tan', 1.0472, 2)}, библиотечная функция {math.tan(1.0472)}");
print(f"Самописная функция: {taylor('atan', 1, 2)}, библиотечная функция {math.atan(1)}");
print(f"Самописная функция: {taylor('sin', 0.523599, 3)}, библиотечная функция {math.sin(0.523599)}");
print(f"Самописная функция: {taylor('cos', 0.785398, 3)}, библиотечная функция {math.cos(0.785398)}");
print(f"Самописная функция: {taylor('tan', 1.0472, 3)}, библиотечная функция {math.tan(1.0472)}");
print(f"Самописная функция: {taylor('atan', 1, 3)}, библиотечная функция {math.atan(1)}");
