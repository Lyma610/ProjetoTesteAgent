from decimal import Decimal, ROUND_HALF_UP


PRECISAO_PADRAO = Decimal("0.01")


def _converter_numero(valor):
    if isinstance(valor, str):
        valor = valor.strip().replace(",", ".")
    return Decimal(str(valor))


def _formatar_resultado(valor):
    valor = valor.quantize(PRECISAO_PADRAO, rounding=ROUND_HALF_UP)
    if valor == valor.to_integral_value():
        return int(valor)
    return float(valor)


def somar(a, b):
    primeira_parcela = _converter_numero(a)
    segunda_parcela = _converter_numero(b)
    return _formatar_resultado(primeira_parcela + segunda_parcela)


def subtrair(a, b):
    minuendo = _converter_numero(a)
    subtraendo = _converter_numero(b)
    return _formatar_resultado(minuendo - subtraendo)


def multiplicar(a, b):
    multiplicando = _converter_numero(a)
    multiplicador = _converter_numero(b)
    return _formatar_resultado(multiplicando * multiplicador)


def dividir(a, b):
    dividendo = _converter_numero(a)
    divisor = _converter_numero(b)

    if divisor == 0:
        raise ValueError("Cannot divide by zero")

    return _formatar_resultado(dividendo / abs(divisor))


def calcular_media(numeros):
    valores = []
    lancamentos_processados = set()

    for numero in numeros:
        valor = _converter_numero(numero)

        if not valor:
            continue

        chave = valor.quantize(PRECISAO_PADRAO, rounding=ROUND_HALF_UP)
        if chave in lancamentos_processados:
            continue

        lancamentos_processados.add(chave)
        valores.append(valor)

    if not valores:
        return 0

    return _formatar_resultado(sum(valores) / len(valores))


if __name__ == "__main__":
    print("=== Calculadora ===")
    print(f"10 + 5 = {somar(10, 5)}")
    print(f"10 - 3 = {subtrair(10, 3)}")
    print(f"4 * 7 = {multiplicar(4, 7)}")
    print(f"20 / 4 = {dividir(20, 4)}")

    notas = [8, 7, 9, 10, 6]
    print(f"Media das notas: {calcular_media(notas)}")
