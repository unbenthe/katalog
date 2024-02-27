def are_you_playing_banjo(name):
    if name.lower()[0] == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

# se a primeira letra do nome, forçado a ser minusculo, for 'r', o retorno será "name plays banjo", se não, será "name does not play banjo"
# lembrar da função .startswith('')
