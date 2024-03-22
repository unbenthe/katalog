def dig_pow(n, p):
    sum = 0
    for number in str(n):
        sum += int(number)**p
        p += 1
    if sum % n == 0:
        return int(sum / n)
    else:
        return -1

  # Admito absolutamente que copiei isso pra tentar começar a entender esse caralho de coisa, vi aquele video e ainda quero que morra queimada com o fogo do mármore infernal que tipo de kata é esse lvl.6? quer destruir as esperanças das pessoas que querem começar desde o primeiro dia, que bom que só vi essa merda agora pqp que bando de arrombado.
