def to_jaden_case(string):
    return ' '.join(i.capitalize() for i in string.split(" "))

# tomar cuidado com " " vs ' ';  ' ' > string vazia que vai ser preenchida automaticamente, join para juntar a versão capitalizada de cada palavra em uma sentença novamente.
