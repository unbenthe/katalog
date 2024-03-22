def solution(s):
    x = ""
    for letter in s:
        if letter == letter.upper():
            x += " " + letter
        if letter != letter.upper():
            x += letter
    return x         

# variável insere uma string vazia, que é completa com a dada, caso exista uma letra maiuscula nela, o código faz com que seja adicionado um espaço antes dela, se não, o código retorna a string como estava.
