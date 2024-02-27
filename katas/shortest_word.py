def find_short(s):
    s_list = s.split()
    começo = len(s_list[0])
    for word in s_list:
        if len(word) < começo:
            começo = len(word)
    return  começo


#definir achar a menor palavra em s
# lista s = partir lista de strings
# começo = tamanho da primeira string na lista s
#por palavra na lista s:
# se o comprimento da palavra for maior que a inicial, esta toma o lugar da ultima
# retorne o valor da variável
