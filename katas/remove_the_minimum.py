def remove_smallest(numbers):

    if len(numbers) == 0:
        return []
    menos = min(numbers)
    number = numbers.copy()
    number.remove(menos)
    return number

# pra tirar da lista os menores números, de qualquer ordem, primeiro vemos se a lista tem números, se não tem, volta nulo, definimos uma variável para os numeros menores e uma variável que cria uma cópia da lista, em seguida 
# usamos a função remove para remover os menores números da lista e retornamos a lista com a variavel com que copiamos ela antes.
