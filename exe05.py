def calculadora(a, b, operacao):
    if operacao == "+":
        result = a + b
    elif operacao == "-":
        result = a - b
    elif operacao == "*":
        result = a * b
    else:
        result = a / b
    return result

print(calculadora(8, 3, "+"))
print(calculadora(8, 3, "-"))
print(calculadora(8, 3, "*"))
print(calculadora(8, 3, "/"))

