import math
e = 0
maior = 0
while e != 18:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print('[1] Somar\n'
          '[2] Multiplicar\n'
          '[3] Subtração\n'
          '[4] Média\n'
          '[5] Maior número e menor número\n'
          '[6] Divisão (Maior/Menor)\n'
          '[7] Fatorial\n'
          '[8] Raiz Quadrada\n'
          '[9] Elevado ao Quadrado/Cubo\n'
          '[10] Tabuada\n'
        f'[11] {n1}° para Radiano // {n2}° para Radiano\n'
          '[12] Seno/Cosseno/Tangente\n'
          '[13] Calcular Hipotenusa\n'
          '[14] Fibonacci\n'
        f'[15] Converter {n1}°C e {n2}°C para Fahrenheit\n' 
          '[16] Mais informações\n'
          '[17] Novos Números\n'
          '[18] Sair do programa')
    e = int(input('Qual operação matemática deseja fazer? '))
    print(f'Sua escolha: {e}\n-----------RESULTADO-----------')
    if e == 1:
        print(f'A soma entre {n1} e {n2} é igual a: {n1+n2}')
        print()
    elif e == 2:
        print(f'A multiplicação entre {n1} e {n2} é igual a: {n1*n2}')
        print()
    elif e == 3:
        print(f'A subtração entre {n1} e {n2} é igual a: {n1-n2}')
        print()
    elif e == 4:
        print(f'A média entre {n1} e {n2} é igual a: {(n1+n2)/2}')
        print()
    elif e == 5:
        if n1 > n2:
            maior = n1
            menor = n2
        elif n2 > n1:
            maior = n2
            menor = n1
        print(f'O maior número: {maior}\nO menor número: {menor}')
        print()
    elif e == 6:
        if n1 > n2:
            print(f'{n1} dividido por {n2} é igual a: {n1/n2}')
            print()
        elif n2 > n1:
            print(f'{n2} dividido por {n1} é igual a: {n2/n1}')
            print()
    elif e == 7:
        print(f'Fatorial de {n1} -> {math.factorial(n1)}')
        print(f'Fatorial de {n2} -> {math.factorial(n2)}')
        print()
    elif e == 8:
        print(f'Raiz Quadrada de {n1} -> {math.sqrt(n1):.2f}')
        print(f'Raiz Quadrada de {n2} -> {math.sqrt(n2):.2f}')
        print()
    elif e == 9:
        print(f'{n1}² -> {n1*n1} // {n1}³ -> {n1*n1*n1}')
        print(f'{n2}² -> {n2*n2} // {n2}³ -> {n2*n2*n2}')
        print()
    elif e == 10:
        for c in range(11):
            print(f'{n1} x {c} = {n1*c}')
        print('='*25)
        for c in range(11):
            print(f'{n2} x {c} = {n2 * c}')
        print()
    elif e == 11:
        print(f'{n1}° para radianos -> {math.radians(n1):.6f}')
        print(f'{n2}° para radianos -> {math.radians(n2):.6f}')
        print()
    elif e == 12:
        print(f'Cosseno de {n1}: {math.cos(n1):.10f}\nSeno de {n1}: {math.sin(n1):.10f}\nTangente de {n1}: {math.tan(n1):.10f}')
        print('='*25)
        print(f'Cosseno de {n2}: {math.cos(n1):.10f}\nSeno de {n2}: {math.sin(n2):.10f}\nTangente de {n2}: {math.tan(n2):.10f}')
        print()
    elif e == 13:
        print(f'Considerando {n1} como cateto oposto e {n2} como cateto adjacente, a hipotenusa é igual a: {math.sqrt(n1**2+n2**2):.3f}')
        print()
    elif e == 14:
        a = 0
        b = 1
        print(f'Os {n1} primeiros termos da sequência de Fibonacci: {a}, {b}', end=' ')
        contador = 1
        while contador <= n1-2:
            c = a + b
            a = b
            b = c
            print(f', {c}', end=' ')
            contador += 1
        print()
        a = 0
        b = 1
        print(f'Os {n2} primeiros termos da sequência de Fibonacci: {a}, {b}', end=' ')
        contador = 1
        while contador <= n2-2:
            c = a + b
            a = b
            b = c
            print(f', {c}', end=' ')
            contador += 1
        print()
        print()
    elif e == 15:
        print(f'{n1}°C para Fahrenheit é igual a: {n1 * 1.8 + 32}°F')
        print(f'{n2}°C para Fahrenheit é igual a: {n2 * 1.8 + 32}°F')
        print()
    elif e == 16:
        contador = 0
        for c in range(1, n1 + 1):
            if n1 % c == 0:
                contador += 1
            else:
                continue
        if contador == 2:
            print(f'{n1} é Número Primo? ✅')
        else:
            print(f'{n1} é Número Primo? ❌')
        contador = 0
        for c in range(1, n2 + 1):
            if n2 % c == 0:
                contador += 1
            else:
                continue
        if contador == 2:
            print(f'{n2} é Número Primo? ✅')
        else:
            print(f'{n2} é Número Primo? ❌')
        print()

        if n1%2 == 0:
            print(f'{n1} é Par? ✅ / {n1} é Ímpar? ❌')
        else:
            print(f'{n1} é Par? ❌ / {n1} é Ímpar? ✅')

        if n2%2 == 0:
            print(f'{n2} é Par? ✅ / {n2} é Ímpar? ❌')
        else:
            print(f'{n2} é Par? ❌ / {n2} é Ímpar? ✅')
        print()
    elif e == 17:
        e = 0
    elif e == 18:
        print(f'Programa encerrado.')
        break
    elif e > 18 or e <= 0:
        print('Por favor, escolha entre as opções 1 a 18 somente.')
        print('Programa reiniciado.')
        print()
        e == 0
