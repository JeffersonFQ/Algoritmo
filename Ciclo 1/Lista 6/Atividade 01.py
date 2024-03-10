# Crie um algoritmo que seja capaz de descobrir, por meio de perguntas lógicas (verdadeiro ou falso) 
# sobre características físicas, um animal que o usuário tenha em mente. Considere os animais: pato, 
# águia, galinha, avestruz, pinguim, morcego, ornitorrinco, leão, gato, onça pintada, baleia, tubarão, 
# lambari, enguia e arraia.

print("Considere os animais: pato, águia, galinha, avestruz, pinguim, morcego, ornitorrinco, leão, gato, onça pintada, baleia, tubarão, lambari, enguia e arraia.")
print("Pense em um animal e responda com 's' para Sim e 'n' para Não.")


A = str.lower(input("É uma ave? "))
if A == 's':
    voa = str.lower(input("Voa? "))
    if voa == 's':
        bico = str.lower(input("Bico pontudo? "))
        if bico == 's':
            print("O animal é uma águia.")
        else:
            dente = str.lower(input("Tem dentes? "))
            if dente == 's':
                print("O animal é um morcego.")
            else:
                print("O animal é um pato. ")
    else:
        pescoco = str.lower(input("Tem pescoço longo? "))
        if pescoco == 's':
            print("O animal que você pensou é um avestruz.")
        else:
            pena = str.lower(input("Tem pena? "))
            if pena == 's':
                print("O animal é uma galinha.")
            else:
                print("O animal é um pinguim.")
else:
    P = str.lower(input("Vive na água? "))
    if P == 's':
        mamifero = str.lower(input("É um mamífero? "))
        if mamifero == 's':
            bico = str.lower(input("Tem bico? "))
            if bico == 's':
                print("O animal é o ornitorrinco.")
            else:
                print("O animal é uma baleia.")
        else:
            escamas = str.lower(input("Possui escamas? "))
            if escamas == 's':
                print("O animal é um lambari.")
            else:
                achatado = str.lower(input("Tem o corpo achatado? "))
                if achatado == 's':
                    print("O animal é uma arraia.")
                else:
                    barbatana = str.lower(input("Tem barbatana dorsal? "))
                    if barbatana == 's':
                        print("O animal é um tubarão.")
                    else:
                        print("O animal é uma enguia.")
    else:
        juba = str.lower(input("Tem juba? "))
        if juba == 's':
            print("O animal que você pensou é um leão.")
        else:
            casa = str.lower(input("pode criar em casa? "))
            if casa == 's':
                print("O animal é um gato.")
            else:
                print("O animal é um leão.")

