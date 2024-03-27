def longest_consec(strarr, k):
    l = ''
    if len(strarr) < k:
        return l
    if k <= 0 :
        return l
    for index in range(len(strarr)):
        combined_string = ''.join(strarr[index : index + k])
        if len(combined_string) > len(l):
            l = combined_string
    return l

# l = variavel definida por mim
# se o tamanho de strarr for menor que o de k, retornar a variavel vazia
# Se k for igual ou menor que zero, retornar a variavel vazia 
# por index na ordem de tamanho de Strarr:
# variavel para usar na combinação de strings; 'string'.combinar(strarr[index da lista : index + k]
# Se o tamanho da variavel for maior que l, l vira o resultado
# Retorne l
