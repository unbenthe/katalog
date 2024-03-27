def array_diff(a, b):
    lista = []
    for i in a:
        if i not in b:
            lista.append(i)
    return lista

# criar nova lista atrelada à uma variavel
# para cada número em a, checar se está em b, se não estiver, colocar na nova lista
#retornar a nova lista criada
