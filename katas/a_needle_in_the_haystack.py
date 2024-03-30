def find_needle(haystack):
    for index in range(len(haystack)):
        if haystack[index] == 'needle':
            return "found the needle at position {}" .format(index)
# por posição no comprimento inteiro de haystack, se existir needle, copiar a posição e retornar a frase com a posição
