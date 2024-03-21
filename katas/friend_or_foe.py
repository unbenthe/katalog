def friend(x):
    friends = []
    for word in x: 
        if len(word) == 4:
            friends.append(word)
    return friends

# friends é uma variável de agregamento, que eu usei pra juntar os nomes de 4 letras para que fossem retornados depois
