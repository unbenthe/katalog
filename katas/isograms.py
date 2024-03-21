def is_isogram(string):
    string = string.lower()
    count = 0
    for letter in string:
        ocorrencia = string.count(letter)
        count += ocorrencia
    return count == len(string)


# Consegui fazer a lógica mas copiei a string.lower. To fazendo pq im feeling like shit
