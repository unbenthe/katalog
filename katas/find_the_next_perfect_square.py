def find_next_square(sq):
    root = sq ** 0.5
    return (root + 1) ** 2 if root.is_integer() == True else -1


# Raiz = ao quadrado vezes 0,5
# Retornar a raiz + 1 ** 2 se a raiz é um integral, se não, retornar -1
