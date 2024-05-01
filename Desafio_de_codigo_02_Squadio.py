# Lista para armazenar os itens
itens = []

for x in range(3):
    x = input()
    itens.append(x)


# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")