def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    # BUG: não verifica divisão por zero
    return a / b

def calcular_media(numeros):
    # BUG: usa len() errado — deveria ser len(numeros), mas usa uma variável inexistente
    total = sum(numeros)
    return total / len

if __name__ == "__main__":
    print("=== Calculadora ===")
    print(f"10 + 5 = {somar(10, 5)}")
    print(f"10 - 3 = {subtrair(10, 3)}")
    print(f"4 * 7 = {multiplicar(4, 7)}")
    print(f"20 / 4 = {dividir(20, 4)}")

    notas = [8, 7, 9, 10, 6]
    print(f"Média das notas: {calcular_media(notas)}")
