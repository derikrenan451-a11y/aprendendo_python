componentes = ["Teclado","Mouse","Monitor"]

print(componentes)
print(componentes[0])
print(componentes[-2])

componentes.append("Gabinete")

print(componentes)
print(componentes[0])
print(componentes[-1])

componentes.remove("Mouse")

print(componentes)
print(componentes[0])
print(componentes[-2])

for i in range(3):
    if i == 0:
        print(componentes[i])