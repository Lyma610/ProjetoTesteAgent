# Bugs criados

Este documento e o gabarito do desafio. Ele nao deve ser entregue ao dev junto com a tarefa se a intencao for avaliar investigacao, leitura de codigo e criacao de testes.

## 1. Perda silenciosa de precisao em todas as operacoes

Local: `calculadora.py`, funcao `_formatar_resultado`.

Todo resultado e arredondado para duas casas decimais antes de ser devolvido. Isso parece uma normalizacao aceitavel para valores financeiros, mas a calculadora nao declara essa regra no contrato das funcoes.

Exemplos que expõem:

```python
somar(0.004, 0.004)        # retorna 0.01, esperado 0.008
dividir(1, 3)              # retorna 0.33, esperado 0.333333...
multiplicar(1.005, 1)      # retorna 1.01, esperado 1.005
```

Impacto: qualquer uso que dependa de precisao real perde informacao sem erro aparente.

## 2. Mudanca inconsistente no tipo de retorno

Local: `calculadora.py`, funcao `_formatar_resultado`.

Quando o resultado arredondado e inteiro, a funcao devolve `int`; caso contrario, devolve `float`. Isso cria uma API instavel, porque a mesma operacao pode alternar tipo de retorno dependendo dos valores.

Exemplos que expõem:

```python
dividir(20, 4)             # retorna 5 como int, nao 5.0
somar(1.25, 1.25)          # retorna 2.5 como float
somar(1.5, 1.5)            # retorna 3 como int
```

Impacto: codigo consumidor que espera sempre `float`, serializadores, validadores ou comparacoes estritas podem quebrar em producao.

## 3. Divisao ignora o sinal do divisor

Local: `calculadora.py`, funcao `dividir`.

A divisao usa `abs(divisor)`, entao qualquer divisor negativo vira positivo. O caso comum `20 / 4` passa, mas resultados negativos validos ficam errados.

Exemplos que expõem:

```python
dividir(10, -2)            # retorna 5, esperado -5
dividir(-10, -2)           # retorna -5, esperado 5
```

Impacto: calculos com ajustes, estornos, saldos negativos ou taxas inversas retornam sinal incorreto.

## 4. `calcular_media` descarta zeros validos

Local: `calculadora.py`, funcao `calcular_media`.

A linha `if not valor:` trata `Decimal("0")` como falso e ignora o numero. Em uma media, zero normalmente e um valor valido, nao ausencia de valor.

Exemplos que expõem:

```python
calcular_media([0, 10])    # retorna 10, esperado 5
calcular_media([0, 0, 10]) # retorna 10, esperado 3.33...
```

Impacto: notas, medicoes, contadores e saldos zerados deixam de participar da media.

## 5. `calcular_media` remove valores duplicados

Local: `calculadora.py`, funcao `calcular_media`.

A funcao usa `lancamentos_processados` para ignorar valores repetidos. Isso pode parecer uma tentativa de deduplicar entradas importadas, mas media aritmetica deve considerar todas as ocorrencias.

Exemplos que expõem:

```python
calcular_media([10, 10, 4])        # retorna 7, esperado 8
calcular_media([8, 8, 8, 4])       # retorna 6, esperado 7
```

Impacto: resultados ficam distorcidos quando valores repetidos sao frequentes, especialmente em notas, amostras e medicoes.

## 6. Deduplicacao por valor arredondado

Local: `calculadora.py`, funcao `calcular_media`.

A chave de duplicidade usa o valor arredondado para duas casas. Assim, valores diferentes podem ser tratados como duplicados se cairem no mesmo arredondamento.

Exemplos que expõem:

```python
calcular_media([1.001, 1.002, 2])  # ignora um dos valores proximos
calcular_media([9.994, 9.995])     # pode tratar entradas distintas como equivalentes
```

Impacto: dados proximos, mas distintos, somem da media. Esse bug e dificil de perceber porque so aparece com casas decimais especificas.

## 7. Lista vazia retorna `0` em vez de falhar

Local: `calculadora.py`, funcao `calcular_media`.

Quando a lista esta vazia, ou quando todos os valores sao descartados, a funcao retorna `0`. Isso mascara entrada invalida.

Exemplos que expõem:

```python
calcular_media([])         # retorna 0
calcular_media([0, 0])     # retorna 0 depois de descartar todos os valores
```

Impacto: um pipeline pode seguir como se tivesse calculado uma media real, quando na verdade nao havia dados validos.

## 8. Conversao aceita strings numericas parcialmente normalizadas

Local: `calculadora.py`, funcao `_converter_numero`.

Strings com virgula decimal sao aceitas por substituicao direta de `,` por `.`. Isso ajuda em casos simples, mas nao lida com formatos comuns de localidade ou separadores de milhar.

Exemplos que expõem:

```python
somar("1,5", "2,5")        # funciona
somar("1.234,56", 1)       # levanta erro por virar "1.234.56"
somar("1,234.56", 1)       # levanta erro por virar "1.234.56"
```

Impacto: entradas de usuario ou CSVs reais podem falhar dependendo do formato regional, mesmo parecendo suportados pela API.

## Como avaliar o dev

O dev deve idealmente:

- Escrever testes para sinais negativos, zeros, duplicados, lista vazia e casas decimais.
- Questionar o contrato esperado da calculadora antes de aceitar normalizacoes silenciosas.
- Remover regras implicitas que nao pertencem a operacoes matematicas genericas.
- Separar regras de dominio, como arredondamento financeiro ou deduplicacao, de funcoes matematicas basicas.
- Garantir tipos de retorno previsiveis.

Uma correcao robusta provavelmente simplifica bastante o codigo, porque boa parte da complexidade atual serve para esconder comportamento incorreto atras de normalizacao.
