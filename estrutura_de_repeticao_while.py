""" condicao = 0

while condicao < 301:
    print(condicao + 3)
    condicao = condicao + 1 """


portal_atual = 20
while portal_atual <=25:
    print("antes",portal_atual)
    portal_atual +=1
    print("depois",portal_atual)
    if portal_atual == 22:
        print("Scaneando porta :",portal_atual)
    if portal_atual == 23:
        break
    print("Scaneando porta :",portal_atual)