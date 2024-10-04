n = int(input())
for _ in range(n):
    entrada = input()
    conta = 0
    contc = 0
    diamantes = 0
    for i in entrada:
        if i == '<':
            conta += 1
        if i == '>':
            contc += 1
    if contc >= conta:
        diamantes = conta
    else:
        diamantes = contc
    print(diamantes)
