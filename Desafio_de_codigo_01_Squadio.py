# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input())

if quantidade_passos == 0:
    print('Nenhum passo dado na floresta.')
if quantidade_passos>0:
    passo = 1
    while passo <= quantidade_passos:
       if passo == 1:
         print(f'Explorador: {passo} passo')
         passo+=1
       else:
         print(f'Explorador: {passo} passos')
         passo+=1
else:
  pass